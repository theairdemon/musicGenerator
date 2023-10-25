import random

from Genres.RhythmInfo import RhythmInfo

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
        match self.genre:  # type: ignore
            case "anime":
                self.anime_info()
            case "classical":
                self.classical_info()
            case "fantasy":
                self.fantasy_info()
            case "cyberpunk":
                self.cyberpunk_info()
            case default:
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
        anime_rhythm_info.set_full_measure_same(0, 0, 0.1)
        anime_rhythm_info.set_half_measure_same(0, 0, 0.8, 0.3)
        
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
