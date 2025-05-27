from Genres.RhythmInfo import RhythmInfo
from Genres.MelodyInfo import MelodyInfo
from Genres.StructureInfo import StructureInfo
from Genres.MidiInfo import MidiInfo
from .base import GenreBase

class CyberpunkGenre(GenreBase):
    name = 'cyberpunk'

    def build(self) -> dict:
        return {
            'Rhythm' : self._build_rhythm(),
            'Melody' : self._build_melody(),
            'Structure' : self._build_structure(),
            'MidiInfo' : self._build_midi_info()
        }

    def _build_rhythm(self) -> RhythmInfo:
        cyberpunk_rhythm_info = RhythmInfo()
        cyberpunk_rhythm_info.set_rhythms([0.5, 1], [0.45, 0.55])
        probabilities = {
            'full': {
                (1, 3): 0,
                (2, 4): 0.5,
                (1, 2, 3): 0
            },
            'half': {
                (1, 3): 0,
                (2, 4): 0.8,
                (1, 2, 3): 0.2,
                (1, 2, 3, 4): 0.6
            },
        }
        cyberpunk_rhythm_info.set_probabilities(probabilities)
        return cyberpunk_rhythm_info

    def _build_melody(self) -> MelodyInfo:
        cyberpunk_melody_info = MelodyInfo()
        adjustment_probabilities = {
            'perfect': 0,
            'inverted': 0.1,
            'chord': 0.8,
            'slight': 0.2
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
        cyberpunk_melody_info.set_melodic_choices(
            adjustment_probabilities, progressions, note_weights, rest_weights)
        return cyberpunk_melody_info

    def _build_structure(self) -> StructureInfo:
        cyberpunk_structure_info = StructureInfo()
        # TODO: work through sound banks
        # Completed:
        # Next Up: Pop Transcendence, Dystopian Machine, JSPA, Urban Clouds
        melody_instruments = [
            'piano',
            'cellos',
            'Dystopian Machine - Generator',
            'Dystopian Machine - Maniac']
        chords_instruments = [
            'Pop Transcendence - Arpluck',
            'Pop Transcendence - Heartbeat',
            'Pop Transcendence - Okay to Cry',
            'Pop Transcendence - Groovy Flutes',
            'Dystopian Machine - Lamenting Circuits',
            'Dystopian Machine - Loading Process',
            'Dystopian Machine - Divine Chaos',
            'Dystopian Machine - Acid Wave',
            'Dystopian Machine - Cybernetic',
            'Dystopian Machine - Circuit Crush',
            'Dystopian Machine - Steel City Nights',
            'Dystopian Machine - Cyber Assault',
            'JSPA - Industrial Seq',
            'Urban Clouds - Cold Summer',
            'Urban Clouds - Slow Siren']
        arpeggios_instruments = [
            'Pop Transcendence - Deep Pulses',
            'Pop Transcendence - Running From the 80s',
            'Pop Transcendence - Super Cheese',
            'Dystopian Machine - Black Box',
            'Dystopian Machine - Blackout Night']
        instrument_dict = {
            'melody1': melody_instruments,
            'melody2': melody_instruments,
            'chords1': chords_instruments,
            'chords2': chords_instruments,
            'chords3': chords_instruments,
            'arpeggios1': arpeggios_instruments,
            'arpeggios2': arpeggios_instruments,
        }
        tracks_list = ['melody1', 'melody2',
                       'chords1', 'chords2', 'chords3',
                       'arpeggios1', 'arpeggios2']
        cyberpunk_structure_info.set_instruments(instrument_dict)
        cyberpunk_structure_info.set_tracks(tracks_list)
        return cyberpunk_structure_info
    
    def _build_midi_info(self) -> MidiInfo:
        midi_info = MidiInfo()
        midi_info.set_tempo(90)
        midi_info.set_volumes(80, 60, 70)
        return midi_info
