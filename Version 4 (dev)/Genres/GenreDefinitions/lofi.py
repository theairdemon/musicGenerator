from Genres.RhythmInfo import RhythmInfo
from Genres.MelodyInfo import MelodyInfo
from Genres.StructureInfo import StructureInfo
from Genres.MidiInfo import MidiInfo
from .base import GenreBase

class LofiGenre(GenreBase):
    name = 'lofi'

    def build(self) -> dict:
        return {
            'Rhythm' : self._build_rhythm(),
            'Melody' : self._build_melody(),
            'Structure': self._build_structure(),
            'MidiInfo' : self._build_midi_info()
        }

    def _build_rhythm(self) -> RhythmInfo:
        lofi_rhythm_info = RhythmInfo()
        lofi_rhythm_info.set_rhythms([0.5, 1], [0.3, 0.7])
        probabilities = {
            'full': {
                (1, 3): 0.4,
                (2, 4): 0.5,
                (1, 2, 3): 0.9
            },
            'half': {
                (1, 3): 0.4,
                (2, 4): 0.8,
                (1, 2, 3): 0.9,
                (1, 2, 3, 4): 0.8
            },
        }
        lofi_rhythm_info.set_probabilities(probabilities)
        return lofi_rhythm_info

    def _build_melody(self) -> MelodyInfo:
        lofi_melody_info = MelodyInfo()
        adjustment_probabilities = {
            'perfect': 0.8,
            'inverted': 0.1,
            'chord': 0.4,
            'slight': 0.3
        }
        progressions = {
            'in-measure': 0.3,  # odds of continuing progression throughout a measure
            'inverted': 0.0  # will be implemented later
        }
        note_weights = {
            0: 0.15,
            1: 0.6,
            2: 0.25
        }
        rest_weights = [0, 0, 0]
        lofi_melody_info.set_melodic_choices(
            adjustment_probabilities, progressions, note_weights, rest_weights)
        return lofi_melody_info

    def _build_structure(self) -> StructureInfo:
        lofi_structure_info = StructureInfo()
        melody_instruments = [
            'piano',
            'violin',
            'cellos',
            'Pop Transcendence - Deep Pulses',
            'Pop Transcendence - Liquid',
            'Pop Transcendence - Quick Misty Pad',
            'Pop Transcendence - Sweet Echoes',
            'Pop Transcendence - Strings & Sines',
            'Dystopian Machine - Silicon City']
        chords_instruments = [
            'piano',
            'strings',
            'woodwinds',
            'Pop Transcendence - Im Nostalgic',
            'Pop Transcendence - Ether',
            'Dystopian Machine - Life Inside',
            'JSPA - CS80 Pad',
            'JSPA - CS80 Strings']
        arpeggios_instruments = [
            'piano',
            'strings',
            'classical guitar',
            'woodwinds',
            'Pop Transcendence - Deep Pulses',
            'Pop Transcendence - Noisy Sine',
            'Pop Transcendence - Wood Music Box',
            'Pop Transcendence - Penultimate Fantasy',
            'Dystopian Machine - Punk Robot',
            'JSPA - Gentle Synth Brass',
            'JSPA - CS80 Strings']
        instrument_dict = {
            'melody1': melody_instruments,
            'melody2': melody_instruments,
            'chords1': chords_instruments,
            'chords2': chords_instruments,
            'arpeggios1': arpeggios_instruments,
            'arpeggios2': arpeggios_instruments
        }
        tracks_list = ['melody1', 'melody2',
                       'chords1', 'chords2',
                       'arpeggios1', 'arpeggios2']
        lofi_structure_info.set_instruments(instrument_dict)
        lofi_structure_info.set_tracks(tracks_list)
        return lofi_structure_info
    
    def _build_midi_info(self) -> MidiInfo:
        midi_info = MidiInfo()
        midi_info.set_tempo(80)
        midi_info.set_volumes(85, 70, 75)
        return midi_info
