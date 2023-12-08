import random
import sys
sys.path.append('D:\Documents\Github\musicGenerator\Version 4 (dev)')

# Custom module imports
from Genres.DefineGenre import *


class GenRhythm:

    def __init__(self, length, genre):
        self.length = length
        self.genre = genre
        self.rhythm_info = None
        self.rhythm = []

        # Tracking variables for rhythm repetition
        self.repetitions = {}

    def build(self):
        self.setRhythmValues()
        self.genRhythm()
        return self.rhythm

    # ============== #
    # SET GENRE INFO #
    # ============== #
    def setRhythmValues(self):
        genre_details = DefineGenre(genre=self.genre)
        self.rhythm_info = genre_details.genre_info()["Rhythm"]
        self.repetition = self.rhythm_info.probabilities
        self.setRepetition()

    # ============ #
    # BUILD RHYTHM #
    # ============ #

    def genRhythm(self):
        for i in range(1, self.length+1):
            self.genMeasure(i)
            # chance of skipping generation and repeating the rhythm
            # this applies to the entire measure
            # TODO: breakout generation and compare parts of measures, not just the whole
            # if i > 1 and self.length == 4:
            #     r_same = random.uniform(0, 1)
            #     if (i == 2 and r_same < prob_1_3_same) or (i == 3 and r_same < prob_2_4_same):
            #         self.rhythm.append(self.rhythm[i-2])
            #         continue

            # # random generation section
            # total = 0
            # measure = []
            # while total < 4:
            #     # pick a weighted random note
            #     r1 = random.uniform(0, 1)
            #     new_note = self.all_rhythms[-1]
            #     for i in range(0, len(self.all_rhythm_weights)):
            #         if self.all_rhythm_weights[i] <= r1:
            #             new_note = self.all_rhythms[i]

            #     # only add note size that fits inside the measure
            #     if total + new_note > 4:
            #         new_note = 4 - total
            #     measure.append(new_note)
            #     total += new_note

            #     # some percent chance to replicate the same note, creating runs of the same size
            #     # only if the note is < one beat long
            #     if new_note < 1 and total + new_note <= 4:
            #         r2 = random.uniform(0, 1)
            #         if r2 < 0.5:
            #             measure.append(new_note)
            #             total += new_note

            # self.rhythm.append(measure)

    def genMeasure(self, idx):
        total = 0
        measure = []

        if idx > 1:
            total, measure = self.copyMeasure(idx)

        while total < 4:
            # pick a weighted random note
            r1 = random.uniform(0, 1)
            rhythms, weights = self.rhythm_info.all_rhythms, self.rhythm_info.all_rhythm_weights
            new_note = rhythms[-1]  # need a default value i think
            for i in range(0, len(weights)):
                # current weight is equal to sum of weights so far
                current_weight = sum(weights[:i+1])
                if r1 <= current_weight:
                    new_note = rhythms[i]
                    break
                
            # only add note size that fits inside the measure
            if total + new_note > 4:
                new_note = 4 - total
            measure.append(new_note)
            total += new_note

            # some percent chance to replicate the same note, creating runs of the same size
            # only if the note is < one beat long
            # 1/16th notes should be guaranteed to double up
            if new_note < 1 and total + new_note <= 4:
                r2 = random.uniform(0, 4)
                if r2 <= (1 / new_note) + 1:
                    measure.append(new_note)
                    total += new_note
                    
        self.rhythm.append(measure)

    # ================ #
    # HELPER FUNCTIONS #
    # ================ #
    def copyMeasure(self, idx):        
        # looping over our repetition dictionaries
        for measure_set in self.repetition['full']:
            if idx in measure_set and self.repetition['full'][measure_set]:
                measure = self.rhythm[0] if 1 in measure_set else self.rhythm[1]
                return 4, measure
        
        for measure_set in self.repetition['half']:
            if idx in measure_set and self.repetition['half'][measure_set]:
                rhythm_idx = measure_set[0] - 1
                measure = self.rhythm[rhythm_idx][:int(len(self.rhythm[rhythm_idx])/2)]
                total = sum(measure)
                return total, measure
        
        return 0, []

    def setRepetition(self):
        # loop over our dictionaries
        for measure_size in list(self.repetition.keys()):
            for measure_set in list(self.repetition[measure_size].keys()):
                r = random.uniform(0, 1)
                # r <= probability, so prob of 0 is always false, and 1 is always true
                self.repetition[measure_size][measure_set] = r <= self.rhythm_info.probabilities[measure_size][measure_set]
