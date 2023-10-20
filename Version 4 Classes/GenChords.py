import random


class GenChords:

    def __init__(self, scale, style, length, verse_type, startRoot):
        # Input Parameters
        self.scale = scale
        self.style = style
        self.length = length
        self.verse_type = verse_type
        self.startRoot = startRoot

        # ================== #
        # DEFINING CONSTANTS #
        # ================== #
        # Chord Progression Dictionaries
        self.chords = []
        self.chord_notes = []
        self.chord_prog_maj = {'I': [['V', 'vii'], ['ii', 'IV'], ['vi'], ['iii']],
                               'ii': ['V', 'vii'],
                               'iii': ['vi'],
                               'IV': ['V', 'vii'],
                               'V': ['I'],
                               'vi': ['ii', 'IV'],
                               'vii': ['iii', 'I']}
        self.chord_prog_min = {'i': [['V'], ['ii', 'iv'], ['VI'], ['III'], ['VII']],
                               'ii': ['V'],
                               'III': ['VI'],
                               'iv': ['V'],
                               'V': ['i'],
                               'VI': ['ii', 'iv'],
                               'VII': ['III']}
        # select which chord_prog to use depending on major or minor input
        self.chord_prog = self.chord_prog_maj if self.style == 'major' else self.chord_prog_min
        self.one_cycle = 4 if self.style == 'major' else 5  # for use in chord prog picking

    def build(self):
        self.gen_chords()
        self.convert_chords()
        return self.chords, self.chord_notes

    # ======================== #
    # BUILD CHORDS PROGRESSION #
    # ======================== #
    def gen_chords(self):
        chords = ['I'] if self.style == 'major' else ['i']
        sub_value = 2
        start_value = (self.length - sub_value) % self.one_cycle
        start_chord = random.choice(self.chord_prog[chords[0]][start_value])
        chords.append(start_chord)

        # if there's room left, keep adding chords
        while len(chords) != self.length:
            # random choice chord
            if chords[-1] != 'I' and chords[-1] != 'i':
                next_chord = random.choice(self.chord_prog[chords[-1]])
            # moving from a minor 4th to a major 5th before looping
            elif chords[-1] == 'iv' and len(chords) >= self.length - 2:
                next_chord = 'V'
            # restart the cycle again
            else:
                if self.style == 'major':
                    new_start_value = (
                        self.length - sub_value) % self.one_cycle
                else:
                    new_start_value = (self.length - 5) % self.one_cycle
                next_chord = random.choice(
                    self.chord_prog[chords[-1]][new_start_value])
            chords.append(next_chord)

        self.chords = chords
        # If instead of starting on the root, we want to start on another chord,
        # we will swap the root to the end of the chords here
        if not self.startRoot and self.verse_type != 'bridge':
            tempChords = chords[1:]
            tempChords.append(chords[0])
            self.chords = tempChords

    # ======================= #
    # CONVERT CHORDS TO NOTES #
    # ======================= #
    def convert_chords(self):
        # adding the specific notes for each chord
        # if adding more chords, add the notes for those chords here
        for chord in self.chords:
            if chord == 'I' or chord == 'i':
                self.chord_notes.append(
                    [self.scale[0], self.scale[2], self.scale[4]])
            elif chord == 'ii':
                self.chord_notes.append(
                    [self.scale[1], self.scale[3], self.scale[5]])
            elif chord == 'iii' or chord == 'III':
                self.chord_notes.append(
                    [self.scale[2], self.scale[4], self.scale[6]])
            elif chord == 'IV' or chord == 'iv':
                self.chord_notes.append(
                    [self.scale[3], self.scale[5], self.scale[0]])
            elif chord == 'V':
                self.chord_notes.append(
                    [self.scale[4], self.scale[6], self.scale[1]])
            elif chord == 'vi' or chord == 'VI':
                self.chord_notes.append(
                    [self.scale[5], self.scale[0], self.scale[2]])
            elif chord == 'vii' or chord == 'VII':
                self.chord_notes.append(
                    [self.scale[6], self.scale[1], self.scale[3]])
