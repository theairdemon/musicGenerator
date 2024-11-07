import random

from midiutil.MidiFile import MIDIFile
from datetime import datetime
import os

# Custom Classes
from Generators.GenChords import GenChords
from Generators.GenMelody import GenMelody
from Generators.GenRhythm import GenRhythm
from Generators.GenMidi import GenMidi


class SongGeneration:

    def __init__(self, song_dict):
        # BASIC SONG INFORMATION
        # song key
        self.key = song_dict["key"]
        # 'major' or 'minor'
        self.style = song_dict["style"]
        # default is 4 chords
        self.length = song_dict["length"]
        # default is verse
        self.verse_type = song_dict["verse_type"]
        # default is to start on the root chord
        self.startRoot = song_dict["startRoot"]
        # genre name - no default, since we always want a name
        self.genre = song_dict["genre"]

        # FILE INFORMATION
        # maximum recommended length: 9
        self.file_name = song_dict["file_name"]
        # where to save the midi file
        self.file_location = song_dict["file_location"]
        # the full OS path to the folder
        self.folder_location = song_dict["folder_location"]

        # ================== #
        # DEFINING CONSTANTS #
        # ================== #
        # List of all possible notes, rhythms, and rhythm weights
        self.all_notes = ['C', 'C#', 'D', 'D#', 'E',
                          'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        # ====================== #
        #  MIDI FILE CONVERSIONS #
        # ====================== #
        # Notes dictionary for MIDI file
        self.notes_dict = {}
        bass = 48
        treble1 = 60
        treble2 = 72
        treble3 = 84
        for i in range(0, len(self.all_notes)):
            self.notes_dict[self.all_notes[i]] = [
                bass + i, treble1 + i, treble2 + i, treble3 + i]

        # ================ #
        #  CLASS VARIABLES #
        # ================ #
        # for use in generation functions
        self.scale = []
        self.chords = []
        self.chord_notes = []
        self.melody = []
        self.volumes = []
        self.rhythm = []
        self.harmony_names = ["3rd_down", "3rd_up",
                              "4th_up", "5th_up", "8_up", "8_down"]
        self.harmonies = []
        for name in self.harmony_names:
            self.harmonies.append([])

    def __str__(self):
        return_string = str(self.key) + " " + \
            str(self.style) + "\n" + str(self.chords) + "\n"
        return return_string

    # TODO: add ramp up from verses to chorus maybe idk

    # ============================ #
    # MAIN SONG GENERATION CONTROL #
    # ============================ #
    def gen_song(self):
        self.gen_scale()

        # Chord Generation
        chordGenerator = GenChords(
            self.scale,
            self.style,
            self.length,
            self.verse_type,
            self.startRoot
        )
        self.chords, self.chord_notes = chordGenerator.build()

        # Rhythm Generation
        rhythmGenerator = GenRhythm(len(self.chords), self.genre)
        self.rhythm = rhythmGenerator.build()

        # Melody Generation
        melodyGenerator = GenMelody(
            self.genre, self.scale, self.chords, self.chord_notes, self.rhythm)
        self.melody, self.volumes = melodyGenerator.build()

        self.run_MIDI()

    # Small generation helper; builds 1 measure with the root chord and
    # a single sustained root note
    def gen_base_measure(self):
        self.gen_scale()

        chordGenerator = GenChords(
            self.scale,
            self.style,
            self.length,
            self.verse_type,
            True
        )
        self.chords, self.chord_notes = chordGenerator.build()
        self.chords = self.chords[:1]
        self.chord_notes = self.chord_notes[:1]
        self.melody = [[[self.key, 4]]]
        self.volumes = [[100]]
        self.run_MIDI()

    # =========== #
    # BUILD SCALE #
    # =========== #

    def gen_scale(self):
        i = self.all_notes.index(self.key)
        l = len(self.all_notes)
        if self.style == 'major':
            self.scale.append(self.all_notes[i])
            self.scale.append(self.all_notes[(i + 2) % l])
            self.scale.append(self.all_notes[(i + 4) % l])
            self.scale.append(self.all_notes[(i + 5) % l])
            self.scale.append(self.all_notes[(i + 7) % l])
            self.scale.append(self.all_notes[(i + 9) % l])
            self.scale.append(self.all_notes[(i + 11) % l])
        elif self.style == 'minor':
            self.scale.append(self.all_notes[i])
            self.scale.append(self.all_notes[(i + 2) % l])
            self.scale.append(self.all_notes[(i + 3) % l])
            self.scale.append(self.all_notes[(i + 5) % l])
            self.scale.append(self.all_notes[(i + 7) % l])
            self.scale.append(self.all_notes[(i + 8) % l])
            self.scale.append(self.all_notes[(i + 10) % l])

    # ============= #
    # BUILD HARMONY #
    # ============= #
    # TODO: make harmonies depend on the chord structure
    # something like, I -> 3rd&5th, IV -> 4th, V -> 5th, and all others -> octave
    # order of harmonies: ["3rd_down", "3rd_up", "4th_up", "5th_up", "8_up", "8_down"]
    # matching with chords: I -> 5th
    def gen_harmony(self):
        # loop over measures
        for measure in self.melody:
            for harmony in self.harmonies:
                harmony.append([])
            # loop over notes
            for note in measure:
                # this loop is very specific to the current order of harmonies
                h_value = 3
                for i in range(0, len(self.harmonies)):
                    harmony = self.harmonies[i]
                    if i == 2:
                        h_value = 4
                    elif i == 3:
                        h_value = 5
                    else:
                        h_value = 0

                    note_i = self.scale.index(note[0])
                    if i == 0 or i == 5:
                        h_note = self.scale[(note_i - h_value) %
                                            len(self.scale)]
                    else:
                        h_note = self.scale[(note_i + h_value) %
                                            len(self.scale)]

                    harmony[-1].append([h_note, note[1]])
                    h_value += 1

    def gen_drums(self):
        print("testing drums")

    def run_MIDI(self):
        new_song_dict = {}
        # FILE INFORMATION
        # maximum recommended length: 9
        new_song_dict["file_name"] = self.file_name
        # where to save the midi file
        new_song_dict["file_location"] = self.file_location
        # the full OS path to the folder
        new_song_dict["folder_location"] = self.folder_location

        # The GOOD stuff
        new_song_dict["melody"] = self.melody
        new_song_dict["volumes"] = self.volumes
        new_song_dict["notes_dict"] = self.notes_dict
        new_song_dict["chord_notes"] = self.chord_notes
        new_song_dict["harmonies"] = self.harmonies

        # Run the midi generator
        midiGenerator = GenMidi(new_song_dict)
        midiGenerator.build()

    def add_SongDict(self, song_dict):
        song_dict["melody"] += self.melody
        song_dict["volumes"] += self.volumes
        song_dict["notes_dict"] = self.notes_dict
        song_dict["chord_notes"] += self.chord_notes
        song_dict["harmonies"] += self.harmonies

        return song_dict
