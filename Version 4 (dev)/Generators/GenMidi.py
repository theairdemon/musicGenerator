from midiutil.MidiFile import MIDIFile
import random


class GenMidi:

    def __init__(self, song_dict, tracks_list=None):
        # FILE INFORMATION
        # maximum recommended length: 9
        self.file_name = song_dict["file_name"]
        # where to save the midi file
        self.file_location = song_dict["file_location"]
        # the full OS path to the folder
        self.folder_location = song_dict["folder_location"]

        # The GOOD stuff
        self.melody = song_dict["melody"]
        self.volumes = song_dict["volumes"]
        self.notes_dict = song_dict["notes_dict"]
        self.chord_notes = song_dict["chord_notes"]
        self.harmonies = song_dict["harmonies"]
        if not tracks_list:
            self.tracks_list = ['melody', 'chords', 'arpeggios']
        else:
            self.tracks_list = tracks_list

    def build(self):
        # create your MIDI object
        # track_length = 4
        tracks = [i for i in range(len(self.tracks_list))]

        track_harmonies = []

        mf = MIDIFile(len(tracks))

        time = 0
        for i in tracks:
            mf.addTrackName(i, time, self.file_name +
                            "_" + self.tracks_list[i])

        # add some notes
        channel_chords = 0
        channel_melody = 1
        # channel_melody = 0
        channel_arp = 2
        # channel_arp = 0
        channel_harmonies = 3
        # channel_harmonies = 0
        volume = 100

        last_pitch = 0
        current_track = 0

        while "melody" in self.tracks_list[current_track]:
            # MELODY
            for i in range(0, len(self.melody)):
                measure = self.melody[i]
                volumes = self.volumes[i]
                measure_time = i * 4

                for j in range(0, len(measure)):
                    volume = volumes[j]
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

                    mf.addNote(current_track, channel_melody, pitch,
                               measure_time, duration, volume)

                    measure_time += duration
                    last_pitch = pitch
            current_track += 1

        # default volume for chords and arps
        chords_volume = 100
        arp_volume = 40

        # CHORDS
        while "chords" in self.tracks_list[current_track]:
            overall_chord_time = 0
            for i in range(0, len(self.chord_notes)):
                chord = self.chord_notes[i]
                chord_time = overall_chord_time + i * 4
                pitches = [self.notes_dict[chord[0]][0],
                           self.notes_dict[chord[1]][0], self.notes_dict[chord[2]][0]]
                duration = 4
                for pitch in pitches:
                    mf.addNote(tracks[current_track], channel_chords, pitch,
                               chord_time, duration, chords_volume)
            overall_chord_time += len(self.chord_notes) * 4
            current_track += 1

        # 1/4 ARP
        while "arpeggios" in self.tracks_list[current_track]:
            overall_chord_time = 0
            for i in range(0, len(self.chord_notes)):
                # silence arpeggios if we're in a 1 measure verse
                if len(self.melody[i]) == 1:
                    support_volume = 0
                else:
                    support_volume = 65
                chord = self.chord_notes[i]
                chord_time = overall_chord_time + i * 4
                pitches = [self.notes_dict[chord[0]][0],
                           self.notes_dict[chord[1]][0], self.notes_dict[chord[2]][0]]
                pitches.append(pitches[1])
                duration = 1
                for i in range(4):
                    mf.addNote(tracks[current_track], channel_arp, pitches[i],
                               chord_time, duration, arp_volume)
                    chord_time += duration
            overall_chord_time += len(self.chord_notes) * 4
            current_track += 1
            if current_track >= len(self.tracks_list):
                break

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
                    mf.addNote(track_harmonies[k], channel_harmonies,
                               pitch, measure_time, duration, chord_volume)

                    measure_time += duration
                    last_pitch = pitch

            # write it to disk
            fullFileName = self.folder_location + \
                self.file_location + self.file_name + ".mid"
            f = open(fullFileName, 'w')
            f.close()
            with open(fullFileName, 'wb') as outf:
                mf.writeFile(outf)
