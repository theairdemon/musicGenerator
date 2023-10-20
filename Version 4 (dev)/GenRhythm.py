import random


class GenRhythm:

    def __init__(self, length):
        self.length = length
        self.all_rhythms = [0.25, 0.5, 1, 2]
        self.all_rhythm_weights = [0.1, 0.4, 0.95, 1.0]

    def build(self):
        self.gen_rhythm()

    # ============ #
    # BUILD RHYTHM #
    # ============ #
    def gen_rhythm(self):
        prob_1_3_same, prob_2_4_same = self.prob_same()

        for i in range(self.length):
            # chance of skipping generation and repeating the rhythm
            # this applies to the entire measure
            # TODO: breakout generation and compare parts of measures, not just the whole
            if i > 1 and self.length == 4:
                r_same = random.uniform(0, 1)
                if (i == 2 and r_same < prob_1_3_same) or (i == 3 and r_same < prob_2_4_same):
                    self.rhythm.append(self.rhythm[i-2])
                    continue

            # random generation section
            total = 0
            measure = []
            while total < 4:
                # pick a weighted random note
                r1 = random.uniform(0, 1)
                new_note = self.all_rhythms[-1]
                for i in range(0, len(self.all_rhythm_weights)):
                    if self.all_rhythm_weights[i] <= r1:
                        new_note = self.all_rhythms[i]

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
    def prob_same(self):
        # probability of measures 1/3 and 2/4 being identical in a 4 bar series
        # the bridge is most likely gonna be similar for measures 1 and 3
        if self.verse_type == "bridge":
            prob_1_3_same = 0.6
            prob_2_4_same = 0.0
        # the chorus should feel a bit repetitive, but not overly so
        # we usually want each breath to end the same
        elif self.verse_type == "chorus":
            prob_1_3_same = 0.1
            prob_2_4_same = 0.9
        # we want some continuity between verses, so some repetition is ok
        else:
            prob_1_3_same = 0.3
            prob_2_4_same = 0.0
        return prob_1_3_same, prob_2_4_same
