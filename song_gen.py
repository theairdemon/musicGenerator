from generator import Generate

key_name = 'G'
chord_1 = 'II'
chord_2 = 'VI'
chord_3 = 'I'
chord_4 = 'V'

percent_16 = 20
percent_8 = 40
percent_4 = 40
percent_2 = 0
percent_1 = 0

song1 = Generate(key_name, chord_1, chord_2, chord_3, chord_4, percent_16, percent_8, percent_4, percent_2, percent_1)

for i in range(0, 16):
    song1.one_measure(i+1)
