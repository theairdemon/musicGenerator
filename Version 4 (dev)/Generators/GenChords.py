import random

from Builders.ChordBuilder import ChordBuilder


class GenChords:

    def __init__(
        self,
        key,
        style,
        length,
        verse_type,
        startRoot,
        prebuilt_name="random",
        using_prebuilt=False,
    ):
        # Common parameters across all styles of songs
        self.key = key
        self.style = style

        # ================================= #
        # FOR GENERATING CHORD PROGRESSIONS #
        # ================================= #
        self.length = length
        # verse_type -> basically checking bridge or not lol
        self.verse_type = verse_type
        # startRoot -> determines whether we start or finish on the root chord
        self.startRoot = startRoot

        # ================== #
        # DEFINING CONSTANTS #
        # ================== #
        # Chord Progression Dictionaries
        self.chords = []
        self.chord_notes = []
        self.chord_prog_maj = {
            "I": [["V", "vii"], ["ii", "IV"], ["vi"], ["iii"]],
            "ii": ["V", "vii"],
            "iii": ["vi"],
            "IV": ["V", "vii"],
            "V": ["I"],
            "vi": ["ii", "IV"],
            "vii": ["iii", "I"],
        }
        self.chord_prog_min = {
            "i": [["V"], ["ii", "iv"], ["VI"], ["III"], ["VII"]],
            "ii": ["V"],
            "III": ["VI"],
            "iv": ["V"],
            "V": ["i"],
            "VI": ["ii", "iv"],
            "VII": ["III"],
        }
        # select which chord_prog to use depending on major or minor input
        self.chord_prog = (
            self.chord_prog_maj if self.style == "major" else self.chord_prog_min
        )
        self.one_cycle = (
            4 if self.style == "major" else 5
        )  # for use in chord prog picking

        # =============================== #
        # FOR USING PREBUILT PROGRESSIONS #
        # =============================== #
        # prebuilt -> something new I'm experimenting with
        # Adding some prebuilt chord structures like I-V-vi-IV, Pachelbel's Canon, etc.
        self.prebuilt_name = prebuilt_name
        self.using_prebuilt = using_prebuilt

        # ===================== #
        # PREBUILT PROGRESSIONS #
        # ===================== #
        self.prebuilt_chords_maj = {
            "pop_four": ["I", "V", "vi", "IV"],
            "pachelbel": ["I", "V", "vi", "iii", "IV", "I", "IV", "V"],
        }
        self.prebuilt_chords_min = {
            "wonderwall": ["i", "III", "VII", "IV"],
            # TODO: how to get this to be "double-time"? Interesting problem
            "bo_burnham": ["i", "i", "iv", "iv", "VII", "VII", "III", "V"],
            # TODO: figure out 7th chords
            "in_the_pines": ["i", "i", "iv", "i", "i", "V", "i", "i"],
        }

    def build(self):
        if self.using_prebuilt:
            self.gen_prebuilt_chords()
        else:
            self.gen_chords()
        self.convert_chords()
        return self.chords, self.chord_notes

    # ======================== #
    # BUILD CHORDS PROGRESSION #
    # ======================== #
    def gen_prebuilt_chords(self):
        if self.prebuilt_name != "random":
            if self.prebuilt_name in self.prebuilt_chords_maj:
                self.chords = self.prebuilt_chords_maj[self.prebuilt_name]
            elif self.prebuilt_name in self.prebuilt_chords_min:
                self.chords = self.prebuilt_chords_min[self.prebuilt_name]
        else:
            if self.style == "major":
                self.prebuilt_name = random.choice(
                    list(self.prebuilt_chords_maj.keys())
                )
                self.chords = self.prebuilt_chords_maj[self.prebuilt_name]
            elif self.style == "minor":
                self.prebuilt_name = random.choice(
                    list(self.prebuilt_chords_min.keys())
                )
                self.chords = self.prebuilt_chords_min[self.prebuilt_name]
        print(f"Using prebuilt progression: {self.prebuilt_name}, {self.chords}")

    def gen_chords(self):
        chords = ["I"] if self.style == "major" else ["i"]
        sub_value = 2
        start_value = (self.length - sub_value) % self.one_cycle
        start_chord = random.choice(self.chord_prog[chords[0]][start_value])
        chords.append(start_chord)

        # if there's room left, keep adding chords
        while len(chords) != self.length:
            # random choice chord
            if chords[-1] != "I" and chords[-1] != "i":
                next_chord = random.choice(self.chord_prog[chords[-1]])
            # moving from a minor 4th to a major 5th before looping
            elif chords[-1] == "iv" and len(chords) >= self.length - 2:
                next_chord = "V"
            # restart the cycle again
            else:
                if self.style == "major":
                    new_start_value = (self.length - sub_value) % self.one_cycle
                else:
                    new_start_value = (self.length - 5) % self.one_cycle
                next_chord = random.choice(self.chord_prog[chords[-1]][new_start_value])
            chords.append(next_chord)

        self.chords = chords
        # If instead of starting on the root, we want to start on another chord,
        # we will swap the root to the end of the chords here
        if not self.startRoot and self.verse_type != "bridge":
            tempChords = chords[1:]
            tempChords.append(chords[0])
            self.chords = tempChords
        print(f"Generated chords: {self.chords}")

    # ======================= #
    # CONVERT CHORDS TO NOTES #
    # ======================= #
    def convert_chords(self):
        chordBuilder = ChordBuilder(self.key)
        for chord in self.chords:
            self.chord_notes.append(chordBuilder.build_chord(chord))
