import random

from Genres.RhythmInfo import *


class DefineGenre:

    def __init__(self, genre=""):
        self.genre = genre

        # Defining genre strings here
        self.genre_dict = {
            "anime": self.anime_info,
            "classical": self.classical_info,
            "cyberpunk": self.cyberpunk_info,
            "fantasy": self.fantasy_info,
            "lofi": self.lofi_info
        }

        self.return_dict = {"Rhythm": None, "Melody": None}

        if self.genre not in self.genre_dict.keys():
            self.genre = random.choice(self.potential_genres)

    def genre_info(self):
        self.genre_dict[self.genre]()
        return self.return_dict

    # GENRE INFO FUNCTIONS
    # Return type: Dictionary, structured as follows
    # {
    #   "Rhythm": RhythmInfo
    #   "Melody": MelodyInfo
    # }

    def anime_info(self):
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

        self.return_dict["Rhythm"] = anime_rhythm_info

    def classical_info(self):
        print("classical")

    def cyberpunk_info(self):
        print("cyberpunk")

    def fantasy_info(self):
        print("fantasy")
    
    def lofi_info(self):
        print("lofi")


if __name__ == "__main__":
    genreDefinition = DefineGenre()
    genreDefinition.genre_info()
