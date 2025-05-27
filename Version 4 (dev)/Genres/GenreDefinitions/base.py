# GenreDefinitions/base.py
from abc import ABC, abstractmethod

class GenreBase(ABC):
    @property
    @classmethod
    @abstractmethod
    def name(cls) -> str:
        ...

    @abstractmethod
    def build(self) -> dict:
        ...
