from generator import Generate

key_name = 'D'
chord_1 = 'I'
chord_2 = 'V'
chord_3 = 'VI'
chord_4 = 'IV'

percent_16 = 40
percent_8 = 40
percent_4 = 20
percent_2 = 0
percent_1 = 0

song1 = Generate(key_name, chord_1, chord_2, chord_3, chord_4, percent_16, percent_8, percent_4, percent_2, percent_1)

for i in range(0, 32):
    song1.one_measure(i+1)
