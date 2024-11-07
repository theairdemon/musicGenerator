import random

from Genres.RhythmInfo import RhythmInfo
from Genres.MelodyInfo import MelodyInfo
from Genres.StructureInfo import StructureInfo


class DefineGenre:

    def __init__(self, genre=''):
        self.genre = genre

        # Defining genre strings here
        self.genre_dict = {
            'anime': self.anime_info,
            'classical': self.classical_info,
            'cyberpunk': self.cyberpunk_info,
            'fantasy': self.fantasy_info,
            'lofi': self.lofi_info
        }

        self.return_dict = {'Rhythm': None,
                            'Melody': None,
                            'Structure': StructureInfo()}

        if self.genre not in self.genre_dict.keys():
            self.genre = random.choice(list(self.genre_dict.keys()))

    # Fast retrieval of info
    def get(self, key):
        return self.return_dict[key]

    # Build the genre definition
    def build(self):
        self.genre_dict[self.genre]()

    # ==================== #
    # GENRE INFO FUNCTIONS #
    # ==================== #
    def anime_info(self):
        # Rhythm Definitions
        anime_rhythm_info = RhythmInfo()
        anime_rhythm_info.set_rhythms([0.25, 0.5, 1], [0.15, 0.5, 0.35])
        probabilities = {
            'full': {
                (1, 3): 0,
                (2, 4): 0,
                (1, 2, 3): 0.1
            },
            'half': {
                (1, 3): 0,
                (2, 4): 0,
                (1, 2, 3): 0.8,
                (1, 2, 3, 4): 0.3
            },
        }
        anime_rhythm_info.set_probabilities(probabilities)
        self.return_dict['Rhythm'] = anime_rhythm_info

        # Melody Definitions
        anime_melody_info = MelodyInfo()
        adjustment_probabilities = {
            'perfect': 0.35,
            'inverted': 0.0,
            'chord': 0.5,
            'slight': 0.8
        }
        progressions = {
            'in-measure': 0.4,  # odds of continuing progression throughout a measure
            'inverted': 0.0  # will be implemented later
        }
        note_weights = {
            0: 0.1,
            1: 0.8,
            2: 0.1
        }
        rest_weights = [0, 0.05, 0.2]
        anime_melody_info.set_melodic_choices(
            adjustment_probabilities, progressions, note_weights, rest_weights)
        self.return_dict['Melody'] = anime_melody_info

    def classical_info(self):
        # Rhythm Definitions
        classical_rhythm_info = RhythmInfo()
        classical_rhythm_info.set_rhythms([0.25, 0.5, 1], [0.25, 0.5, 0.25])
        probabilities = {
            'full': {
                (1, 3): 0,
                (2, 4): 0.2,
                (1, 2, 3): 0.4
            },
            'half': {
                (1, 3): 0.5,
                (2, 4): 0,
                (1, 2, 3): 0.9,
                (1, 2, 3, 4): 0.3
            },
        }
        classical_rhythm_info.set_probabilities(probabilities)
        self.return_dict['Rhythm'] = classical_rhythm_info

        # Melody Definitions
        classical_melody_info = MelodyInfo()
        adjustment_probabilities = {
            'perfect': 0.65,
            'inverted': 0.7,
            'chord': 0.5,
            'slight': 0.8
        }
        progressions = {
            'in-measure': 0.3,  # odds of continuing progression throughout a measure
            'inverted': 0.0  # will be implemented later
        }
        note_weights = {
            0: 0.1,
            1: 0.8,
            2: 0.1
        }
        rest_weights = [0.05, 0.05, 0.1]
        classical_melody_info.set_melodic_choices(
            adjustment_probabilities, progressions, note_weights, rest_weights)
        self.return_dict['Melody'] = classical_melody_info

    def cyberpunk_info(self):
        # Rhythm Definitions
        cyberpunk_rhythm_info = RhythmInfo()
        cyberpunk_rhythm_info.set_rhythms([0.5, 1], [0.45, 0.55])
        probabilities = {
            'full': {
                (1, 3): 0,
                (2, 4): 0.5,
                (1, 2, 3): 0
            },
            'half': {
                (1, 3): 0,
                (2, 4): 0.8,
                (1, 2, 3): 0.2,
                (1, 2, 3, 4): 0.6
            },
        }
        cyberpunk_rhythm_info.set_probabilities(probabilities)
        self.return_dict['Rhythm'] = cyberpunk_rhythm_info

        # Melody Definitions
        cyberpunk_melody_info = MelodyInfo()
        adjustment_probabilities = {
            'perfect': 0,
            'inverted': 0.1,
            'chord': 0.8,
            'slight': 0.2
        }
        progressions = {
            'in-measure': 0.5,  # odds of continuing progression throughout a measure
            'inverted': 0.0  # will be implemented later
        }
        note_weights = {
            0: 0.1,
            1: 0.8,
            2: 0.1
        }
        rest_weights = [0, 0, 0.2]
        cyberpunk_melody_info.set_melodic_choices(
            adjustment_probabilities, progressions, note_weights, rest_weights)
        self.return_dict['Melody'] = cyberpunk_melody_info

    def fantasy_info(self):
        print('fantasy')

    def lofi_info(self):
        print('lofi')


if __name__ == '__main__':
    genreDefinition = DefineGenre()
    genreDefinition.genre_info()
