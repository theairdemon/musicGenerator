import random


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

        if self.genre == "random":
            self.genre = random.choice(self.potential_genres)

    def genre_info(self):
        match self.genre:  # type: ignore
            case "anime":
                self.anime_info()
            case default:
                print("Error")
    
    def anime_info(self):
        print("anime")




if __name__ == "__main__":
    genreDefinition = DefineGenre("anime")
    genreDefinition.genre_info()
