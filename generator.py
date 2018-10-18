from random import randint, seed


class Generate:

    def __init__(self, key, chord1, chord2, chord3, chord4, percent16, percent8, percent4, percent2, percent1):
        self.key = key
        self.chord1 = chord1
        self.chord2 = chord2
        self.chord3 = chord3
        self.chord4 = chord4

        self.percent16 = percent16
        self.percent8 = percent8
        self.percent4 = percent4
        self.percent2 = percent2
        self.percent1 = percent1

        #                   0       1      2      3       4    5      6       7      8       9      10      11
        self.note_names = ['C', 'C_sharp', 'D', 'E_flat', 'E', 'F', 'F_sharp', 'G', 'G_sharp', 'A', 'B_flat', 'B']
        self.scale = []
        self.chords = [self.chord1, self.chord2, self.chord3, self.chord4]
        self.chord_notes = []

        for i in range(len(self.note_names)):
            if self.key == self.note_names[i]:
                for j in range(i, (len(self.note_names))):
                    if i == j or i + 2 == j or i + 4 == j or i + 5 == j or i + 7 == j or i + 9 == j or i + 11 == j:
                        self.scale.append(self.note_names[j])
                for k in range(0, i):
                    if i - 1 == k or i - 3 == k or i - 5 == k or i - 7 == k or i - 8 == k or i - 10 == k:
                        self.scale.append(self.note_names[k])
                self.scale.append(self.note_names[i])

        for i in range(0, len(self.chords)):
            if self.chords[i] == 'I':
                self.chord_notes.append(self.scale[0])
                self.chord_notes.append(self.scale[2])
                self.chord_notes.append(self.scale[4])
            elif self.chords[i] == 'II':
                self.chord_notes.append(self.scale[1])
                self.chord_notes.append(self.scale[3])
                self.chord_notes.append(self.scale[5])
            elif self.chords[i] == 'III':
                self.chord_notes.append(self.scale[2])
                self.chord_notes.append(self.scale[4])
                self.chord_notes.append(self.scale[6])
            elif self.chords[i] == 'IV':
                self.chord_notes.append(self.scale[0])
                self.chord_notes.append(self.scale[3])
                self.chord_notes.append(self.scale[5])
            elif self.chords[i] == 'V':
                self.chord_notes.append(self.scale[1])
                self.chord_notes.append(self.scale[4])
                self.chord_notes.append(self.scale[6])
            elif self.chords[i] == 'VI':
                self.chord_notes.append(self.scale[0])
                self.chord_notes.append(self.scale[2])
                self.chord_notes.append(self.scale[5])

        print('Scale: ' + str(self.scale))
        print('Chords: ' + str(self.chords))
        print('Notes in Chords: ' + str(self.chord_notes))

    def one_measure(self, measure_num):
        subdivisions = []
        subdivided_name = []
        beats = 1.0

        # determining the subdivisions in the measure
        while beats > 0:
            rand1 = randint(1, 100)

            # 1/16 notes
            if rand1 <= self.percent16:
                note_val = 0.0625
                note_name = '1/16'

                beats -= 2 * note_val

                # append twice to have two 1/16 notes in a row
                subdivisions.append(note_val)
                subdivided_name.append(note_name)
                subdivisions.append(note_val)
                subdivided_name.append(note_name)

            # 1/8 notes
            elif rand1 <= self.percent16 + self.percent8 and beats - 0.125 >= 0:
                note_val = 0.125
                note_name = '1/8'

                if rand1 <= self.percent16 + (0.75 * self.percent8) and beats - 0.25 >= 0:
                    beats -= 2 * note_val

                    # append twice to have two 1/8 notes in a row
                    subdivisions.append(note_val)
                    subdivided_name.append(note_name)
                    subdivisions.append(note_val)
                    subdivided_name.append(note_name)
                else:
                    beats -= note_val

                    subdivisions.append(note_val)
                    subdivided_name.append(note_name)

            # 1/4 notes
            elif rand1 <= self.percent16 + self.percent8 + self.percent4 and beats - 0.25 >= 0:
                note_val = 0.25
                note_name = '1/4'

                beats -= note_val

                subdivisions.append(note_val)
                subdivided_name.append(note_name)

            # 1/2 notes: 5%
            elif rand1 <= self.percent16 + self.percent8 + self.percent4 + self.percent2 and beats - 0.5 >= 0:
                note_val = 0.5
                note_name = '1/2'

                beats -= note_val

                subdivisions.append(note_val)
                subdivided_name.append(note_name)

            # 1/1 notes: 3%
            elif rand1 <= 100 and beats - 1.0 >= 0:
                note_val = 1.0
                note_name = '1/1'

                beats -= note_val

                subdivisions.append(note_val)
                subdivided_name.append(note_name)

            else:
                note_val = 0

                beats -= note_val

        c_num = measure_num % 4 - 1
        if c_num == -1:
            c_num = 3

        rand_start_note = randint(-1, 1)
        s_num = measure_num % 4 + (measure_num % 4 - 1) * 2
        if s_num == 0:
            s_num = 10
        start_note_position = s_num + rand_start_note
        start_note = self.chord_notes[start_note_position]

        print('Measure number: ' + str(measure_num) + ' | ' + 'Chord: ' + str(self.chords[c_num]))
        # print('Note sequence: ' + str(start_note), end=' ')

        new_note = start_note

        note_subdivisions = [str(new_note)]

        # naming the notes
        for i in range(1, len(subdivisions)):
            for note in self.scale:
                if note == new_note:
                    new_note_position = self.scale.index(new_note)
                    rand_new_note = 0
                    while rand_new_note == 0:
                        rand_new_note = randint(-4, 4)
                    if rand_new_note == -4 or rand_new_note == 4:
                        rand_new_note = int(rand_new_note / 2)
                    elif rand_new_note < 0 or rand_new_note > 0:
                        rand_new_note = int(rand_new_note / abs(rand_new_note))
                    new_note_position += rand_new_note
                    if new_note_position >= len(self.scale):
                        new_note_position -= len(self.scale)
                    elif new_note_position < 0:
                        new_note_position += len(self.scale)
                    new_note = self.scale[new_note_position]
                    # print(str(new_note), end=' ')
                    note_subdivisions.append(str(new_note))
                    break
        # print('| Subdivided measure: ' + str(subdivided_name))

        for i in range(0, len(subdivisions)):
            print("   " + subdivided_name[i] + " - " + note_subdivisions[i])
