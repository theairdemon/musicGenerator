class StructureInfo:
    def __init__(self):
        # Default verse order for songs
        self.order_list = ['verse1', 'verse1',
                           'chorus', 'chorus',
                           'verse2', 'verse2',
                           'chorus', 'chorus',
                           'bridge',
                           'chorus', 'chorus', "finalChorus"]

        # Default dictionary of instruments
        self.instruments = {
            'melody': ['any'],
            'chords': ['any'],
            'arpeggios': ['any']
        }

        # Default number of tracks per song part
        self.tracks = ['melody', 'chords', 'arpeggios']

    def setOrderList(self, new_order_list):
        self.order_list = new_order_list

    def getOrderList(self):
        return self.order_list

    def set_instruments(self, instrument_dict):
        self.instruments = instrument_dict

    def get_instruments(self):
        return self.instruments

    def set_tracks(self, tracks_list):
        self.tracks = tracks_list

    def get_tracks(self):
        return self.tracks
