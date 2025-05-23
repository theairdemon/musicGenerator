#!/bin/bash
exec > /tmp/test_shell_log.txt 2>&1
cd "/mnt/DATA/Documents/Github/musicGenerator/Version 4 (dev)"
echo "=================================="
echo "FULL END-TO-END SONG GENERATION"
echo "=================================="
echo ""
echo "Running python MIDI file generation..."
/home/hunter/.pyenv/shims/python3 RunSongGen.py $1 $2 $3
echo ""
echo "Building test1 C file..."
gcc -I./fluidsynth/include test1.c -L./fluidsynth/build/src -lfluidsynth -lm -lpthread -ldl -o test1
echo "Playing MIDI files through fluidsynth..."
./test1 ../midi_files/album_2/fantasy_2/fullSong.mid $4 $5 $6 & echo $! > /tmp/test1_pid