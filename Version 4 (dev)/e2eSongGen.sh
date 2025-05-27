#!/bin/bash
# ORDER OF ARGUMENTS - integers that represent the following:
# $1 = key (C, C3, etc)
# $2 = genre (anime, fantasy, etc)
# $3 = style (major or minor)
# $4 = chords instrument
# $5 = melody instrument
# $6 = arpeggio instrument
# $7 = synth gain in float (max at like 2.5 i think, min 0.2)
exec > /tmp/test_shell_log.txt 2>&1
cd "/mnt/DATA/Documents/Github/musicGenerator/Version 4 (dev)"
echo "================================================"
echo "  FULL END-TO-END SONG GENERATION - DEBUG INFO  "
echo "================================================"
echo "Input Args: " $1 $2 $3 $4 $5 $6 $7
echo ""
echo "Running MIDI file generation..."
/home/hunter/.pyenv/shims/python3 RunSongGen.py $1 $2 $3
echo ""
echo "Building executable C file..."
gcc -I./fluidsynth/include test1.c -L./fluidsynth/build/src -lfluidsynth -lm -lpthread -ldl -o test1
echo "Playing MIDI files through fluidsynth..."
./test1 ../midi_files/app_testing/fullSong.mid $4 $5 $6 $7 & echo $! > /tmp/test1_pid