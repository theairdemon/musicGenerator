class ChordBuilder:
    def __init__(self, root):
        self.root = root

        starting_all_notes = [
            "C",  # 0
            "C#",  # 1
            "D",  # 2
            "D#",  # 3
            "E",  # 4
            "F",  # 5
            "F#",  # 6
            "G",  # 7
            "G#",  # 8
            "A",  # 9
            "A#",  # 10
            "B",  # 11
        ]

        root_index = starting_all_notes.index(root)
        self.all_notes = (
            starting_all_notes[root_index:] + starting_all_notes[:root_index]
        )

    def build_chord(self, chord):
        match chord:
            case "I":  # 0, 4, 7
                return [self.all_notes[0], self.all_notes[4], self.all_notes[7]]

            case "i":  # 0, 3, 7
                return [self.all_notes[0], self.all_notes[3], self.all_notes[7]]

            case "II":  # 2, 6, 9
                return [self.all_notes[2], self.all_notes[6], self.all_notes[9]]

            case "ii":  # 2, 5, 9
                return [self.all_notes[2], self.all_notes[5], self.all_notes[9]]

            case "III":  # 4, 8, 11
                return [self.all_notes[4], self.all_notes[8], self.all_notes[11]]

            case "iii":  # 4, 7, 11
                return [self.all_notes[4], self.all_notes[7], self.all_notes[11]]

            case "IV":  # 5, 9, 0
                return [self.all_notes[5], self.all_notes[9], self.all_notes[0]]

            case "iv":  # 5, 8, 0
                return [self.all_notes[5], self.all_notes[8], self.all_notes[0]]

            case "V":  # 7, 11, 2
                return [self.all_notes[7], self.all_notes[11], self.all_notes[2]]

            case "v":  # 7, 10, 2
                return [self.all_notes[7], self.all_notes[10], self.all_notes[2]]

            case "VI":  # 9, 1, 4
                return [self.all_notes[9], self.all_notes[1], self.all_notes[4]]

            case "vi":  # 9, 0, 4
                return [self.all_notes[9], self.all_notes[0], self.all_notes[4]]

            case "VII":  # 11, 3, 6
                return [self.all_notes[11], self.all_notes[3], self.all_notes[6]]

            case "vii":  # 11, 2, 6
                return [self.all_notes[11], self.all_notes[2], self.all_notes[6]]
