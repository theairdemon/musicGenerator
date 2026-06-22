import random


class GenChords:

    def __init__(
        self,
        scale_major,
        scale_minor,
        style,
        length,
        verse_type,
        startRoot,
        prebuilt_name="random",
        using_prebuilt=False,
    ):
        # Common parameters across all styles of songs
        self.scale_major = scale_major
        self.scale_minor = scale_minor
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
        print(f"Using prebuilt progression: {self.prebuilt_name}")

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
        # adding the specific notes for each chord
        # if adding more chords, add the notes for those chords here
        for chord in self.chords:
            match chord:
                case "I":  # 1, 3, 5
                    self.chord_notes.append(
                        [self.scale_major[0], self.scale_major[2], self.scale_major[4]]
                    )
                case "i":  # 1, 3, 5
                    self.chord_notes.append(
                        [self.scale_minor[0], self.scale_minor[2], self.scale_minor[4]]
                    )
                case "ii":  # 2, 4, 6
                    self.chord_notes.append(
                        [self.scale_major[1], self.scale_major[3], self.scale_major[5]]
                    )
                # TODO: Same output for III and iii?
                # III is really only used in minor scales, so we need the minor not major
                # iii is only used in major scales
                # e.g. C E Am F becomes minor scale III V i VI
                case "III":  # 3, 5, 7
                    self.chord_notes.append(
                        [self.scale_minor[2], self.scale_minor[4], self.scale_minor[6]]
                    )
                case "iii":  # 3, 5, 7
                    self.chord_notes.append(
                        [self.scale_major[2], self.scale_major[4], self.scale_major[6]]
                    )
                case "IV":  # 4, 6, 1
                    self.chord_notes.append(
                        [self.scale_major[3], self.scale_major[5], self.scale_major[0]]
                    )
                case "iv":  # 4, 6, 1
                    self.chord_notes.append(
                        [self.scale_minor[3], self.scale_minor[5], self.scale_minor[0]]
                    )
                case "V":  # 5, 7, 2
                    self.chord_notes.append(
                        [self.scale_major[4], self.scale_major[6], self.scale_major[1]]
                    )
                case "vi":  # 6, 1, 3
                    self.chord_notes.append(
                        [self.scale_major[5], self.scale_major[0], self.scale_major[2]]
                    )
                case "VI":  # 6, 1, 3
                    self.chord_notes.append(
                        [self.scale_major[5], self.scale_major[0], self.scale_major[2]]
                    )
                case "vii":  # 7, 2, 4
                    self.chord_notes.append(
                        [self.scale_major[6], self.scale_major[1], self.scale_major[3]]
                    )
                case "VII":  # 7, 2, 4
                    self.chord_notes.append(
                        [self.scale_major[6], self.scale_major[1], self.scale_major[3]]
                    )
