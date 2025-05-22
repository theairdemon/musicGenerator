#!/bin/bash
echo "Building test1 C file..."
gcc -I./fluidsynth/include test1.c -L./fluidsynth/build/src -lfluidsynth -lm -lpthread -ldl -o test1
echo "Playing MIDI files through fluidsynth..."
./test1 ../soundfonts/1_FantasyPiano.sf2 ../midi_files/album_2/fantasy_2/fullSong.mid