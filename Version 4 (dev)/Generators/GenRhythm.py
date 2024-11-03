from Genres.DefineGenre import *
import random
import sys
sys.path.append('D:\Documents\Github\musicGenerator\Version 4 (dev)')

# Custom module imports


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
        # first check if we're repeating the full measure
        for measure_set in self.repetition['full']:
            if idx in measure_set[1:] and self.repetition['full'][measure_set]:
                # get index of the measure to copy from
                rhythm_idx = measure_set[0] - 1
                measure = self.rhythm[rhythm_idx]
                return 4, measure

        # next, check if we want half of our measures repeated
        for measure_set in self.repetition['half']:
            if idx in measure_set[1:] and self.repetition['half'][measure_set]:
                rhythm_idx = measure_set[0] - 1
                measure = self.rhythm[rhythm_idx][:int(
                    len(self.rhythm[rhythm_idx])/2)]
                total = sum(measure)
                return total, measure

        # if there's no repetition, then we just return 0 and an empty array
        return 0, []

    def setRepetition(self):
        # loop over our dictionaries
        for measure_size in list(self.repetition.keys()):
            for measure_set in list(self.repetition[measure_size].keys()):
                r = random.uniform(0, 1)
                # r <= probability, so prob of 0 is always false, and 1 is always true
                self.repetition[measure_size][measure_set] = r <= self.rhythm_info.probabilities[measure_size][measure_set]
