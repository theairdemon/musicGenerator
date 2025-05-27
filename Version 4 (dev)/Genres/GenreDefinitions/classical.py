from Genres.RhythmInfo import RhythmInfo
from Genres.MelodyInfo import MelodyInfo
from Genres.StructureInfo import StructureInfo
from Genres.MidiInfo import MidiInfo
from .base import GenreBase

class ClassicalGenre(GenreBase):
    name = 'classical'

    def build(self) -> dict:
        return {
            'Rhythm' : self._build_rhythm(),
            'Melody' : self._build_melody(),
            'Structure' : self._build_structure(),
            'MidiInfo' : self._build_midi_info()
        }

    def _build_rhythm(self) -> RhythmInfo:
        classical_rhythm_info = RhythmInfo()
        classical_rhythm_info.set_rhythms([0.25, 0.5, 1], [0.25, 0.5, 0.25])
        probabilities = {
            'full': {
                (1, 3): 0,
                (2, 4): 0.2,
                (1, 2, 3): 0.5
            },
            'half': {
                (1, 3): 0.5,
                (2, 4): 0.4,
                (1, 2, 3): 0.7,
                (1, 2, 3, 4): 0.3
            },
        }
        classical_rhythm_info.set_probabilities(probabilities)
        return classical_rhythm_info

    def _build_melody(self) -> MelodyInfo:
        classical_melody_info = MelodyInfo()
        adjustment_probabilities = {
            'perfect': 0.65,
            'inverted': 0.7,
            'chord': 0.5,
            'slight': 0.8
        }
        progressions = {
            'in-measure': 0.0,  # odds of continuing progression throughout a measure
            'inverted': 0.0  # will be implemented later
        }
        note_weights = {
            0: 0.1,
            1: 0.8,
            2: 0.1
        }
        rest_weights = [0, 0, 0]
        classical_melody_info.set_melodic_choices(
            adjustment_probabilities, progressions, note_weights, rest_weights)
        return classical_melody_info

    def _build_structure(self) -> StructureInfo:
        melody_instruments = ['piano', 'violin', 'flute']
        chords_instruments = ['piano', 'cellos', 'strings', 'woodwinds']
        arpeggios_instruments = ['cellos', 'violas',
                                 'strings', 'classical guitar', 'woodwinds']
        classical_structure_info = StructureInfo()
        instrument_dict = {
            'melody': melody_instruments,
            'chords': chords_instruments,
            'arpeggios': arpeggios_instruments
        }
        classical_structure_info.set_instruments(instrument_dict)
        return classical_structure_info
    
    def _build_midi_info(self) -> MidiInfo:
        midi_info = MidiInfo()
        midi_info.set_tempo(110)
        midi_info.set_volumes(50, 100, 40)
        return midi_info
