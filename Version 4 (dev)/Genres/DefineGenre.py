import random

from Genres.RhythmInfo import RhythmInfo
from Genres.MelodyInfo import MelodyInfo
from Genres.StructureInfo import StructureInfo


class DefineGenre:

    def __init__(self, genre=''):
        self.genre = genre

        # Defining genre strings here
        self.genre_dict = {
            'anime': self.anime_info,
            'classical': self.classical_info,
            'cyberpunk': self.cyberpunk_info,
            'fantasy': self.fantasy_info,
            'lofi': self.lofi_info
        }

        self.return_dict = {'Rhythm': None,
                            'Melody': None,
                            'Structure': None}

        if self.genre not in self.genre_dict.keys():
            self.genre = random.choice(list(self.genre_dict.keys()))

    # Fast retrieval of info
    def get(self, key):
        return self.return_dict[key]

    # Build the genre definition
    def build(self):
        self.genre_dict[self.genre]()

    # ==================== #
    # GENRE INFO FUNCTIONS #
    # ==================== #
    def anime_info(self):
        # Rhythm Definitions
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
        self.return_dict['Rhythm'] = anime_rhythm_info

        # Melody Definitions
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
        self.return_dict['Melody'] = anime_melody_info

        # Structural Definitions
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
        self.return_dict['Structure'] = anime_structure_info

    def classical_info(self):
        # Rhythm Definitions
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
        self.return_dict['Rhythm'] = classical_rhythm_info

        # Melody Definitions
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
        self.return_dict['Melody'] = classical_melody_info

        # Structural Definitions
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
        self.return_dict['Structure'] = classical_structure_info

    def cyberpunk_info(self):
        # Rhythm Definitions
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
        self.return_dict['Rhythm'] = cyberpunk_rhythm_info

        # Melody Definitions
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
        self.return_dict['Melody'] = cyberpunk_melody_info

        # Structural Definitions
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
        self.return_dict['Structure'] = cyberpunk_structure_info

    def fantasy_info(self):
        # Rhythm Definitions
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
        self.return_dict['Rhythm'] = fantasy_rhythm_info

        # Melody Definitions
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
        self.return_dict['Melody'] = fantasy_melody_info

        # Structural Definitions
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
        self.return_dict['Structure'] = fantasy_structure_info

    def lofi_info(self):
        # Rhythm Definitions
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
        self.return_dict['Rhythm'] = lofi_rhythm_info

        # Melody Definitions
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
        self.return_dict['Melody'] = lofi_melody_info

        # Structural Definitions
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
        self.return_dict['Structure'] = lofi_structure_info


if __name__ == '__main__':
    genreDefinition = DefineGenre()
    genreDefinition.genre_info()
