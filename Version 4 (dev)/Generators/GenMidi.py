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
        self.notes_dict = song_dict["notes_dict"]
        self.chord_notes = song_dict["chord_notes"]
        self.harmonies = song_dict["harmonies"]
        self.genre = song_dict["genre"]
        if not tracks_list:
            self.tracks_list = ['melody', 'chords', 'arpeggios']
        else:
            self.tracks_list = tracks_list

    def build(self) -> None:
        # create your MIDI object
        # track_length = 4
        tracks = [i for i in range(len(self.tracks_list))]
        track_harmonies = []
        time = 0
        genre = self.genre.genre
        tempo = self.genre.get('MidiInfo').tempo
        volumes = self.genre.get('MidiInfo').volumes
        
        mf = MIDIFile(len(tracks))
        for i in tracks:
            mf.addTrackName(i, time, self.file_name +
                            "_" + self.tracks_list[i])
            mf.addTempo(i, time, tempo)

        # add some notes
        channel_chords = 0
        channel_melody = 1
        channel_arp = 2

        last_pitch = 0
        current_track = 0
        count_channel = 0
        while "melody" in self.tracks_list[current_track]:
            # MELODY
            current_channel = channel_melody + (count_channel * 3)
            for i in range(0, len(self.melody)):
                measure = self.melody[i]
                measure_time = i * 4
                swing_counter = 0

                for j in range(0, len(measure)):
                    note, duration = measure[j]
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

                    if genre == 'lofi' and duration == 0.5:
                        swing_counter += 1
                        if swing_counter % 2 == 1:
                            duration = 0.67
                        else:
                            duration = 0.33
                    
                    if genre == 'classical':
                        if pitch > 72:
                            pitch -= 12
                    # print(pitch, measure_time, duration)

                    mf.addNote(current_track, current_channel, pitch,
                               measure_time, duration, volumes['melody'])
                    
                    if genre == 'classical':
                        mf.addNote(current_track, current_channel, pitch + 12,
                               measure_time + 1, duration, volumes['melody'])
                        mf.addNote(current_track, current_channel, pitch + 24,
                               measure_time + 2, duration, volumes['melody'])

                    measure_time += duration
                    last_pitch = pitch
            current_track += 1
            count_channel += 1

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
                               chord_time, duration, volumes['chords'])
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
                               chord_time, duration, volumes['arp'])
                    chord_time += duration
            overall_chord_time += len(self.chord_notes) * 4
            current_track += 1
            if current_track >= len(self.tracks_list):
                break

        # write it to disk
        fullFileName = self.folder_location + \
            self.file_location + self.file_name + ".mid"
        f = open(fullFileName, 'w')
        f.close()
        with open(fullFileName, 'wb') as outf:
            mf.writeFile(outf)

# HARMONIES
# Testing, might add back later idk
# for k in range(len(self.harmonies)):
#     for i in range(len(self.harmonies[k])):
#         measure = self.harmonies[k][i]
#         measure_time = i * 4

#         for j in range(len(measure)):
#             note = measure[j][0]
#             pitch1 = self.notes_dict[note][1]
#             pitch2 = self.notes_dict[note][2]
#             pitch3 = self.notes_dict[note][3]

#             dist1 = (pitch1 - last_pitch)**2
#             dist2 = (pitch2 - last_pitch)**2
#             dist3 = (pitch3 - last_pitch)**2
#             distances = [dist1, dist2, dist3]

#             if min(distances) == dist1:
#                 pitch = pitch1
#             elif min(distances) == dist2:
#                 pitch = pitch2
#             else:
#                 pitch = pitch3
#             duration = measure[j][1]
#             mf.addNote(track_harmonies[k], channel_harmonies,
#                         pitch, measure_time, duration, chord_volume)

#             measure_time += duration
#             last_pitch = pitch
