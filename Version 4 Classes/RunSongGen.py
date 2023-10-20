import random
from midiutil.MidiFile import MIDIFile
from datetime import datetime
import os

# Custom Class Imports
from SongGen import *

note_list = ['C', 'C#', 'D', 'D#', 'E',
             'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
# key = random.choice(note_list)
key = 'E'
minorKey = note_list[(note_list.index(key) + 9) % len(note_list)]
# print(key, minorKey)

# test_song = SongGeneration(key, style='minor', rhythm = [7, 8, 7, 8], length=4, verses=1)
# test_song.gen_song()
# print(test_song.scale)

# OTHER PEOPLE: CHANGE THIS LINE FOR YOUR OWN DIRECTORY path
script_dir = "D:\\Documents\\Github\\musicGenerator\\midi_files\\"
folder = "test_oct_2023_4\\"
song_style = "major"
startRoot = True
fullSongGen(key, minorKey, folder, song_style, script_dir, startRoot=startRoot)
