class RhythmInfo:

    def __init__(self):
        # all possible rhythms and the weighted probability of each
        self.all_rhythms = []
        self.all_rhythm_weights = []

        # probability that our rhythm repeats for these sets of measures:
        # 1/3, 2/4, 1/2/3
        self.probabilities = {
            'full': {
                (1, 3): 0,
                (2, 4): 0,
                (1, 2, 3): 0
            },
            'half': {
                (1, 3): 0,
                (2, 4): 0,
                (1, 2, 3): 0,
                (1, 2, 3, 4): 0
            },
        }

    def set_rhythms(self, rhythms, rhythm_weights):
        self.all_rhythms = rhythms
        self.all_rhythm_weights = rhythm_weights

    def set_probabilities(self, new_probabilities):
        self.probabilities = new_probabilities
