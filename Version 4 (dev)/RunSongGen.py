import random
from midiutil.MidiFile import MIDIFile
from datetime import datetime
import os

# Custom Class Imports
from SongGen import *

# ========= #
# FULL SONG #
# ========= #
def fullSongGen(key, minorKey, folder, song_style, script_dir, startRoot=True):
    song_info_file = "song_info.txt"
    f = open(script_dir + folder + song_info_file, "w")

    song_input_dict = {
        "key": key,
        "style": song_style,
        "length": 4,
        "verses": 1,
        "verse_type": "verse",
        "startRoot": startRoot,
        "genre": "anime",
        "file_name": "verse1",
        "file_location": folder,
        "folder_location": script_dir
    }

    # Writing verse 1 to the folder
    verse1 = SongGeneration(song_input_dict)
    verse1.gen_song()
    f.write("Verse 1\n")
    f.write(str(verse1))

    # Writing chorus to the folder
    song_input_dict["verse_type"] = "chorus"
    song_input_dict["file_name"] = "chorus"
    chorus = SongGeneration(song_input_dict)
    chorus.gen_song()
    f.write("\nChorus\n")
    f.write(str(chorus))

    # Writing verse 2 to the folder
    song_input_dict["verse_type"] = "verse"
    song_input_dict["file_name"] = "verse2"
    verse2 = SongGeneration(song_input_dict)
    verse2.gen_song()
    f.write("\nVerse 2\n")
    f.write(str(verse2))

    # Writing the bridge to the folder
    song_input_dict["length"] = 7
    song_input_dict["verse_type"] = "bridge"
    song_input_dict["file_name"] = "bridge"
    bridge = SongGeneration(song_input_dict)
    bridge.gen_song()
    f.write("\nBridge\n")
    f.write(str(bridge))

    if song_style == "major":
        song_input_dict["key"] = minorKey
        song_input_dict["style"] = "minor"
        song_input_dict["file_name"] = "minorBridge"
        minorBridge = SongGeneration(song_input_dict)
        minorBridge.gen_song()
        f.write("\nMinor Bridge\n")
        f.write(str(minorBridge))

    f.close()


if __name__ == "__main__":
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
    folder = "test_2023_12_2\\"
    song_style = "major"
    startRoot = True
    fullSongGen(key, minorKey, folder, song_style,
                script_dir, startRoot=startRoot)
