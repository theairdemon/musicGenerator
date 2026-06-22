#!/bin/bash
# ORDER OF ARGUMENTS - integers that represent the following:
# $1 = chords instrument
# $2 = melody instrument
# $3 = arpeggio instrument
# $4 = synth gain in float (max at like 2.5 i think, min 0.2)
exec >/tmp/test_shell_log.txt 2>&1
cd "/mnt/DATA/Documents/Github/musicGenerator/Version 4 (dev)"
echo "================================================="
echo " RESUME FLUIDSYNTH SONG GENERATION - DEBUG INFO  "
echo "================================================="
echo "Input Args: " $1 $2 $3 $4
echo ""
echo "Building executable C file..."
gcc -I./fluidsynth/include test1.c -L./fluidsynth/build/src -lfluidsynth -lm -lpthread -ldl -o test1
echo "Playing MIDI files through fluidsynth..."
./test1 ../midi_files/app_testing/fullSong.mid $1 $2 $3 $4 &
echo $! >/tmp/test1_pid
