# musicGenerator
A Python project aimed at making a music generator that creates songs from pure music theory.

## Published Music

["One Small Step"](https://distrokid.com/hyperfollow/huntergallant/one-small-step)
- First album created using this program
- Song setup: verse1-chorus-verse2-chorus-bridge-chorus-chorus
- Tracklist:
	- "No Fear": minor key, arpeggiators, instrumental vocals
	- "Everything is OK": major key, arpeggiators, first track generated
	- "Rain Reflections": major key, arpeggiators, plucked guitar
	- "Deep Breath": minor key, arpeggiators, deleted melody due to bad generation

--- 

# Version History

## Version 4 (dev)
Taking Version 3 and converting it to a series of classes that are imported into our SongGen class, which is then used to build a song using RunSongGen. Also trying to add genre definitions to create various genre tropes.


## Version 3 (stable)
Expanded on Version 2 by pulling the Jupyter notebook into a python file. Cleaned up chord generation and overall improved efficiency, adding a complete "full song generator" that performed successive generations to make all the components of a full song - verses, chords, and bridge (with a minor scale variation for a song that is normally in a major key).

This version, while not feature-rich

## Version 2 (deprecated)
Process:
1. Setup class variables. Key, optional rhythm, optional major/minor, etc.
2. Chords
3. Melody - rhythm
4. Melody - notes
5. MIDI Files

After this, the MIDI files can be placed into a DAW (Digital Audio Workstation), and the musician can select audio effects, instruments, arpeggiators, etc. 

## Version 1 (deprecated)
This contains the code for version 1 of this project. This version is simpler in its music theory applications, while ebing more complex in its actual programming. The Python files in this version generate random notes that follow a set series of chords from a designated key, and generates the sounds as sine waves that are added together and played through a Python library. It is difficult to listen to for long periods of time.
