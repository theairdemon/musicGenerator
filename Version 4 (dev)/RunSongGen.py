import random
from midiutil.MidiFile import MIDIFile
from datetime import datetime
import os

# Custom Class Imports
from SongGen import *
from Generators.GenMidi import GenMidi
from Genres.DefineGenre import DefineGenre

# ========= #
# FULL SONG #
# ========= #


def fullSongGen(key, minorKey, folder, song_style, genre, script_dir, startRoot=True):
    song_info_file = "song_info.txt"
    f = open(script_dir + folder + song_info_file, "w")

    genreInfo = DefineGenre(genre)
    genreInfo.build()

    full_song_dict = {
        "file_name": "fullSong",
        "file_location": folder,
        "folder_location": script_dir,
        "melody": [],
        "notes_dict": {},
        "verses": 1,
        "chord_notes": [],
        "harmonies": []
    }

    song_input_dict = {
        "key": key,
        "style": song_style,
        "length": 4,
        "verses": 1,
        "verse_type": "verse",
        "startRoot": startRoot,
        "genre": genreInfo,
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

    # Writing chorus to the folder
    song_input_dict["verse_type"] = "chorus"
    song_input_dict["file_name"] = "baseMeasure"
    base_measure = SongGeneration(song_input_dict)
    base_measure.gen_base_measure()

    if song_style == "major":
        song_input_dict["key"] = minorKey
        song_input_dict["style"] = "minor"
        song_input_dict["file_name"] = "minorBridge"
        minorBridge = SongGeneration(song_input_dict)
        minorBridge.gen_song()
        f.write("\nMinor Bridge\n")
        f.write(str(minorBridge))

    # Build our full song, start to finish, one midi file
    for part in genreInfo.get('Structure').getOrderList():
        if part == "verse1":
            full_song_dict = verse1.add_SongDict(full_song_dict)
        elif part == "verse2":
            full_song_dict = verse2.add_SongDict(full_song_dict)
        elif part == "bridge":
            full_song_dict = bridge.add_SongDict(full_song_dict)
            full_song_dict = base_measure.add_SongDict(full_song_dict)
        elif part == "chorus":
            full_song_dict = chorus.add_SongDict(full_song_dict)
        elif part == "finalChorus":
            full_song_dict = chorus.add_SongDict(full_song_dict)
            full_song_dict = base_measure.add_SongDict(full_song_dict)
    midiGenerator = GenMidi(full_song_dict)
    midiGenerator.build()

    f.close()


if __name__ == "__main__":
    note_list = ['C', 'C#', 'D', 'D#', 'E',
                 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    # key = random.choice(note_list)
    key = 'D#'
    minorKey = note_list[(note_list.index(key) + 9) % len(note_list)]

    # OTHER PEOPLE: CHANGE THIS LINE FOR YOUR OWN DIRECTORY path
    script_dir = "D:\\Documents\\Github\\musicGenerator\\midi_files\\"
    folder = "test_2024_11_3\\"
    song_style = "major"
    genre = "anime"
    startRoot = True
    fullSongGen(key, minorKey, folder, song_style,
                genre, script_dir, startRoot=startRoot)
