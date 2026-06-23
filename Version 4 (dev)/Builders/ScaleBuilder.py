class ScaleBuilder:
    def __init__(self, key, style):
        self.key = key
        self.style = style

        self.all_notes = [
            "C",
            "C#",
            "D",
            "D#",
            "E",
            "F",
            "F#",
            "G",
            "G#",
            "A",
            "A#",
            "B",
        ]

    def build_scale(self, key=None, style=None):
        scale_key = key if key else self.key
        scale_style = style if style else self.style

        i = self.all_notes.index(scale_key)
        l = len(self.all_notes)
        scale = []
        if scale_style == "major":
            scale.append(self.all_notes[i])
            scale.append(self.all_notes[(i + 2) % l])
            scale.append(self.all_notes[(i + 4) % l])
            scale.append(self.all_notes[(i + 5) % l])
            scale.append(self.all_notes[(i + 7) % l])
            scale.append(self.all_notes[(i + 9) % l])
            scale.append(self.all_notes[(i + 11) % l])
        elif scale_style == "minor":
            scale.append(self.all_notes[i])
            scale.append(self.all_notes[(i + 2) % l])
            scale.append(self.all_notes[(i + 3) % l])
            scale.append(self.all_notes[(i + 5) % l])
            scale.append(self.all_notes[(i + 7) % l])
            scale.append(self.all_notes[(i + 8) % l])
            scale.append(self.all_notes[(i + 10) % l])
        return scale
