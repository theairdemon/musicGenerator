class MidiInfo:

    def __init__(self):
        # Default tempo
        self.tempo = 120

        # Default volumes per-track
        self.volumes = {'chords' : 60,
            'melody': 100,
            'arp': 40
        }
    
    def set_tempo(self, new_tempo) -> None:
        self.tempo = new_tempo
    
    def set_volumes(self, chords_volume = 60, melody_volume = 100, arp_volume = 40) -> None:
        self.volumes = {'chords' : chords_volume,
            'melody': melody_volume,
            'arp': arp_volume
        }