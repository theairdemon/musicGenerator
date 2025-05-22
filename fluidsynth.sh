#!/bin/sh
# fluidsynth -a alsa -m alsa_seq soundfonts/1_FantasyPiano.sf2 midi_files/album_2/cyberpunk_2/fullSong.mid 
fluidsynth -a alsa -m alsa_seq -v -o synth.polyphony=512 soundfonts/1_FantasyPiano.sf2 midi_files/album_2/cyberpunk_2/fullSong.mid 