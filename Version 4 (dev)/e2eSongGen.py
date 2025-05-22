import subprocess



def echo(print_string):
    subprocess.run(["echo", print_string])

setup_echoes = ["==================================",
    "FULL END-TO-END SONG GENERATION",
    "==================================",
    ""]

for s in setup_echoes:
    echo(s)

echo("Running python MIDI file generation...")
subprocess.run(["python", "RunSongGen.py"])

echo("")
echo("Building test1 C file...")
subprocess.run("gcc -I./fluidsynth/include test1.c -L./fluidsynth/build/src -lfluidsynth -lm -lpthread -ldl -o test1".split(" "))
echo("Playing MIDI files through fluidsynth...")
subprocess.run(["./test1", "../soundfonts/1_FantasyPiano.sf2", "../midi_files/album_2/fantasy_2/verse1.mid"])