import random


class DefineGenre:

    def __init__(self, genre="random"):
        self.genre = genre

        self.potential_genres = [
            "anime",
            "classical",
            "fantasy",
            "cyberpunk"
        ]

        if self.genre == "random":
            self.genre = random.choice(self.potential_genres)

    def genre_info(self):
        match self.genre: # type: ignore 
            case "anime":
                print("anime")
            case default:
                print("Error")


if __name__ == "__main__":
    genreDefinition = DefineGenre("anime")
    genreDefinition.genre_info()
