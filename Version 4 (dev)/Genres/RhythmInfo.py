class RhythmInfo:

    def __init__(self):
        # all possible rhythms and the weighted probability of each
        self.all_rhythms = []
        self.all_rhythm_weights = []

        # probability that our rhythm repeats for these sets of measures:
        # 1/3, 2/4, 1/2/3
        self.full_measure_1_3_same = 0
        self.full_measure_2_4_same = 0
        self.full_measure_1_2_3_same = 0

        # probability that half the measure repeats for these sets of measures:
        # 1/3, 2/4, 1/2/3, 1/2/3/4
        self.half_measure_1_3_same = 0
        self.half_measure_2_4_same = 0
        self.half_measure_1_2_3_same = 0
        self.half_measure_1_2_3_4_same = 0

    def set_rhythms(self, rhythms, rhythm_weights):
        self.all_rhythms = rhythms
        self.all_rhythm_weights = rhythm_weights

    def set_full_measure_same(self, prob_1_3, prob_2_4, prob_1_2_3):
        self.full_measure_1_3_same = prob_1_3
        self.full_measure_2_4_same = prob_2_4
        self.full_measure_1_2_3_same = prob_1_2_3

    def set_half_measure_same(self, prob_1_3, prob_2_4, prob_1_2_3, prob_1_2_3_4):
        self.half_measure_1_3_same = prob_1_3
        self.half_measure_2_4_same = prob_2_4
        self.half_measure_1_2_3_same = prob_1_2_3
        self.half_measure_1_2_3_4_same = prob_1_2_3_4
