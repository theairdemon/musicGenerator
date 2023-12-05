import random

from ..Genres.RhythmInfo import RhythmInfo


class DefineGenre:

    def __init__(self, genre="random"):
        self.genre = genre

        # Defining genre strings here
        self.potential_genres = [
            "anime",
            "classical",
            "fantasy",
            "cyberpunk"
        ]

        self.return_dict = {"Rhythm": None, "Melody": None}

        if self.genre == "random":
            self.genre = random.choice(self.potential_genres)

    def genre_info(self):
        if self.genre == "anime":
            self.anime_info()
        elif self.genre == "classical":
            self.classical_info()
        elif self.genre == "fantasy":
            self.fantasy_info()
        elif self.genre == "cyberpunk":
            self.cyberpunk_info()
        else:
            print("Error, genre undefined")
        return self.return_dict

    # GENRE INFO FUNCTIONS
    # Return type: Dictionary, structured as follows
    # {
    #   "Rhythm": RhythmInfo
    #   "Melody": MelodyInfo
    # }

    def anime_info(self):
        anime_rhythm_info = RhythmInfo()
        anime_rhythm_info.set_rhythms([0.25, 0.5, 1], [0.1, 0.45, 0.45])
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

    def fantasy_info(self):
        print("fantasy")

    def cyberpunk_info(self):
        print("cyberpunk")


if __name__ == "__main__":
    genreDefinition = DefineGenre()
    genreDefinition.genre_info()
