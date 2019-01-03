from generator import Generate

key_name = 'D'

epic_chords1 = ['II', 'VI', 'I', 'V']

four_chords1 = ['I', 'V', 'VI', 'IV']
four_chords2 = ['VI', 'IV', 'I', 'V']

songChords = []

for i in epic_chords1:
    songChords.append(i) 

percent_16 = 10
percent_8 = 40
percent_4 = 50
percent_2 = 0
percent_1 = 0

song1 = Generate(key_name, songChords[0], songChords[1],songChords[2], songChords[3], percent_16, percent_8, percent_4, percent_2, percent_1)

for i in range(0, 256):
    song1.one_measure(i+1)
