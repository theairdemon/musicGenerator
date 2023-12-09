import random
import sys
sys.path.append('D:\Documents\Github\musicGenerator\Version 4 (dev)')

# Custom module imports
from Genres.DefineGenre import *


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
        genre_details = DefineGenre(self.genre)
        self.melody_info = genre_details.genre_info()["Melody"]
        self.gen_melody()
        return self.melody
    
    # ============ #
    # BUILD MELODY #
    # ============ #
    def gen_melody(self):
        for i in range(0, self.length):
            self.melody.append(self.genMeasure(i))
            # chance of skipping generation and repeating the melody
            # this checks if the random value fits and also if the rhythm is the same
            # if i > 1 and self.rhythm[i] == self.rhythm[i-2] and len(self.chords) == 4:
            #    r_same = random.uniform(0, 1)
            #    if (i == 2 and r_same <= prob_1_3_same) or (i == 3 and r_same <= prob_2_4_same):
            #        self.melody.append(self.melody[i-2])
            #        continue
            starting_note = random.choice(self.chord_notes[i])
            measure = [[starting_note, self.rhythm[i][0]]]
            
            # loop over the rhythm and build notes from it
            # rough outline:
            # 0. if the rhythm is the same for the measures, we want to repeat the notes as closely as possible while making sense for the current chord
            # 1. pick a note
            # 2. if the length of the note is more than a quarter, only play a note from the chord (but still close to the previous note preferably)
            # 3. weighted pick of continuing the "direction" of the note movement, i.e., if notes are going up, then continue that trend, and vice-versa
            for j in range(1, len(self.rhythm[i])):
                prev_note = measure[j-1][0]
                note = prev_note
                scale_i = self.scale.index(prev_note)
                if self.rhythm[i][j] < 2:
                    if scale_i + 1 == len(self.scale):
                        note = random.choice(
                            [self.scale[scale_i - 1], self.scale[scale_i]])
                    elif scale_i - 1 == -1:
                        note = random.choice(
                            [self.scale[scale_i + 1], self.scale[scale_i]])
                    else:
                        note = random.choice([self.scale[scale_i + 1],
                                              self.scale[scale_i - 1],
                                              self.scale[scale_i]])
                else:
                    for k in range(scale_i):
                        note_below = self.scale[max(scale_i - k, 0)]
                        note_above = self.scale[min(
                            scale_i + k, len(self.scale) - 1)]
                        if note_below in self.chord_notes:
                            note = note_below
                        elif note_above in self.chord_notes:
                            note = note_above
                measure.append([note, self.rhythm[i][j]])
            self.melody.append(measure)
    
    def genMeasure(self, idx):
        starting_note = random.choice(self.chord_notes[i])
        measure = [[starting_note, self.rhythm[idx][0]]]
        
        repeated_idx, does_repeat, ratio = self.comparePreviousMeasures(idx)
        if does_repeat:
            measure = self.adjustMeasure(repeated_idx, idx, ratio)

        # loop over the rhythm and build notes from it
        # rough outline:
        # 0. if the rhythm is the same for the measures, we want to repeat the notes as closely as possible while making sense for the current chord
        # 1. weighted pick of continuing the "direction" of the note movement, i.e., if notes are going up, then continue that trend, and vice-versa
        # 2. if the length of the note is more than a quarter, only play a note from the chord (but still close to the previous note preferably)
        # 3. pick a random note in the scale, somewhere within 2 of the original
        for j in range(1, len(self.rhythm[i])):
            prev_note = measure[j-1][0]
            note = prev_note
            scale_i = self.scale.index(prev_note)
            if self.rhythm[i][j] < 2:
                if scale_i + 1 == len(self.scale):
                    note = random.choice(
                        [self.scale[scale_i - 1], self.scale[scale_i]])
                elif scale_i - 1 == -1:
                    note = random.choice(
                        [self.scale[scale_i + 1], self.scale[scale_i]])
                else:
                    note = random.choice([self.scale[scale_i + 1],
                                          self.scale[scale_i - 1],
                                          self.scale[scale_i]])
            else:
                for k in range(scale_i):
                    note_below = self.scale[max(scale_i - k, 0)]
                    note_above = self.scale[min(
                        scale_i + k, len(self.scale) - 1)]
                    if note_below in self.chord_notes:
                        note = note_below
                    elif note_above in self.chord_notes:
                        note = note_above
            measure.append([note, self.rhythm[i][j]])
        return measure
        
    # ================ #
    # HELPER FUNCTIONS #
    # ================ #
    
    # "Adjusts" the original_measure parameter to better fit our chord_notes[idx]
    # Begins at starting note, adjusts all others accordingly
    # Returns the adjusted measure in the measure-array format
    def adjustMeasure(self, previous_idx, idx, ratio):
        cut_length = int(len(self.melody[previous_idx])/ratio)
        # reference measure, for easy comparison
        ref_measure = self.melody[previous_idx][:cut_length]
        # working measure, to be changed throughout the adjustments
        working_measure = self.melody[previous_idx][:cut_length]
        
        # Compare notes, one at a time, with the chords underneath
        # Do this for both the ref and the working measure
        # 
        # if perfect replication, then return measure as-is, no changes
        # if inverted, then invert the direction of the notes, and continue
        # if chord, then set the starting note to the same chord position as the ref_measure and adjust all other notes correspondingly, and return
        # if slight, then go through and adjust starting note and any >= 1/4th notes to the closest chord note in the trending direction, adjusting the following notes correspondingly
        
        
        return working_measure
    
    # Compares a given index against all previous measures of rhythm
    # Return value: integer, boolean, integer = index of found measure, "True" if either are the same, and the ratio for the cut length
    def comparePreviousMeasures(self, idx):
        for i in range(0, idx):
            if self.compareOneMeasure(i, idx, 1):
                return i, True, 1
            elif self.compareOneMeasure(i, idx, 2):
                return i, True, 2
    
    def compareOneMeasure(self, previous_idx, idx, ratio):
        current_measure = self.rhythm[i]
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