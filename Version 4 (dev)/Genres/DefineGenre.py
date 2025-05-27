import random

from Genres.GenreDefinitions.anime import AnimeGenre
from Genres.GenreDefinitions.classical import ClassicalGenre
from Genres.GenreDefinitions.cyberpunk import CyberpunkGenre
from Genres.GenreDefinitions.fantasy import FantasyGenre
from Genres.GenreDefinitions.lofi import LofiGenre

GENRE_MAP = {
    AnimeGenre.name : AnimeGenre,
    ClassicalGenre.name : ClassicalGenre,
    CyberpunkGenre.name : CyberpunkGenre,
    FantasyGenre.name : FantasyGenre,
    LofiGenre.name : LofiGenre,
}

class DefineGenre:
    def __init__(self, genre=''):
        choices = list(GENRE_MAP.keys())
        self.genre = genre if genre in GENRE_MAP else random.choice(choices)
        self.builder = GENRE_MAP[self.genre]()

    # Fast retrieval of info
    def get(self, key):
        return self.build()[key]

    # Build the genre definition
    def build(self):
        return self.builder.build()
