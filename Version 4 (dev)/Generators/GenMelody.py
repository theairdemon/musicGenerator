import random
import sys

from Builders.ScaleBuilder import ScaleBuilder
from Genres.DefineGenre import *

sys.path.append("D:\Documents\Github\musicGenerator\Version 4 (dev)")

# Custom module imports


class GenMelody:

    def __init__(self, genre, scale, chords, chord_notes, rhythm):
        self.genre = genre
        self.scale = scale
        self.chords = chords
        self.chord_notes = chord_notes
        self.length = len(chords)
        self.rhythm = rhythm

        self.melody = []
        self.melody_info = None
        self.volumes = []

    def build(self) -> tuple[list[float], list[int]]:
        self.melody_info = self.genre.get("Melody")
        self.genMelody()
        return self.melody, self.volumes

    # ============ #
    # BUILD MELODY #
    # ============ #
    def genMelody(self) -> None:
        for i in range(0, self.length):
            self.melody.append(self.genMeasure(i))
            self.volumes.append(self.genVolume(i))

    def genMeasure(self, idx) -> list[float]:
        starting_note = random.choice(self.chord_notes[idx])
        measure = [[starting_note, self.rhythm[idx][0]]]

        measure_scale = self._pick_chord_scale(idx)

        # loop over the rhythm and build notes from it
        # rough outline:
        # 0. if the rhythm is the same for the measures, we want to repeat the notes as closely as possible while making sense for the current chord
        # 1. weighted pick of continuing the "direction" of the note movement, i.e., if notes are going up, then continue that trend, and vice-versa
        # 2. if the length of the note is more than a quarter, only play a note from the chord (but still close to the previous note preferably)
        # 3. pick a random note in the scale, somewhere within 2 of the original
        if idx > 1:
            repeated_idx, does_repeat, ratio = self.comparePreviousMeasures(idx)
            if does_repeat:
                measure = self.adjustMeasure(repeated_idx, idx, ratio, measure_scale)

        measure_progression = self.determineProgression()

        for j in range(len(measure), len(self.rhythm[idx])):
            measure.append(
                self.genNote(measure, idx, j, measure_progression, measure_scale)
            )

        return measure

    def genNote(self, measure, measure_idx, idx, progression, measure_scale):
        prev_note = measure[idx - 1][0]
        note = prev_note
        scale_idx = self._check_index(prev_note, idx)

        # Make a list of the possible note_indices we can move to
        note_indices = []
        for note_idx in list(self.melody_info.note_weights.keys()):
            if progression >= 0:
                note_indices.append(note_idx)
            if progression <= 0:
                note_indices.append(-1 * note_idx)

        note_choices = {
            n: measure_scale[(scale_idx + n) % len(measure_scale)] for n in note_indices
        }

        r_note = random.uniform(0, 1)
        current_weights = 0
        for key in list(self.melody_info.note_weights.keys()):
            current_weights += self.melody_info.note_weights[key]
            if r_note <= current_weights:
                random_choices = (
                    [key, -1 * key] if progression == 0 else [progression * key]
                )
                note = note_choices[random.choice(random_choices)]
                return [note, self.rhythm[measure_idx][idx]]

        return [note, self.rhythm[measure_idx][idx]]

    def genVolume(self, idx):
        # TODO: redo this generation!! it's wayyy to jarring
        volumes = []
        measure = self.melody[idx]
        rest_weights = self.melody_info.rest_weights

        running_total = 0
        skip_next = False
        for i in range(len(measure)):
            note = measure[i][1]
            running_total += note
            if skip_next:
                skip_next = False
                continue

            if running_total > 3:
                if random.uniform(0, 1) < rest_weights[2]:
                    volumes.append(0)
                else:
                    volumes.append(100)
            elif running_total > 2:
                if random.uniform(0, 1) < rest_weights[1]:
                    volumes.append(0)
                else:
                    volumes.append(100)
            else:
                if random.uniform(0, 1) < rest_weights[0]:
                    volumes.append(0)
                else:
                    volumes.append(100)
            if i < len(measure) - 1 and note < 1 and volumes[-1] == 0:
                skip_next = True
                volumes.append(0)
        return volumes

    # ================ #
    # HELPER FUNCTIONS #
    # ================ #

    # Determine a particular measure's progression
    # Return -1, 0, or 1 for down, random, or up, respectively

    def determineProgression(self):
        r = random.uniform(0, 1)
        if r <= self.melody_info.progressions["in-measure"]:
            return random.choice([-1, 1])
        return 0

    # "Adjusts" the original_measure parameter to better fit our chord_notes[idx]
    # Begins at starting note, adjusts all others accordingly
    # Returns the adjusted measure in the measure-array format
    def adjustMeasure(self, previous_idx, idx, ratio, measure_scale):
        cut_length = int(len(self.melody[previous_idx]) / ratio)
        # reference measure, for easy comparison
        ref_measure = self.melody[previous_idx][:cut_length]
        # working measure, to be changed throughout the adjustments
        working_measure = self.melody[previous_idx][:cut_length]

        # if perfect replication, then return measure as-is, no changes
        r_perfect = random.uniform(0, 1)
        if r_perfect <= self.melody_info.measure_adjustments["perfect"]:
            return working_measure

        # if inverted, then invert the direction of the notes, and continue
        r_inverted = random.uniform(0, 1)
        if r_inverted <= self.melody_info.measure_adjustments["inverted"]:
            working_measure = [
                [working_measure[-1 * (i + 1)][0], working_measure[i][1]]
                for i in range(len(working_measure))
            ]

        # if chord, then set the starting note to the same chord position as the ref_measure and adjust all other notes correspondingly, and return
        r_chord = random.uniform(0, 1)
        if r_chord <= self.melody_info.measure_adjustments["chord"]:
            return self.chordBasedMeasure(
                previous_idx, idx, working_measure, measure_scale
            )

        # if slight, then go through and adjust starting note and any >= 1/4th notes to the closest chord note in the trending direction, adjusting the following notes correspondingly
        r_slight = random.uniform(0, 1)
        if r_slight <= self.melody_info.measure_adjustments["slight"]:
            return self.slightBasedMeasure(
                previous_idx, idx, working_measure, measure_scale
            )
        return working_measure

    # Performs slight adjustments to pull chord_notes to our current chords
    def slightBasedMeasure(self, previous_idx, idx, measure, measure_scale):
        previous_chord_notes = self.chord_notes[previous_idx]
        chord_notes = self.chord_notes[idx]

        fixed_measure = []
        for note in measure:
            # if we see a previous chord's note that's not in our current chord, let's adjust
            # pull that note to the closest chord note we have
            # this guarantees the first note is always in our chord
            if note[0] in previous_chord_notes and note[0] not in chord_notes:
                previous_note_idx = self._check_index(note[0], idx)
                chord_note_differences = [
                    self._check_index(elem, idx) - previous_note_idx
                    for elem in chord_notes
                ]
                closest_note_diff = min(chord_note_differences, key=abs)
                closest_note_idx = (previous_note_idx + closest_note_diff) % len(
                    measure_scale
                )
                closest_note = measure_scale[closest_note_idx]
                fixed_measure.append([closest_note, note[1]])
            else:
                fixed_measure.append(note)

        return fixed_measure

    # Adjusts a measure based off the input index and previous index
    # Uses our "chord" method, finding the corresponding chord note
    def chordBasedMeasure(self, previous_idx, idx, measure, measure_scale):
        previous_measure = self.melody[previous_idx]
        previous_starting_note = previous_measure[0][0]
        # find chord note position
        chord_note_idx = self.chord_notes[previous_idx].index(previous_starting_note)
        # find position of relative chord notes for current measure
        starting_note = self.chord_notes[idx][chord_note_idx]
        # now find difference between scale positions of these notes
        note_difference = self._check_index(starting_note, idx) - self._check_index(
            previous_starting_note, idx
        )

        fixed_measure = []
        for note in measure:
            previous_note_idx = self._check_index(note[0], idx)
            new_note_idx = (previous_note_idx + note_difference) % len(measure_scale)
            fixed_measure.append([measure_scale[new_note_idx], note[1]])

        return fixed_measure

    # Compares a given index against all previous measures of rhythm
    # Return value: integer, boolean, integer = index of found measure, "True" if either are the same, and the ratio for the cut length
    def comparePreviousMeasures(self, idx):
        for i in range(0, idx):
            if self.compareOneMeasure(i, idx, 1):
                return i, True, 1
            elif self.compareOneMeasure(i, idx, 2):
                return i, True, 2
        return i, False, 1

    def compareOneMeasure(self, previous_idx, idx, ratio):
        current_measure = self.rhythm[idx]
        previous_measure = self.rhythm[previous_idx]
        cut_length = int(len(previous_measure) / ratio)

        # if full measure is the same (ratio = 1), lengths should be the same
        # if half measure is the same (ratio = 2), then length >= cut_length
        if len(current_measure) < cut_length:
            return False

        # index won't run over due to previous if statement
        cut_current_measure = current_measure[:cut_length]
        cut_previous_measure = previous_measure[:cut_length]

        return cut_current_measure == cut_previous_measure

    # Scale-agnostic checking index
    # Might need tweaking but should stop outright failures
    def _check_index(self, elem, idx):
        if elem in self.scale:
            return self.scale.index(elem)
        if idx >= len(self.chord_notes):
            return 0
        else:
            if self.chord_notes[idx][0] in self.scale:
                return self.scale.index(self.chord_notes[idx][0])
            else:
                temp_scale = self._pick_chord_scale(idx)
                if elem in temp_scale:
                    return temp_scale.index(elem)
        # If all else fails, just return index of very first note
        return 0

    # Find the right scale for this measure
    def _pick_chord_scale(self, idx):
        if self._is_chord_in_scale(self.chord_notes[idx], self.scale):
            return self.scale
        else:
            scaleBuilder = ScaleBuilder(self.chord_notes[idx][0], "major")
            major_scale = scaleBuilder.build_scale(style="major")
            minor_scale = scaleBuilder.build_scale(style="minor")
            chord_major_scale = scaleBuilder.build_scale(
                self.chord_notes[idx][0], style="major"
            )
            chord_minor_scale = scaleBuilder.build_scale(
                self.chord_notes[idx][0], style="minor"
            )
            if self._is_chord_in_scale(self.chord_notes[idx], major_scale):
                return major_scale
            elif self._is_chord_in_scale(self.chord_notes[idx], minor_scale):
                return minor_scale
            elif self._is_chord_in_scale(self.chord_notes[idx], chord_major_scale):
                return major_scale
            elif self._is_chord_in_scale(self.chord_notes[idx], chord_minor_scale):
                return minor_scale
            else:
                print("Issue with parsing chord into scale from some reason, weird lol")
                return self.scale

    def _is_chord_in_scale(self, chord_notes, scale):
        count = 0
        for note in chord_notes:
            if note in scale:
                count += 1
        if count == 3:
            return True
        else:
            return False
