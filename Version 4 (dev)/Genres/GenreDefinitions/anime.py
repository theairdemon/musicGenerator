from Genres.RhythmInfo import RhythmInfo
from Genres.MelodyInfo import MelodyInfo
from Genres.StructureInfo import StructureInfo
from Genres.MidiInfo import MidiInfo
from .base import GenreBase

class AnimeGenre(GenreBase):
    name = 'anime'

    def build(self) -> dict:
        return {
            'Rhythm' : self._build_rhythm(),
            'Melody' : self._build_melody(),
            'Structure' : self._build_structure(),
            'MidiInfo' : self._build_midi_info()
        }

    def _build_rhythm(self) -> RhythmInfo:
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
                (2, 4): 0.4,
                (1, 2, 3): 0.8,
                (1, 2, 3, 4): 0.7
            },
        }
        anime_rhythm_info.set_probabilities(probabilities)
        return anime_rhythm_info

    def _build_melody(self) -> MelodyInfo:
        anime_melody_info = MelodyInfo()
        adjustment_probabilities = {
            'perfect': 0.7,
            'inverted': 0.0,
            'chord': 0.6,
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
        rest_weights = [0, 0, 0]
        anime_melody_info.set_melodic_choices(
            adjustment_probabilities, progressions, note_weights, rest_weights)
        return anime_melody_info

    def _build_structure(self) -> StructureInfo:
        melody_instruments = [
            'piano',
            'violin',
            'bells',
            'flute']
        chords_instruments = [
            'strings',
            'woodwinds',
            'piano (quiet)']
        arpeggios_instruments = [
            'woodwinds',
            'piano',
            'bells',
            'Pop Transcendence - Wooden Music Box',
            'trumpet (quiet)',
            'flute',
            'clarinet']
        anime_structure_info = StructureInfo()
        instrument_dict = {
            'melody': melody_instruments,
            'chords1': chords_instruments,
            'chords2': chords_instruments,
            'arpeggios1': arpeggios_instruments,
            'arpeggios2': arpeggios_instruments,
            'arpeggios3': arpeggios_instruments
        }
        tracks_list = ['melody1',
                       'chords1', 'chords2',
                       'arpeggios1', 'arpeggios2', 'arpeggios3']
        anime_structure_info.set_instruments(instrument_dict)
        anime_structure_info.set_tracks(tracks_list)
        return anime_structure_info
    
    def _build_midi_info(self) -> MidiInfo:
        midi_info = MidiInfo()
        midi_info.set_tempo(120)
        midi_info.set_volumes(70, 100, 50)
        return midi_info

