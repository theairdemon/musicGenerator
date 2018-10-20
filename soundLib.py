import pyaudio
import numpy as np

class SoundLibrary:

    def __init__(self):

        self.volume = 0.1     # range [0.0, 1.0]
        self.fs = 44100       # sampling rate, Hz, must be integer
        concertA = 440.0        # sine frequency, Hz, may be float

        self.quarter = 4.0
        self.eighth = 2.0
        self.sixteenth = 1.0


        ###########################################
        #              Frequencies                #
        ###########################################
        C3Freq = 130.813     # C3 sine frequency (middle c)
        C_sharp3Freq = 138.591
        D3Freq = 146.832     # D3 sine frequency
        E_flat3Freq = 155.563
        E3Freq = 164.814     # E3 sine frequency
        F3Freq = 174.614     # F3 sine frequency
        F_sharp3Freq = 184.997
        G3Freq = 195.998     # G3 sine frequency
        G_sharp3Freq = 207.652
        A3Freq = 220.000     # A3 sine frequency
        B_flat3Freq = 233.082
        B3Freq = 246.942     # B3 sine frequency (concert pitch)

        C4Freq = 261.626     # C4 sine frequency (middle c)
        C_sharp4Freq = 277.183
        D4Freq = 293.665     # D4 sine frequency
        E_flat4Freq = 311.127
        E4Freq = 329.628     # E4 sine frequency
        F4Freq = 349.228     # F4 sine frequency
        F_sharp4Freq = 369.994
        G4Freq = 391.995     # G4 sine frequency
        G_sharp4Freq = 415.305
        A4Freq = 440.000     # A4 sine frequency
        B_flat4Freq = 466.164
        B4Freq = 493.883     # B4 sine frequency (concert pitch)

        C5Freq = 523.251     # C5 sine frequency
        C_sharp5Freq = 554.365
        D5Freq = 587.330     # D5 sine frequency
        E_flat5Freq = 622.254
        E5Freq = 659.255     # E5 sine frequency
        F5Freq = 698.456     # F5 sine frequency
        F_sharp5Freq = 739.989
        G5Freq = 783.991     # G5 sine frequency
        G_sharp5Freq = 830.609
        A5Freq = 880.000     # A5 sine frequency
        B_flat5Freq = 932.328
        B5Freq = 987.767     # B5 sine frequency

        self.Octave34_16 = []
        self.Octave34_8 = []
        self.Octave34_4 = []

        self.Octave45_16 = []
        self.Octave45_8 = []
        self.Octave45_8 = []


        # generate samples, note conversion to float32 array

        ###########################################
        #                Octave 3                 #
        ###########################################
        C3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * C3Freq / self.fs ) ).astype( np.float32 )
        C_sharp3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * C_sharp3Freq / self.fs ) ).astype( np.float32 )
        D3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * D3Freq / self.fs ) ).astype( np.float32 )
        E_flat3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * E_flat3Freq / self.fs ) ).astype( np.float32 )
        E3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * E3Freq / self.fs ) ).astype( np.float32 )
        F3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * F3Freq / self.fs ) ).astype( np.float32 )
        F_sharp3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * F_sharp3Freq / self.fs ) ).astype( np.float32 )
        G3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * G3Freq / self.fs ) ).astype( np.float32 )
        G_sharp3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * G_sharp3Freq / self.fs ) ).astype( np.float32 )
        A3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * A3Freq / self.fs ) ).astype( np.float32 )
        B_flat3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * B_flat3Freq / self.fs ) ).astype( np.float32 )
        B3_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * B3Freq / self.fs ) ).astype( np.float32 )
        Octave3_16 = [C3_16, C_sharp3_16, D3_16, E_flat3_16, E3_16, F3_16, F_sharp3_16, G3_16, G_sharp3_16, A3_16, B_flat3_16, B3_16]

        C3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * C3Freq / self.fs ) ).astype( np.float32 )
        C_sharp3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * C_sharp3Freq / self.fs ) ).astype( np.float32 )
        D3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * D3Freq / self.fs ) ).astype( np.float32 )
        E_flat3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * E_flat3Freq / self.fs ) ).astype( np.float32 )
        E3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * E3Freq / self.fs ) ).astype( np.float32 )
        F3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * F3Freq / self.fs ) ).astype( np.float32 )
        F_sharp3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * F_sharp3Freq / self.fs ) ).astype( np.float32 )
        G3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * G3Freq / self.fs ) ).astype( np.float32 )
        G_sharp3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * G_sharp3Freq / self.fs ) ).astype( np.float32 )
        A3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * A3Freq / self.fs ) ).astype( np.float32 )
        B_flat3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * B_flat3Freq / self.fs ) ).astype( np.float32 )
        B3_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * B3Freq / self.fs ) ).astype( np.float32 )
        Octave3_8 = [C3_8, C_sharp3_8, D3_8, E_flat3_8, E3_8, F3_8, F_sharp3_8, G3_8, G_sharp3_8, A3_8, B_flat3_8, B3_8]

        C3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * C3Freq / self.fs ) ).astype( np.float32 )
        C_sharp3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * C_sharp3Freq / self.fs ) ).astype( np.float32 )
        D3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * D3Freq / self.fs ) ).astype( np.float32 )
        E_flat3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * E_flat3Freq / self.fs ) ).astype( np.float32 )
        E3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * E3Freq / self.fs ) ).astype( np.float32 )
        F3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * F3Freq / self.fs ) ).astype( np.float32 )
        F_sharp3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * F_sharp3Freq / self.fs ) ).astype( np.float32 )
        G3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * G3Freq / self.fs ) ).astype( np.float32 )
        G_sharp3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * G_sharp3Freq / self.fs ) ).astype( np.float32 )
        A3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * A3Freq / self.fs ) ).astype( np.float32 )
        B_flat3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * B_flat3Freq / self.fs ) ).astype( np.float32 )
        B3_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * B3Freq / self.fs ) ).astype( np.float32 )
        Octave3_4 = [C3_4, C_sharp3_4, D3_4, E_flat3_4, E3_4, F3_4, F_sharp3_4, G3_4, G_sharp3_4, A3_4, B_flat3_4, B3_4]


        ###########################################
        #                Octave 4                 #
        ###########################################
        C4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * C4Freq / self.fs ) ).astype( np.float32 )
        C_sharp4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * C_sharp4Freq / self.fs ) ).astype( np.float32 )
        D4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * D4Freq / self.fs ) ).astype( np.float32 )
        E_flat4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * E_flat4Freq / self.fs ) ).astype( np.float32 )
        E4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * E4Freq / self.fs ) ).astype( np.float32 )
        F4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * F4Freq / self.fs ) ).astype( np.float32 )
        F_sharp4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * F_sharp4Freq / self.fs ) ).astype( np.float32 )
        G4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * G4Freq / self.fs ) ).astype( np.float32 )
        G_sharp4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * G_sharp4Freq / self.fs ) ).astype( np.float32 )
        A4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * A4Freq / self.fs ) ).astype( np.float32 )
        B_flat4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * B_flat4Freq / self.fs ) ).astype( np.float32 )
        B4_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * B4Freq / self.fs ) ).astype( np.float32 )
        Octave4_16 = [C4_16, C_sharp4_16, D4_16, E_flat4_16, E4_16, F4_16, F_sharp4_16, G4_16, G_sharp4_16, A4_16, B_flat4_16, B4_16]

        C4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * C4Freq / self.fs ) ).astype( np.float32 )
        C_sharp4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * C_sharp4Freq / self.fs ) ).astype( np.float32 )
        D4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * D4Freq / self.fs ) ).astype( np.float32 )
        E_flat4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * E_flat4Freq / self.fs ) ).astype( np.float32 )
        E4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * E4Freq / self.fs ) ).astype( np.float32 )
        F4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * F4Freq / self.fs ) ).astype( np.float32 )
        F_sharp4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * F_sharp4Freq / self.fs ) ).astype( np.float32 )
        G4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * G4Freq / self.fs ) ).astype( np.float32 )
        G_sharp4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * G_sharp4Freq / self.fs ) ).astype( np.float32 )
        A4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * A4Freq / self.fs ) ).astype( np.float32 )
        B_flat4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * B_flat4Freq / self.fs ) ).astype( np.float32 )
        B4_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * B4Freq / self.fs ) ).astype( np.float32 )
        Octave4_8 = [C4_8, C_sharp4_8, D4_8, E_flat4_8, E4_8, F4_8, F_sharp4_8, G4_8, G_sharp4_8, A4_8, B_flat4_8, B4_8]

        C4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * C4Freq / self.fs ) ).astype( np.float32 )
        C_sharp4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * C_sharp4Freq / self.fs ) ).astype( np.float32 )
        D4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * D4Freq / self.fs ) ).astype( np.float32 )
        E_flat4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * E_flat4Freq / self.fs ) ).astype( np.float32 )
        E4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * E4Freq / self.fs ) ).astype( np.float32 )
        F4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * F4Freq / self.fs ) ).astype( np.float32 )
        F_sharp4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * F_sharp4Freq / self.fs ) ).astype( np.float32 )
        G4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * G4Freq / self.fs ) ).astype( np.float32 )
        G_sharp4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * G_sharp4Freq / self.fs ) ).astype( np.float32 )
        A4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * A4Freq / self.fs ) ).astype( np.float32 )
        B_flat4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * B_flat4Freq / self.fs ) ).astype( np.float32 )
        B4_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * B4Freq / self.fs ) ).astype( np.float32 )
        Octave4_4 = [C4_4, C_sharp4_4, D4_4, E_flat4_4, E4_4, F4_4, F_sharp4_4, G4_4, G_sharp4_4, A4_4, B_flat4_4, B4_4]


        ###########################################
        #                Octave 5                 #
        ###########################################
        C5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * C5Freq / self.fs ) ).astype( np.float32 )
        C_sharp5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * C_sharp5Freq / self.fs ) ).astype( np.float32 )
        D5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * D5Freq / self.fs ) ).astype( np.float32 )
        E_flat5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * E_flat5Freq / self.fs ) ).astype( np.float32 )
        E5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * E5Freq / self.fs ) ).astype( np.float32 )
        F5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * F5Freq / self.fs ) ).astype( np.float32 )
        F_sharp5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * F_sharp5Freq / self.fs ) ).astype( np.float32 )
        G5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * G5Freq / self.fs ) ).astype( np.float32 )
        G_sharp5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * G_sharp5Freq / self.fs ) ).astype( np.float32 )
        A5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * A5Freq / self.fs ) ).astype( np.float32 )
        B_flat5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * B_flat5Freq / self.fs ) ).astype( np.float32 )
        B5_16 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.sixteenth ) * B5Freq / self.fs ) ).astype( np.float32 )
        Octave5_16 = [C5_16, C_sharp5_16, D5_16, E_flat5_16, E5_16, F5_16, F_sharp5_16, G5_16, G_sharp5_16, A5_16, B_flat5_16, B5_16]

        C5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * C5Freq / self.fs ) ).astype( np.float32 )
        C_sharp5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * C_sharp5Freq / self.fs ) ).astype( np.float32 )
        D5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * D5Freq / self.fs ) ).astype( np.float32 )
        E_flat5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * E_flat5Freq / self.fs ) ).astype( np.float32 )
        E5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * E5Freq / self.fs ) ).astype( np.float32 )
        F5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * F5Freq / self.fs ) ).astype( np.float32 )
        F_sharp5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * F_sharp5Freq / self.fs ) ).astype( np.float32 )
        G5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * G5Freq / self.fs ) ).astype( np.float32 )
        G_sharp5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * G_sharp5Freq / self.fs ) ).astype( np.float32 )
        A5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * A5Freq / self.fs ) ).astype( np.float32 )
        B_flat5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * B_flat5Freq / self.fs ) ).astype( np.float32 )
        B5_8 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.eighth ) * B5Freq / self.fs ) ).astype( np.float32 )
        Octave5_8 = [C5_8, C_sharp5_8, D5_8, E_flat5_8, E5_8, F5_8, F_sharp5_8, G5_8, G_sharp5_8, A5_8, B_flat5_8, B5_8]

        C5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * C5Freq / self.fs ) ).astype( np.float32 )
        C_sharp5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * C_sharp5Freq / self.fs ) ).astype( np.float32 )
        D5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * D5Freq / self.fs ) ).astype( np.float32 )
        E_flat5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * E_flat5Freq / self.fs ) ).astype( np.float32 )
        E5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * E5Freq / self.fs ) ).astype( np.float32 )
        F5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * F5Freq / self.fs ) ).astype( np.float32 )
        F_sharp5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * F_sharp5Freq / self.fs ) ).astype( np.float32 )
        G5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * G5Freq / self.fs ) ).astype( np.float32 )
        G_sharp5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * G_sharp5Freq / self.fs ) ).astype( np.float32 )
        A5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * A5Freq / self.fs ) ).astype( np.float32 )
        B_flat5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * B_flat5Freq / self.fs ) ).astype( np.float32 )
        B5_4 = ( np.sin( 2 * np.pi * np.arange( self.fs * self.quarter ) * B5Freq / self.fs ) ).astype( np.float32 )
        Octave5_4 = [C5_4, C_sharp5_4, D5_4, E_flat5_4, E5_4, F5_4, F_sharp5_4, G5_4, G_sharp5_4, A5_4, B_flat5_4, B5_4]


        ###########################################
        #            Composite Scales             #
        ###########################################
        self.Octave34_16 = Octave3_16 + Octave4_16
        self.Octave34_8 = Octave3_8 + Octave4_8
        self.Octave34_4 = Octave3_4 + Octave4_4

        self.Octave45_16 = Octave4_16 + Octave5_16
        self.Octave45_8 = Octave4_8 + Octave5_8
        self.Octave45_4 = Octave4_4 + Octave5_4


    #sum chords, return total value
    def chordSum( self, chordName ):
        self.chordName = chordName

        self.chordBeat = 0
        for i in self.chordName:
            self.chordBeat += i
        return self.chordBeat


    def test_chromatic( self, octave ):
        self.octave = octave

        p = pyaudio.PyAudio()
        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format = pyaudio.paFloat32,
                            channels = 1,
                            rate = self.fs,
                            output = True)
        for note in self.octave:
            beat = note
            stream.write( self.volume * beat )

        stream.stop_stream()
        stream.close()

        p.terminate()

    def playBeat( self, chord, note ):
        self.chord = chord
        self.note = note

        p = pyaudio.PyAudio()
        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format = pyaudio.paFloat32,
                            channels = 1,
                            rate = self.fs,
                            output = True)

        beat = self.chordSum(self.chord) + self.note

        stream.write( self.volume * beat )

        stream.stop_stream()
        stream.close()

        p.terminate()



    #test_chromatic( Octave3_16 )
    #test_chromatic( Octave4_16 )
    #test_chromatic( Octave5_16 )

    #test_chromatic( Octave3_8 )
    #test_chromatic( Octave4_8 )
    #test_chromatic( Octave5_8 )

    #test_chromatic( Octave3_4 )
    #test_chromatic( Octave4_4 )
    #test_chromatic( Octave5_4 )

    #test_chords()
