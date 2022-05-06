import random
from midiutil.MidiFile import MIDIFile
from datetime import datetime
import os

class SongGeneration:
    
    def __init__(self, key, style='major', length=4, verses=1, verse_type="verse", rhythm=[], file_name="test", file_location=""):
        self.key = key
        self.style = style # 'major' or 'minor'
        self.length = length # default is 4 chords
        self.verses = verses # default is 1 verse
        self.verse_type = verse_type # default is verse
        self.file_name = file_name # maximum recommended length: 9
        self.file_location = file_location # where to save the midi file
        
        # Chord Progression Dictionaries
        self.chord_prog_maj = {'I':[['V', 'vii'], ['ii', 'IV'], ['vi'], ['iii']],
                          'ii':['V', 'vii'],
                          'iii': ['vi'],
                          'IV':['V', 'vii'],
                          'V': ['I'],
                          'vi': ['ii', 'IV'],
                          'vii': ['iii', 'I']}
        
        self.chord_prog_min = {'i':[['V'], ['ii', 'iv'], ['VI'], ['III'], ['VII']],
                          'ii':['V'],
                          'III': ['VI'],
                          'iv':['V'],
                          'V': ['i'],
                          'VI': ['ii', 'iv'],
                          'VII' : ['III']}
        # select which chord_prog to use depending on major or minor input
        self.chord_prog = self.chord_prog_maj if self.style == 'major' else self.chord_prog_min
        self.one_cycle = 4 if self.style == 'major' else 5 # for use in chord prog picking
        
        # List of all possible notes, rhythms, and rhythm weights
        self.all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.all_rhythms = [0.25, 0.5, 1, 2]
        self.all_rhythm_weights = [0.1, 0.4, 0.95, 1.0]
        
        # Notes dictionary for MIDI file
        self.notes_dict = {}
        bass = 48
        treble1 = 60
        treble2 = 72
        treble3 = 84
        for i in range(0, len(self.all_notes)):
            self.notes_dict[self.all_notes[i]] = [bass + i, treble1 + i, treble2 + i, treble3 + i]
        
        # Class variables, for use in generation functions
        self.scale = []
        self.chords = []
        self.chord_notes = []
        self.melody = []
        self.rhythm_intro = rhythm
        self.rhythm = []
        self.harmony_names = ["3rd_down", "3rd_up", "4th_up", "5th_up", "8_up", "8_down"]
        self.harmonies = []
        for name in self.harmony_names:
            self.harmonies.append([])
    
    def __str__(self):
        return_string = str(self.key) + " " + str(self.style) + "\n" + str(self.chords) + "\n" 
        #return_string += str(self.chord_notes) + "\n" + str(self.rhythm) + "\n"
        #return_string += str(self.melody)
        return return_string

    # ============================ #
    # MAIN SONG GENERATION CONTROL #
    # ============================ #
    def gen_song(self):
        self.gen_scale()
        self.gen_chords()
        for i in range(self.verses):
            self.gen_rhythm()
            self.gen_melody()
            self.gen_harmony()
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
                    new_start_value = (self.length - sub_value) % self.one_cycle
                else: 
                    new_start_value = (self.length - 5) % self.one_cycle
                next_chord = random.choice(self.chord_prog[chords[-1]][new_start_value])
            chords.append(next_chord)
            
        self.chords = chords
        # adding the specific notes for each chord
        # if adding more chords, add the notes for those chords here
        for chord in self.chords:
            if chord == 'I' or chord == 'i':
                self.chord_notes.append([self.scale[0], self.scale[2], self.scale[4]])
            elif chord == 'ii':
                self.chord_notes.append([self.scale[1], self.scale[3], self.scale[5]])
            elif chord == 'iii' or chord == 'III':
                self.chord_notes.append([self.scale[2], self.scale[4], self.scale[6]])
            elif chord == 'IV' or chord == 'iv':
                self.chord_notes.append([self.scale[3], self.scale[5], self.scale[0]])
            elif chord == 'V':
                self.chord_notes.append([self.scale[4], self.scale[6], self.scale[1]])
            elif chord == 'vi' or chord == 'VI':
                self.chord_notes.append([self.scale[5], self.scale[0], self.scale[2]])
            elif chord == 'vii' or chord == 'VII':
                self.chord_notes.append([self.scale[6], self.scale[1], self.scale[3]])
        #print(self.chords)

    # ============ #
    # BUILD RHYTHM #
    # ============ #
    def gen_rhythm(self):
        prob_1_3_same, prob_2_4_same = self.prob_same()
        
        if len(self.rhythm_intro) == 0:
            for i in range(len(self.chords)):
                # chance of skipping generation and repeating the rhythm
                if i > 1 and len(self.chords) == 4:
                    r_same = random.uniform(0, 1)
                    if (i == 2 and r_same < prob_1_3_same) or (i == 3 and r_same < prob_2_4_same):
                        self.rhythm.append(self.rhythm[i-2])
                        continue
                chord = self.chords[i]
                total = 0
                measure = []
                while total < 4:
                    # pick a weighted random note
                    r1 = random.uniform(0, 1)
                    new_note = self.all_rhythms[-1]  
                    for i in range(0, len(self.all_rhythm_weights)):
                        if self.all_rhythm_weights[i] <= r1:
                            new_note = self.all_rhythms[i]                            
                    
                    # only add note size that fits inside the measure
                    if total + new_note > 4:
                        new_note = 4 - total
                    measure.append(new_note)
                    total += new_note
                    
                    # some percent chance to replicate the same note, creating runs of the same size
                    # only if the note is < one beat long
                    if new_note < 1 and total + new_note <= 4:
                        r2 = random.uniform(0, 1)
                        if r2 < 0.5:
                            measure.append(new_note)
                            total += new_note
                    
                self.rhythm.append(measure)
                
        else:
            for i in range(0, len(self.chords)):
                # chance of skipping generation and repeating the rhythm
                if i > 1 and len(self.chords) == 4:
                    r_same = random.uniform(0, 1)
                    if (i == 2 and r_same < prob_1_3_same) or (i == 3 and r_same < prob_2_4_same):
                        self.rhythm.append(self.rhythm[i-2])
                        continue
                
                num_notes = self.rhythm_intro[i]
                total = 4
                rough_notes = total / num_notes
                raw_measure = [rough_notes for i in range(0, num_notes)]
                measure = []
                for note in raw_measure:
                    #self.all_rhythms = [0.25, 0.5, 1, 2]
                    closest_two = [0.25, 0.5]
                    if note > 0.5:
                        closest_two[0] = 1
                    if note > 1:
                        closest_two[1] = 2
                        
                    measure.append(random.choice(closest_two))
                
                if sum(measure) > 4:
                    while sum(measure) > 4:
                        max_note = max(measure)
                        note_loc = measure.index(max_note)
                        if max_note > sum(measure) - 4:
                            new_note = max_note - (sum(measure) - 4)
                        else:
                            new_note = max_note / 2
                        measure[note_loc] = new_note
                elif sum(measure) < 4:
                    while sum(measure) < 4:
                        min_note = min(measure)
                        note_loc = measure.index(min_note)
                        new_note = min_note + (4 - sum(measure))
                        measure[note_loc] = new_note
                        
                self.rhythm.append(measure)      
                
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
                        note = random.choice([self.scale[scale_i - 1], self.scale[scale_i]])
                    elif scale_i - 1 == -1:
                        note = random.choice([self.scale[scale_i + 1], self.scale[scale_i]])
                    else:
                        note = random.choice([self.scale[scale_i + 1], 
                                              self.scale[scale_i - 1], 
                                              self.scale[scale_i]])
                else:
                    for k in range(scale_i):
                        note_below = self.scale[max(scale_i - k, 0)]
                        note_above = self.scale[min(scale_i + k, len(self.scale) - 1)]
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
                    if i == 2: h_value = 4
                    elif i == 3: h_value = 5
                    else: h_value = 0

                    note_i = self.scale.index(note[0])
                    if i == 0 or i == 5:
                        h_note = self.scale[(note_i - h_value) % len(self.scale)]
                    else:
                        h_note = self.scale[(note_i + h_value) % len(self.scale)]

                    harmony[-1].append([h_note, note[1]])
                    h_value += 1
    
    def gen_MIDI(self):
        #print(str(self.melody))
        # create your MIDI object
        tracks = [0, 1, 2, 3]
        track_harmonies = []
        for i in range(1, len(self.harmonies)+1):
            track_harmonies.append(tracks[-1] + i)
        mf = MIDIFile(len(tracks) + len(track_harmonies))

        time = 0
        mf.addTrackName(tracks[0], time, self.file_name + "_melody")
        mf.addTrackName(tracks[1], time, self.file_name + "_chords")
        mf.addTrackName(tracks[2], time, self.file_name + "_arp_1_4")
        mf.addTrackName(tracks[3], time, self.file_name + "_arp_1_8")

        for i in range(0, len(track_harmonies)):
            mf.addTrackName(track_harmonies[i], time, self.file_name + "_harmony_" + self.harmony_names[i])
        

        # add some notes
        channel = 0
        channel_chords = 0
        channel_melody = 1
        volume = 100
        
        last_pitch = 0
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
                mf.addNote(tracks[0], channel, pitch, measure_time, duration, volume)
                
                measure_time += duration
                last_pitch = pitch
        
        overall_chord_time = 0
        for v in range(self.verses):
            for i in range(0, len(self.chord_notes)):
                chord = self.chord_notes[i]
                chord_time = overall_chord_time + i * 4
                pitches = [self.notes_dict[chord[0]][0], self.notes_dict[chord[1]][0], self.notes_dict[chord[2]][0]]
                duration = 4
                for pitch in pitches:
                    mf.addNote(tracks[1], channel, pitch, chord_time, duration, 65)
            overall_chord_time += len(self.chord_notes) * 4
        
        overall_chord_time = 0
        for v in range(self.verses):
            for i in range(0, len(self.chord_notes)):
                chord = self.chord_notes[i]
                chord_time = overall_chord_time + i * 4
                pitches = [self.notes_dict[chord[0]][0], self.notes_dict[chord[1]][0], self.notes_dict[chord[2]][0]]
                pitches.append(pitches[1])
                duration = 1
                for i in range(4):
                    mf.addNote(tracks[2], channel, pitches[i], chord_time, duration, 65)
                    chord_time += duration
            overall_chord_time += len(self.chord_notes) * 4
            
        overall_chord_time = 0
        for v in range(self.verses):
            for i in range(0, len(self.chord_notes)):
                chord = self.chord_notes[i]
                chord_time = overall_chord_time + i * 4
                pitches = [self.notes_dict[chord[0]][0], self.notes_dict[chord[1]][0], self.notes_dict[chord[2]][0]]
                pitches.append(pitches[1])
                duration = 0.5
                for i in range(8):
                    mf.addNote(tracks[3], channel, pitches[i % 4], chord_time, duration, 65)
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
                    mf.addNote(track_harmonies[k], channel, pitch, measure_time, duration, volume)
                    
                    measure_time += duration
                    last_pitch = pitch

        # write it to disk
        with open("midi_files\\" + self.file_location + self.file_name + ".mid", 'wb') as outf:
            mf.writeFile(outf)
        
    # ================ #
    # HELPER FUNCTIONS #
    # ================ #
    def prob_same(self):
        # probability of measures 1/3 and 2/4 being identical in a 4 bar series
        if self.verse_type == "bridge":
            prob_1_3_same = 0.1
            prob_2_4_same = 0.0
        elif self.verse_type == "chorus":
            prob_1_3_same = 0.0
            prob_2_4_same = 0.9
        else:
            prob_1_3_same = 0.6
            prob_2_4_same = 0.0
        return prob_1_3_same, prob_2_4_same

# Generate a complete song
def fullSongGen(key, minorKey, folder, song_style, script_dir):
    song_info_file = "song_info.txt"
    f = open(script_dir + folder + song_info_file, "w")

    verse1 = SongGeneration(key, style=song_style, length=4, verses=1, verse_type="verse", file_name="verse1", file_location=folder)
    verse1.gen_song()
    f.write("Verse 1\n")
    f.write(str(verse1))

    chorus = SongGeneration(key, style=song_style, length=4, verses=1, verse_type="chorus", file_name="chorus", file_location=folder)
    chorus.gen_song()
    f.write("\nChorus\n")
    f.write(str(chorus))

    verse2 = SongGeneration(key, style=song_style, length=4, verses=1, verse_type="verse", file_name="verse2", file_location=folder)
    verse2.gen_song()
    f.write("\nVerse 2\n")
    f.write(str(verse2))

    bridge = SongGeneration(key, style=song_style, length=7, verses=1, verse_type="bridge", file_name="bridge", file_location=folder)
    bridge.gen_song()
    f.write("\nBridge\n")
    f.write(str(bridge))

    if song_style == "major":
        minorBridge = SongGeneration(minorKey, style="minor", length=7, verses=1, verse_type="bridge", file_name="minorBridge", file_location=folder)
        minorBridge.gen_song()
        f.write("\nMinor Bridge\n")
        f.write(str(minorBridge))

    f.close()

if __name__ == "__main__":
    note_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    # key = random.choice(note_list)
    key = 'A#'
    minorKey = note_list[(note_list.index(key) + 9) % len(note_list)]
    print(key, minorKey)

    # test_song = SongGeneration(key, style='minor', rhythm = [7, 8, 7, 8], length=4, verses=1)
    # test_song.gen_song()
    # print(test_song.scale)

    folder = "test_january_2022\\"
    song_style = "major"
    # OTHER PEOPLE: CHANGE THIS LINE FOR YOUR OWN DIRECTORY path
    script_dir = "D:\\Documents\\Github\\musicGenerator\\midi_files\\"
    fullSongGen(key, minorKey, folder, song_style, script_dir)