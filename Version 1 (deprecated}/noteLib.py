import pyaudio
import numpy as np
from soundLib import SoundLibrary

class NoteLibrary:

    def __init__(self, key, chord1, chord2, chord3, chord4):
        self.key = key
        self.chord1 = chord1
        self.chord2 = chord2
        self.chord3 = chord3
        self.chord4 = chord4

        self.sampleLib = SoundLibrary()

        ###########################################
        #                Key Value                #
        ###########################################
        if self.key == "C": self.keyValue = 0
        elif self.key == "C_sharp": self.keyValue = 1
        elif self.key == "D": self.keyValue = 2
        elif self.key == "E_flat": self.keyValue = 3
        elif self.key == "E": self.keyValue = 4
        elif self.key == "F": self.keyValue = 5
        elif self.key == "F_sharp": self.keyValue = 6
        elif self.key == "G": self.keyValue = 7
        elif self.key == "G_sharp": self.keyValue = 8
        elif self.key =="A": self.keyValue = 9
        elif self.key == "B_flat": self.keyValue = 10
        elif self.key == "B": self.keyValue = 11

        #set starting value of scales
        self.scale34_16 = self.sampleLib.Octave34_16[ self.keyValue : ]
        self.scale34_8 = self.sampleLib.Octave34_8[ self.keyValue : ]
        self.scale34_4 = self.sampleLib.Octave34_4[ self.keyValue : ]

        self.scale45_16 = self.sampleLib.Octave45_16[ self.keyValue : ]
        self.scale45_8 = self.sampleLib.Octave45_8[ self.keyValue : ]
        self.scale45_4 = self.sampleLib.Octave45_4[ self.keyValue : ]

        #divide into an actual key
        self.key34_16 = [self.scale34_16[0], self.scale34_16[2], self.scale34_16[4], self.scale34_16[5], self.scale34_16[7], self.scale34_16[9], self.scale34_16[11]]
        self.key34_8 = [self.scale34_8[0], self.scale34_8[2], self.scale34_8[4], self.scale34_8[5], self.scale34_8[7], self.scale34_8[9], self.scale34_8[11]]
        self.key34_4 = [self.scale34_4[0], self.scale34_4[2], self.scale34_4[4], self.scale34_4[5], self.scale34_4[7], self.scale34_4[9], self.scale34_4[11]]

        self.key45_16 = [self.scale45_16[0], self.scale45_16[2], self.scale45_16[4], self.scale45_16[5], self.scale45_16[7], self.scale45_16[9], self.scale45_16[11]]
        self.key45_8 = [self.scale45_8[0], self.scale45_8[2], self.scale45_8[4], self.scale45_8[5], self.scale45_8[7], self.scale45_8[9], self.scale45_8[11]]
        self.key45_4 = [self.scale45_4[0], self.scale45_4[2], self.scale45_4[4], self.scale45_4[5], self.scale45_4[7], self.scale45_4[9], self.scale45_4[11]]


        #useful for the music playing down below
        self.note_names = ['C', 'C_sharp', 'D', 'E_flat', 'E', 'F', 'F_sharp', 'G', 'G_sharp', 'A', 'B_flat', 'B']
        self.noteScale = []

        for i in range(len(self.note_names)):
            if self.key == self.note_names[i]:
                for j in range(i, (len(self.note_names))):
                    if i == j or i + 2 == j or i + 4 == j or i + 5 == j or i + 7 == j or i + 9 == j or i + 11 == j:
                        self.noteScale.append(self.note_names[j])
                for k in range(0, i):
                    if i - 1 == k or i - 3 == k or i - 5 == k or i - 7 == k or i - 8 == k or i - 10 == k:
                        self.noteScale.append(self.note_names[k])


    ###########################################
    #            Play some music!!            #
    ###########################################
    def testPlay(self):
        self.sampleLib.test_chromatic(self.sampleLib.Octave34_4)

    def playNote( self, chordNum, noteName, subdivision ):
        self.chordNum = chordNum
        self.noteName = noteName
        self.subdivision = subdivision
        #first, get chord number and notes
        self.newChord = self.getChordWithSubdivision( self.chordNum, self.subdivision)

        #then, get note name and value, according to subdivision
        self.newNote = self.getNoteWithSubdivision( self.noteName, self.subdivision )

        #finally, play the beat using playBeat( chord, note )
        self.sampleLib.playBeat( self.newChord, self.newNote )

    #chord instructions
    def getChordWithSubdivision( self, chordNumber2, subdivisionNum ):
        self.chordNumber2 = chordNumber2
        self.subdivisionNum = subdivisionNum
        if self.subdivisionNum == '1/16':
            return self.getChordNotes( self.chordNumber2, self.key34_16 )
        elif self.subdivisionNum == '1/8':
            return self.getChordNotes( self.chordNumber2, self.key34_8 )
        elif self.subdivisionNum == '1/4':
            return self.getChordNotes( self.chordNumber2, self.key34_4 )

    def getChordNotes( self, chordNumber3, chordArray ):
        self.chordNumber3 = chordNumber3
        self.chordArray = chordArray

        if self.chordNumber3 == 'I':
            return [self.chordArray[0], self.chordArray[2], self.chordArray[4]]
        elif self.chordNumber3 == 'II':
            return [self.chordArray[1], self.chordArray[3], self.chordArray[5]]
        elif self.chordNumber3 == 'III':
            return [self.chordArray[2], self.chordArray[4], self.chordArray[6]]
        elif self.chordNumber3 == 'IV':
            return [self.chordArray[0], self.chordArray[3], self.chordArray[5]]
        elif self.chordNumber3 == 'V':
            return [self.chordArray[1], self.chordArray[4], self.chordArray[6]]
        elif self.chordNumber3 == 'VI':
            return [self.chordArray[0], self.chordArray[2], self.chordArray[5]]

    #note instructions
    def getNoteWithSubdivision( self, noteName2, subdivisionNum2 ):
        self.noteName2 = noteName2
        self.subdivisionNum2 = subdivisionNum2

        if self.subdivisionNum2 == '1/16':
            return self.getNotes( self.noteName2, self.key45_16 )
        elif self.subdivisionNum2 == '1/8':
            return self.getNotes( self.noteName2, self.key45_8 )
        elif self.subdivisionNum2 == '1/4':
            return self.getNotes( self.noteName2, self.key45_4 )

    def getNotes( self, noteName3, noteArray ):
        self.noteName3 = noteName3
        self.noteArray = noteArray

        return self.noteArray[self.noteScale.index(self.noteName3)]
