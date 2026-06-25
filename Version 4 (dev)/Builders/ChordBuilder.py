from Builders.ScaleBuilder import ScaleBuilder


class ChordBuilder:
    def __init__(self, root, style):
        self.root = root
        self.style = style

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

        self.scaleBuilder = ScaleBuilder(self.root, self.style)
        self.scale = self.scaleBuilder.build_scale()

    def build_chord(self, chord):
        match chord:
            case "I":  # 0, 4, 7
                return self._build_chord(0, "major")
            case "i":  # 0, 3, 7
                return self._build_chord(0, "minor")
            case "II":  # 2, 6, 9
                return self._build_chord(1, "major")
            case "ii":  # 2, 5, 9
                return self._build_chord(1, "minor")
            case "III":  # 4, 8, 11
                return self._build_chord(2, "major")
            case "iii":  # 4, 7, 11
                return self._build_chord(2, "minor")
            case "IV":  # 5, 9, 0
                return self._build_chord(3, "major")
            case "iv":  # 5, 8, 0
                return self._build_chord(3, "minor")
            case "V":  # 7, 11, 2
                return self._build_chord(4, "major")
            case "v":  # 7, 10, 2
                return self._build_chord(4, "minor")
            case "VI":  # 9, 1, 4
                return self._build_chord(5, "major")
            case "vi":  # 9, 0, 4
                return self._build_chord(5, "minor")
            case "VII":  # 11, 3, 6
                return self._build_chord(6, "major")
            case "vii":  # 11, 2, 6
                return self._build_chord(6, "minor")

    def _build_chord(self, scale_idx, scale_style):
        chord_root = self.scale[scale_idx]
        chord_scale = self.scaleBuilder.build_scale(chord_root, scale_style)

        return [chord_scale[0], chord_scale[2], chord_scale[4]]
