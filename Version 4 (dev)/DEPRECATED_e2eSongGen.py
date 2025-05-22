import subprocess

def echo(print_string):
    subprocess.run(["echo", print_string])

setup_echoes = ["==================================",
    "FULL END-TO-END SONG GENERATION",
    "==================================",
    ""]

for s in setup_echoes:
    echo(s)

project_path = "/mnt/DATA/Documents/Github/musicGenerator/Version 4 (dev)"

echo("Running python MIDI file generation...")
subprocess.run(["python", "RunSongGen.py"], cwd = project_path)

echo("")
echo("Building test1 C file...")
subprocess.run("gcc -I./fluidsynth/include test1.c -L./fluidsynth/build/src -lfluidsynth -lm -lpthread -ldl -o test1".split(" "), cwd = project_path)
echo("Playing MIDI files through fluidsynth...")
subprocess.run(["./test1", "../soundfonts/1_FantasyPiano.sf2", "../midi_files/album_2/fantasy_2/fullSong.mid"], cwd = project_path)