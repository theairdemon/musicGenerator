from midiutil.MidiFile import MIDIFile


class GenMidi:

    def __init__(self, song_dict):
        # FILE INFORMATION
        # maximum recommended length: 9
        self.file_name = song_dict["file_name"]
        # where to save the midi file
        self.file_location = song_dict["file_location"]
        # the full OS path to the folder
        self.folder_location = song_dict["folder_location"]

        # The GOOD stuff
        self.melody = song_dict["melody"]
        self.notes_dict = song_dict["notes_dict"]
        self.chord_notes = song_dict["chord_notes"]
        self.harmonies = song_dict["harmonies"]

    def build(self):
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
