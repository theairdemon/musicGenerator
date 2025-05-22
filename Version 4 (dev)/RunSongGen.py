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


def printInstruments(track_name, instrument):
    print("Our " + track_name + " will be performed by " +
          instrument + ".")


def fullSongGen(key, minorKey, folder, song_style, genre, script_dir, startRoot=True):
    song_info_file = "song_info.txt"
    f = open(script_dir + folder + song_info_file, "w")

    genreInfo = DefineGenre(genre)
    genreInfo.build()

    # Print out our song info
    print("This is a song in the key of " + key + " " +
          song_style + ", in the genre of " + genre + ".")
    instrumentation = genreInfo.return_dict['Structure'].get_instruments()
    instruments_so_far = set()
    for track_name in (instrumentation.keys()):
        instrument = random.choice(
            list(set(instrumentation[track_name]) - instruments_so_far))
        instruments_so_far.add(instrument)
        printInstruments(track_name, instrument)

    full_song_dict = {
        "file_name": "fullSong",
        "file_location": folder,
        "folder_location": script_dir,
        "melody": [],
        "volumes": [],
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
    midiGenerator = GenMidi(
        full_song_dict,
        tracks_list=genreInfo.return_dict['Structure'].get_tracks())
    midiGenerator.build()

    f.close()


if __name__ == "__main__":
    # os.chdir("/mnt/DATA/Documents/Github/musicGenerator/Version 4 (dev)")
    note_list = ['C', 'C#', 'D', 'D#', 'E',
                 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    styles = ['major', 'minor']
    genres = ['anime', 'classical', 'cyberpunk', 'fantasy', 'lofi']

    key = random.choice(note_list)
    # key = 'D#'
    minorKey = note_list[(note_list.index(key) + 9) % len(note_list)]

    # OTHER PEOPLE: CHANGE THIS LINE FOR YOUR OWN DIRECTORY path
    # script_dir = "D:\\Documents\\Github\\musicGenerator\\midi_files\\album_2\\"
    # folder = "fantasy_2\\"
    # script_dir = os.path.abspath("../midi_files/album_2/")
    script_dir = "/mnt/DATA/Documents/Github/musicGenerator/midi_files/album_2/"
    folder = "fantasy_2/"
    # song_style = "major"
    song_style = random.choice(styles)
    # genre = "fantasy"
    genre = random.choice(genres)
    startRoot = True
    fullSongGen(key, minorKey, folder, song_style,
                genre, script_dir, startRoot=startRoot)
