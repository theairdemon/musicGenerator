from Genres.DefineGenre import *
import random
import sys
sys.path.append('D:\Documents\Github\musicGenerator\Version 4 (dev)')

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

    def build(self):
        self.melody_info = self.genre.get('Melody')
        self.genMelody()
        return self.melody

    # ============ #
    # BUILD MELODY #
    # ============ #
    def genMelody(self):
        for i in range(0, self.length):
            self.melody.append(self.genMeasure(i))

    def genMeasure(self, idx):
        starting_note = random.choice(self.chord_notes[idx])
        measure = [[starting_note, self.rhythm[idx][0]]]

        # loop over the rhythm and build notes from it
        # rough outline:
        # 0. if the rhythm is the same for the measures, we want to repeat the notes as closely as possible while making sense for the current chord
        # 1. weighted pick of continuing the "direction" of the note movement, i.e., if notes are going up, then continue that trend, and vice-versa
        # 2. if the length of the note is more than a quarter, only play a note from the chord (but still close to the previous note preferably)
        # 3. pick a random note in the scale, somewhere within 2 of the original
        if idx > 1:
            repeated_idx, does_repeat, ratio = self.comparePreviousMeasures(
                idx)
            if does_repeat:
                measure = self.adjustMeasure(repeated_idx, idx, ratio)

        measure_progression = self.determineProgression()

        for j in range(len(measure), len(self.rhythm[idx])):
            measure.append(self.genNote(measure, idx, j, measure_progression))

        return measure

    def genNote(self, measure, measure_idx, idx, progression):
        prev_note = measure[idx-1][0]
        note = prev_note
        scale_idx = self.scale.index(prev_note)

        # Make a list of the possible note_indices we can move to
        note_indices = []
        for note_idx in list(self.melody_info.note_weights.keys()):
            if progression >= 0:
                note_indices.append(note_idx)
            if progression <= 0:
                note_indices.append(-1 * note_idx)

        note_choices = {
            n: self.scale[(scale_idx + n) % len(self.scale)] for n in note_indices}

        r_note = random.uniform(0, 1)
        current_weights = 0
        for key in list(self.melody_info.note_weights.keys()):
            current_weights += self.melody_info.note_weights[key]
            if r_note <= current_weights:
                random_choices = [
                    key, -1 * key] if progression == 0 else [progression * key]
                note = note_choices[random.choice(random_choices)]
                return [note, self.rhythm[measure_idx][idx]]

        return [note, self.rhythm[measure_idx][idx]]

    # ================ #
    # HELPER FUNCTIONS #
    # ================ #

    # Determine a particular measure's progression
    # Return -1, 0, or 1 for down, random, or up, respectively
    def determineProgression(self):
        r = random.uniform(0, 1)
        if r <= self.melody_info.progressions['in-measure']:
            return random.choice([-1, 1])
        return 0

    # "Adjusts" the original_measure parameter to better fit our chord_notes[idx]
    # Begins at starting note, adjusts all others accordingly
    # Returns the adjusted measure in the measure-array format
    def adjustMeasure(self, previous_idx, idx, ratio):
        cut_length = int(len(self.melody[previous_idx])/ratio)
        # reference measure, for easy comparison
        ref_measure = self.melody[previous_idx][:cut_length]
        # working measure, to be changed throughout the adjustments
        working_measure = self.melody[previous_idx][:cut_length]

        # if perfect replication, then return measure as-is, no changes
        r_perfect = random.uniform(0, 1)
        if r_perfect <= self.melody_info.measure_adjustments['perfect']:
            return working_measure

        # if inverted, then invert the direction of the notes, and continue
        r_inverted = random.uniform(0, 1)
        if r_inverted <= self.melody_info.measure_adjustments['inverted']:
            working_measure = [
                [working_measure[-1 * (i+1)][0], working_measure[i][1]] for i in range(len(working_measure))]

        # if chord, then set the starting note to the same chord position as the ref_measure and adjust all other notes correspondingly, and return
        r_chord = random.uniform(0, 1)
        if r_chord <= self.melody_info.measure_adjustments['chord']:
            return self.chordBasedMeasure(previous_idx, idx, working_measure)

        # if slight, then go through and adjust starting note and any >= 1/4th notes to the closest chord note in the trending direction, adjusting the following notes correspondingly
        r_slight = random.uniform(0, 1)
        if r_slight <= self.melody_info.measure_adjustments['slight']:
            return self.slightBasedMeasure(previous_idx, idx, working_measure)

        return working_measure

    # Performs slight adjustments to pull chord_notes to our current chords
    def slightBasedMeasure(self, previous_idx, idx, measure):
        previous_chord_notes = self.chord_notes[previous_idx]
        chord_notes = self.chord_notes[idx]

        fixed_measure = []
        for note in measure:
            # if we see a previous chord's note that's not in our current chord, let's adjust
            # pull that note to the closest chord note we have
            # this guarantees the first note is always in our chord
            if note[0] in previous_chord_notes and note[0] not in chord_notes:
                previous_note_idx = self.scale.index(note[0])
                chord_note_differences = [self.scale.index(
                    elem) - previous_note_idx for elem in chord_notes]
                closest_note_diff = min(chord_note_differences, key=abs)
                closest_note_idx = (previous_note_idx +
                                    closest_note_diff) % len(self.scale)
                closest_note = self.scale[closest_note_idx]
                fixed_measure.append([closest_note, note[1]])
            else:
                fixed_measure.append(note)

        return fixed_measure

    # Adjusts a measure based off the input index and previous index
    # Uses our "chord" method, finding the corresponding chord note
    def chordBasedMeasure(self, previous_idx, idx, measure):
        previous_measure = self.melody[previous_idx]
        previous_starting_note = previous_measure[0][0]
        # find chord note position
        chord_note_idx = self.chord_notes[previous_idx].index(
            previous_starting_note)
        # find position of relative chord notes for current measure
        starting_note = self.chord_notes[idx][chord_note_idx]
        # now find difference between scale positions of these notes
        note_difference = self.scale.index(
            starting_note) - self.scale.index(previous_starting_note)

        fixed_measure = []
        for note in measure:
            previous_note_idx = self.scale.index(note[0])
            new_note_idx = (previous_note_idx +
                            note_difference) % len(self.scale)
            fixed_measure.append([self.scale[new_note_idx], note[1]])

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
        cut_length = int(len(previous_measure)/ratio)

        # if full measure is the same (ratio = 1), lengths should be the same
        # if half measure is the same (ratio = 2), then length >= cut_length
        if len(current_measure) < cut_length:
            return False

        # index won't run over due to previous if statement
        cut_current_measure = current_measure[:cut_length]
        cut_previous_measure = previous_measure[:cut_length]

        return cut_current_measure == cut_previous_measure
