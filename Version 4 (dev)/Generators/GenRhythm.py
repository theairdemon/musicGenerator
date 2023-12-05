import random

from ..Genres.DefineGenres import *


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

    # ============== #
    # SET GENRE INFO #
    # ============== #
    def setRhythmValues(self):
        genre_details = DefineGenre(self.genre)
        self.rhythm_info = genre_details.genre_info()["Rhythm"]
        self.repetition = self.rhythm_info.probabilities
        self.setRepetition()

    # ============ #
    # BUILD RHYTHM #
    # ============ #

    def genRhythm(self):
        for i in range(self.length):
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

        if idx != 1:
            total, measure = self.copyMeasure(idx)

        while total < 4:
            # pick a weighted random note
            r1 = random.uniform(0, 1)
            rhythms, weights = self.rhythm_info.all_rhythms, self.rhythm_info.all_rhythm_weights
            new_note = rhythms[-1]  # need a default value i think
            for i in range(0, len(weights)):
                if weights[i] <= r1:
                    new_note = rhythms[i]

            # only add note size that fits inside the measure
            if total + new_note > 4:
                new_note = 4 - total
            measure.append(new_note)
            total += new_note

            # some percent chance to replicate the same note, creating runs of the same size
            # only if the note is < one beat long
            if new_note < 1 and total + new_note <= 4:
                r2 = random.uniform(0, 1)
                if r2 < 0.5:
                    measure.append(new_note)
                    total += new_note
        self.rhythm.append(measure)

    # ================ #
    # HELPER FUNCTIONS #
    # ================ #
    def copyMeasure(self, idx):
        # first, check if our measures are gonna fully be the same
        # if so, return full total and the corresponding measure
        if idx == 2 and self.full_1_2_3_same:
            return 4, self.rhythm[0]
        elif idx == 3 and (self.full_1_3_same or self.full_1_2_3_same):
            return 4, self.rhythm[0]
        elif idx == 4 and self.full_2_4_same:
            return 4, self.rhythm[1]

        # if not the same, check if half is gonna be the same
        # chop that up and set it here as well, along with the correct total
        if idx == 2 and self.half_1_2_3_same:
            return sum(self.rhythm[0][:int(len(self.rhythm[0])/2)]), self.rhythm[0][:int(len(self.rhythm[0])/2)]
        elif idx == 3 and (self.half_1_3_same or self.half_1_2_3_same):
            return sum(self.rhythm[0][:int(len(self.rhythm[0])/2)]), self.rhythm[0][:int(len(self.rhythm[0])/2)]
        elif idx == 4 and (self.half_2_4_same or self.half_1_2_3_4_same):
            return sum(self.rhythm[1][:int(len(self.rhythm[1])/2)]), self.rhythm[1][:int(len(self.rhythm[1])/2)]

    def setRepetition(self):
        # loop over our dictionaries
        for measure_size in list(self.probabilities.keys()):
            for measure_set in list(self.probabilities[measure_set].keys()):
                r = random.uniform(0, 1)
                self.probabilities[measure_size][measure_set] = self.rhythm_info.probabilities[measure_size][measure_set] <= r
