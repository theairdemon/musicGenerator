import random

from midiutil.MidiFile import MIDIFile
from datetime import datetime
import os

# Custom Classes
from Generators.GenChords import GenChords
from Generators.GenMelody import GenMelody
from Generators.GenRhythm import GenRhythm


class SongGeneration:

    def __init__(self, song_dict):
        # BASIC SONG INFORMATION
        # song key
        self.key = song_dict["key"]
        # 'major' or 'minor'
        self.style = song_dict["style"]
        # default is 4 chords
        self.length = song_dict["length"]
        # default is 1 verse
        self.verses = song_dict["verses"]
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
        # self.gen_melody()
        melodyGenerator = GenMelody(self.genre, self.scale, self.chords, self.chord_notes, self.rhythm)
        self.melody = melodyGenerator.build()
        
        # self.gen_harmony()
        self.gen_MIDI()

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

    # ============ #
    # BUILD MELODY #
    # ============ #
    def gen_melody(self):
        prob_1_3_same, prob_2_4_same = self.prob_same()

        for i in range(0, len(self.chords)):
            # chance of skipping generation and repeating the melody
            # this checks if the random value fits and also if the rhythm is the same
            if i > 1 and self.rhythm[i] == self.rhythm[i-2] and len(self.chords) == 4:
                r_same = random.uniform(0, 1)
                if (i == 2 and r_same <= prob_1_3_same) or (i == 3 and r_same <= prob_2_4_same):
                    self.melody.append(self.melody[i-2])
                    continue
            starting_note = random.choice(self.chord_notes[i])
            measure = [[starting_note, self.rhythm[i][0]]]
            # loop over the rhythm and build notes from it
            for j in range(1, len(self.rhythm[i])):
                prev_note = measure[j-1][0]
                note = prev_note
                scale_i = self.scale.index(prev_note)
                if self.rhythm[i][j] < 2:
                    if scale_i + 1 == len(self.scale):
                        note = random.choice(
                            [self.scale[scale_i - 1], self.scale[scale_i]])
                    elif scale_i - 1 == -1:
                        note = random.choice(
                            [self.scale[scale_i + 1], self.scale[scale_i]])
                    else:
                        note = random.choice([self.scale[scale_i + 1],
                                              self.scale[scale_i - 1],
                                              self.scale[scale_i]])
                else:
                    for k in range(scale_i):
                        note_below = self.scale[max(scale_i - k, 0)]
                        note_above = self.scale[min(
                            scale_i + k, len(self.scale) - 1)]
                        if note_below in self.chord_notes:
                            note = note_below
                        elif note_above in self.chord_notes:
                            note = note_above
                measure.append([note, self.rhythm[i][j]])
            self.melody.append(measure)

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

    def gen_MIDI(self):
        # print(str(self.melody))
        # create your MIDI object
        track_length = 4
        tracks = [i for i in range(track_length)]

        track_harmonies = []
        for i in range(1, len(self.harmonies)+1):
            track_harmonies.append(tracks[-1] + i)
        mf = MIDIFile(len(tracks) + len(track_harmonies))

        time = 0
        mf.addTrackName(tracks[0], time, self.file_name + "_melody")
        mf.addTrackName(tracks[1], time, self.file_name + "_chords")
        mf.addTrackName(tracks[2], time, self.file_name + "_arp_1_4")
        mf.addTrackName(tracks[3], time, self.file_name + "_arp_1_8")

        # for i in range(0, len(track_harmonies)):
        #     mf.addTrackName(track_harmonies[i], time, self.file_name + "_harmony_" + self.harmony_names[i])

        # add some notes
        channel = 0
        channel_chords = 0
        channel_melody = 1
        volume = 100

        last_pitch = 0
        # MELODY
        for i in range(0, len(self.melody)):
            measure = self.melody[i]
            measure_time = i * 4

            for j in range(0, len(measure)):
                note = measure[j][0]
                pitch1 = self.notes_dict[note][1]
                pitch2 = self.notes_dict[note][2]
                pitch3 = self.notes_dict[note][3]

                dist1 = (pitch1 - last_pitch)**2
                dist2 = (pitch2 - last_pitch)**2
                dist3 = (pitch3 - last_pitch)**2
                distances = [dist1, dist2, dist3]

                if min(distances) == dist1:
                    pitch = pitch1
                elif min(distances) == dist2:
                    pitch = pitch2
                else:
                    pitch = pitch3
                duration = measure[j][1]
                mf.addNote(tracks[0], channel, pitch,
                           measure_time, duration, volume)

                measure_time += duration
                last_pitch = pitch

        # CHORDS
        overall_chord_time = 0
        for v in range(self.verses):
            for i in range(0, len(self.chord_notes)):
                chord = self.chord_notes[i]
                chord_time = overall_chord_time + i * 4
                pitches = [self.notes_dict[chord[0]][0],
                           self.notes_dict[chord[1]][0], self.notes_dict[chord[2]][0]]
                duration = 4
                for pitch in pitches:
                    mf.addNote(tracks[1], channel, pitch,
                               chord_time, duration, 65)
            overall_chord_time += len(self.chord_notes) * 4

        # 1/4 ARP
        overall_chord_time = 0
        for v in range(self.verses):
            for i in range(0, len(self.chord_notes)):
                chord = self.chord_notes[i]
                chord_time = overall_chord_time + i * 4
                pitches = [self.notes_dict[chord[0]][0],
                           self.notes_dict[chord[1]][0], self.notes_dict[chord[2]][0]]
                pitches.append(pitches[1])
                duration = 1
                for i in range(4):
                    mf.addNote(tracks[2], channel, pitches[i],
                               chord_time, duration, 65)
                    chord_time += duration
            overall_chord_time += len(self.chord_notes) * 4

        # 1/8 ARP
        overall_chord_time = 0
        for v in range(self.verses):
            for i in range(0, len(self.chord_notes)):
                chord = self.chord_notes[i]
                chord_time = overall_chord_time + i * 4
                pitches = [self.notes_dict[chord[0]][0],
                           self.notes_dict[chord[1]][0], self.notes_dict[chord[2]][0]]
                pitches.append(pitches[1])
                duration = 0.5
                for i in range(8):
                    mf.addNote(tracks[3], channel, pitches[i %
                               4], chord_time, duration, 65)
                    chord_time += duration
            overall_chord_time += len(self.chord_notes) * 4

        last_pitch = 0
        for k in range(len(self.harmonies)):
            for i in range(len(self.harmonies[k])):
                measure = self.harmonies[k][i]
                measure_time = i * 4

                for j in range(len(measure)):
                    note = measure[j][0]
                    pitch1 = self.notes_dict[note][1]
                    pitch2 = self.notes_dict[note][2]
                    pitch3 = self.notes_dict[note][3]

                    dist1 = (pitch1 - last_pitch)**2
                    dist2 = (pitch2 - last_pitch)**2
                    dist3 = (pitch3 - last_pitch)**2
                    distances = [dist1, dist2, dist3]

                    if min(distances) == dist1:
                        pitch = pitch1
                    elif min(distances) == dist2:
                        pitch = pitch2
                    else:
                        pitch = pitch3
                    duration = measure[j][1]
                    mf.addNote(track_harmonies[k], channel,
                               pitch, measure_time, duration, volume)

                    measure_time += duration
                    last_pitch = pitch

        # write it to disk
        fullFileName = self.folder_location + \
            self.file_location + self.file_name + ".mid"
        f = open(fullFileName, 'w')
        f.close()
        with open(fullFileName, 'wb') as outf:
            mf.writeFile(outf)

    # ================ #
    # HELPER FUNCTIONS #
    # ================ #
    def prob_same(self):
        # probability of measures 1/3 and 2/4 being identical in a 4 bar series
        # the bridge is most likely gonna be similar for measures 1 and 3
        if self.verse_type == "bridge":
            prob_1_3_same = 0.6
            prob_2_4_same = 0.0
        # the chorus should feel a bit repetitive, but not overly so
        # we usually want each breath to end the same
        elif self.verse_type == "chorus":
            prob_1_3_same = 0.1
            prob_2_4_same = 0.9
        # we want some continuity betwee verses, so some repetition is ok
        else:
            prob_1_3_same = 0.3
            prob_2_4_same = 0.0
        return prob_1_3_same, prob_2_4_same
