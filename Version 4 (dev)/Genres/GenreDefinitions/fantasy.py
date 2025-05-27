from Genres.RhythmInfo import RhythmInfo
from Genres.MelodyInfo import MelodyInfo
from Genres.StructureInfo import StructureInfo
from Genres.MidiInfo import MidiInfo
from .base import GenreBase

class FantasyGenre(GenreBase):
    name = 'fantasy'

    def build(self) -> dict:
        return {
            'Rhythm' : self._build_rhythm(),
            'Melody' : self._build_melody(),
            'Structure': self._build_structure(),
            'MidiInfo' : self._build_midi_info()
        }

    def _build_rhythm(self) -> RhythmInfo:
        fantasy_rhythm_info = RhythmInfo()
        fantasy_rhythm_info.set_rhythms([0.25, 0.5, 1], [0.2, 0.4, 0.4])
        probabilities = {
            'full': {
                (1, 3): 0.5,
                (2, 4): 0.5,
                (1, 2, 3): 0.8
            },
            'half': {
                (1, 3): 0.7,
                (2, 4): 0.8,
                (1, 2, 3): 0.7,
                (1, 2, 3, 4): 0.6
            },
        }
        fantasy_rhythm_info.set_probabilities(probabilities)
        return fantasy_rhythm_info

    def _build_melody(self) -> MelodyInfo:
        fantasy_melody_info = MelodyInfo()
        adjustment_probabilities = {
            'perfect': 0.4,
            'inverted': 0.1,
            'chord': 0.4,
            'slight': 0.6
        }
        progressions = {
            'in-measure': 0.4,  # odds of continuing progression throughout a measure
            'inverted': 0.0  # will be implemented later
        }
        note_weights = {
            0: 0.1,
            1: 0.7,
            2: 0.2
        }
        rest_weights = [0, 0, 0]
        fantasy_melody_info.set_melodic_choices(
            adjustment_probabilities, progressions, note_weights, rest_weights)
        return fantasy_melody_info

    def _build_structure(self) -> StructureInfo:
        fantasy_structure_info = StructureInfo()
        melody_instruments = ['piano', 'violin', 'flute', 'trumpet', 'bells']
        chords_instruments = ['piano', 'cellos',
                              'strings', 'woodwinds', 'brass']
        arpeggios_instruments = ['piano', 'cellos', 'violas',
                                 'strings', 'classical guitar', 'woodwinds', 'brass']
        instrument_dict = {
            'melody': melody_instruments,
            'chords1': chords_instruments,
            'chords2': chords_instruments,
            'arpeggios': arpeggios_instruments
        }
        tracks_list = ['melody1', 'chords1', 'chords2', 'arpeggios']
        fantasy_structure_info.set_instruments(instrument_dict)
        fantasy_structure_info.set_tracks(tracks_list)
        return fantasy_structure_info
    
    def _build_midi_info(self) -> MidiInfo:
        midi_info = MidiInfo()
        midi_info.set_tempo(120)
        midi_info.set_volumes(80, 100, 80)
        return midi_info
