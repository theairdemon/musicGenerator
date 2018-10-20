import pyaudio
import numpy as np

class SoundLibrary:

    def __init__(self, key):
        self.key = key

        volume = 0.1     # range [0.0, 1.0]
        fs = 44100       # sampling rate, Hz, must be integer
        durationChord = 8.0   # in seconds, may be float
        concertA = 440.0        # sine frequency, Hz, may be float

        durationNotes = 2.0
        durationLastNote = 4.0

        BPM = 120
        quarter = 1.0
        eighth = 0.5
        sixteenth = 0.25


        ###########################################
        #              Frequencies                #
        ###########################################
        c3Freq = 130.813     # c3 sine frequency (middle c)
        cSharp3Freq = 138.591
        d3Freq = 146.832     # d3 sine frequency
        dSharp3Freq = 155.563
        e3Freq = 164.814     # e3 sine frequency
        f3Freq = 174.614     # f3 sine frequency
        fSharp3Freq = 184.997
        g3Freq = 195.998     # g3 sine frequency
        gSharp3Freq = 207.652
        a3Freq = 220.000     # a3 sine frequency
        aSharp3Freq = 233.082
        b3Freq = 246.942     # b3 sine frequency (concert pitch)

        c4Freq = 261.626     # c4 sine frequency (middle c)
        cSharp4Freq = 277.183
        d4Freq = 293.665     # d4 sine frequency
        dSharp4Freq = 311.127
        e4Freq = 329.628     # e4 sine frequency
        f4Freq = 349.228     # f4 sine frequency
        fSharp4Freq = 369.994
        g4Freq = 391.995     # g4 sine frequency
        gSharp4Freq = 415.305
        a4Freq = 440.000     # a4 sine frequency
        aSharp4Freq = 466.164
        b4Freq = 493.883     # b4 sine frequency (concert pitch)

        c5Freq = 523.251     # c5 sine frequency
        cSharp5Freq = 554.365
        d5Freq = 587.330     # d5 sine frequency
        dSharp5Freq = 622.254
        e5Freq = 659.255     # e5 sine frequency
        f5Freq = 698.456     # f5 sine frequency
        fSharp5Freq = 739.989
        g5Freq = 783.991     # g5 sine frequency
        gSharp5Freq = 830.609
        a5Freq = 880.000     # a5 sine frequency
        aSharp5Freq = 932.328
        b5Freq = 987.767     # b5 sine frequency




        # generate samples, note conversion to float32 array

        ###########################################
        #                Octave 3                 #
        ###########################################
        c3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * c3Freq / fs ) ).astype( np.float32 )
        cSharp3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * cSharp3Freq / fs ) ).astype( np.float32 )
        d3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * d3Freq / fs ) ).astype( np.float32 )
        dSharp3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * dSharp3Freq / fs ) ).astype( np.float32 )
        e3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * e3Freq / fs ) ).astype( np.float32 )
        f3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * f3Freq / fs ) ).astype( np.float32 )
        fSharp3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * fSharp3Freq / fs ) ).astype( np.float32 )
        g3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * g3Freq / fs ) ).astype( np.float32 )
        gSharp3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * gSharp3Freq / fs ) ).astype( np.float32 )
        a3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * a3Freq / fs ) ).astype( np.float32 )
        aSharp3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * aSharp3Freq / fs ) ).astype( np.float32 )
        b3_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * b3Freq / fs ) ).astype( np.float32 )
        Octave3_16 = [c3_16, cSharp3_16, d3_16, dSharp3_16, e3_16, f3_16, fSharp3_16, g3_16, gSharp3_16, a3_16, aSharp3_16, b3_16]

        c3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * c3Freq / fs ) ).astype( np.float32 )
        cSharp3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * cSharp3Freq / fs ) ).astype( np.float32 )
        d3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * d3Freq / fs ) ).astype( np.float32 )
        dSharp3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * dSharp3Freq / fs ) ).astype( np.float32 )
        e3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * e3Freq / fs ) ).astype( np.float32 )
        f3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * f3Freq / fs ) ).astype( np.float32 )
        fSharp3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * fSharp3Freq / fs ) ).astype( np.float32 )
        g3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * g3Freq / fs ) ).astype( np.float32 )
        gSharp3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * gSharp3Freq / fs ) ).astype( np.float32 )
        a3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * a3Freq / fs ) ).astype( np.float32 )
        aSharp3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * aSharp3Freq / fs ) ).astype( np.float32 )
        b3_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * b3Freq / fs ) ).astype( np.float32 )
        Octave3_8 = [c3_8, cSharp3_8, d3_8, dSharp3_8, e3_8, f3_8, fSharp3_8, g3_8, gSharp3_8, a3_8, aSharp3_8, b3_8]

        c3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * c3Freq / fs ) ).astype( np.float32 )
        cSharp3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * cSharp3Freq / fs ) ).astype( np.float32 )
        d3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * d3Freq / fs ) ).astype( np.float32 )
        dSharp3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * dSharp3Freq / fs ) ).astype( np.float32 )
        e3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * e3Freq / fs ) ).astype( np.float32 )
        f3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * f3Freq / fs ) ).astype( np.float32 )
        fSharp3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * fSharp3Freq / fs ) ).astype( np.float32 )
        g3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * g3Freq / fs ) ).astype( np.float32 )
        gSharp3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * gSharp3Freq / fs ) ).astype( np.float32 )
        a3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * a3Freq / fs ) ).astype( np.float32 )
        aSharp3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * aSharp3Freq / fs ) ).astype( np.float32 )
        b3_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * b3Freq / fs ) ).astype( np.float32 )
        Octave3_4 = [c3_4, cSharp3_4, d3_4, dSharp3_4, e3_4, f3_4, fSharp3_4, g3_4, gSharp3_4, a3_4, aSharp3_4, b3_4]


        ###########################################
        #                Octave 4                 #
        ###########################################
        c4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * c4Freq / fs ) ).astype( np.float32 )
        cSharp4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * cSharp4Freq / fs ) ).astype( np.float32 )
        d4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * d4Freq / fs ) ).astype( np.float32 )
        dSharp4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * dSharp4Freq / fs ) ).astype( np.float32 )
        e4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * e4Freq / fs ) ).astype( np.float32 )
        f4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * f4Freq / fs ) ).astype( np.float32 )
        fSharp4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * fSharp4Freq / fs ) ).astype( np.float32 )
        g4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * g4Freq / fs ) ).astype( np.float32 )
        gSharp4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * gSharp4Freq / fs ) ).astype( np.float32 )
        a4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * a4Freq / fs ) ).astype( np.float32 )
        aSharp4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * aSharp4Freq / fs ) ).astype( np.float32 )
        b4_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * b4Freq / fs ) ).astype( np.float32 )
        Octave4_16 = [c4_16, cSharp4_16, d4_16, dSharp4_16, e4_16, f4_16, fSharp4_16, g4_16, gSharp4_16, a4_16, aSharp4_16, b4_16]

        c4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * c4Freq / fs ) ).astype( np.float32 )
        cSharp4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * cSharp4Freq / fs ) ).astype( np.float32 )
        d4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * d4Freq / fs ) ).astype( np.float32 )
        dSharp4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * dSharp4Freq / fs ) ).astype( np.float32 )
        e4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * e4Freq / fs ) ).astype( np.float32 )
        f4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * f4Freq / fs ) ).astype( np.float32 )
        fSharp4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * fSharp4Freq / fs ) ).astype( np.float32 )
        g4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * g4Freq / fs ) ).astype( np.float32 )
        gSharp4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * gSharp4Freq / fs ) ).astype( np.float32 )
        a4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * a4Freq / fs ) ).astype( np.float32 )
        aSharp4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * aSharp4Freq / fs ) ).astype( np.float32 )
        b4_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * b4Freq / fs ) ).astype( np.float32 )
        Octave4_8 = [c4_8, cSharp4_8, d4_8, dSharp4_8, e4_8, f4_8, fSharp4_8, g4_8, gSharp4_8, a4_8, aSharp4_8, b4_8]

        c4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * c4Freq / fs ) ).astype( np.float32 )
        cSharp4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * cSharp4Freq / fs ) ).astype( np.float32 )
        d4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * d4Freq / fs ) ).astype( np.float32 )
        dSharp4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * dSharp4Freq / fs ) ).astype( np.float32 )
        e4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * e4Freq / fs ) ).astype( np.float32 )
        f4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * f4Freq / fs ) ).astype( np.float32 )
        fSharp4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * fSharp4Freq / fs ) ).astype( np.float32 )
        g4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * g4Freq / fs ) ).astype( np.float32 )
        gSharp4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * gSharp4Freq / fs ) ).astype( np.float32 )
        a4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * a4Freq / fs ) ).astype( np.float32 )
        aSharp4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * aSharp4Freq / fs ) ).astype( np.float32 )
        b4_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * b4Freq / fs ) ).astype( np.float32 )
        Octave4_4 = [c4_4, cSharp4_4, d4_4, dSharp4_4, e4_4, f4_4, fSharp4_4, g4_4, gSharp4_4, a4_4, aSharp4_4, b4_4]


        ###########################################
        #                Octave 5                 #
        ###########################################
        c5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * c5Freq / fs ) ).astype( np.float32 )
        cSharp5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * cSharp5Freq / fs ) ).astype( np.float32 )
        d5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * d5Freq / fs ) ).astype( np.float32 )
        dSharp5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * dSharp5Freq / fs ) ).astype( np.float32 )
        e5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * e5Freq / fs ) ).astype( np.float32 )
        f5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * f5Freq / fs ) ).astype( np.float32 )
        fSharp5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * fSharp5Freq / fs ) ).astype( np.float32 )
        g5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * g5Freq / fs ) ).astype( np.float32 )
        gSharp5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * gSharp5Freq / fs ) ).astype( np.float32 )
        a5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * a5Freq / fs ) ).astype( np.float32 )
        aSharp5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * aSharp5Freq / fs ) ).astype( np.float32 )
        b5_16 = ( np.sin( 2 * np.pi * np.arange( fs * sixteenth ) * b5Freq / fs ) ).astype( np.float32 )
        Octave5_16 = [c5_16, cSharp5_16, d5_16, dSharp5_16, e5_16, f5_16, fSharp5_16, g5_16, gSharp5_16, a5_16, aSharp5_16, b5_16]

        c5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * c5Freq / fs ) ).astype( np.float32 )
        cSharp5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * cSharp5Freq / fs ) ).astype( np.float32 )
        d5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * d5Freq / fs ) ).astype( np.float32 )
        dSharp5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * dSharp5Freq / fs ) ).astype( np.float32 )
        e5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * e5Freq / fs ) ).astype( np.float32 )
        f5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * f5Freq / fs ) ).astype( np.float32 )
        fSharp5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * fSharp5Freq / fs ) ).astype( np.float32 )
        g5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * g5Freq / fs ) ).astype( np.float32 )
        gSharp5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * gSharp5Freq / fs ) ).astype( np.float32 )
        a5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * a5Freq / fs ) ).astype( np.float32 )
        aSharp5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * aSharp5Freq / fs ) ).astype( np.float32 )
        b5_8 = ( np.sin( 2 * np.pi * np.arange( fs * eighth ) * b5Freq / fs ) ).astype( np.float32 )
        Octave5_8 = [c5_8, cSharp5_8, d5_8, dSharp5_8, e5_8, f5_8, fSharp5_8, g5_8, gSharp5_8, a5_8, aSharp5_8, b5_8]

        c5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * c5Freq / fs ) ).astype( np.float32 )
        cSharp5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * cSharp5Freq / fs ) ).astype( np.float32 )
        d5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * d5Freq / fs ) ).astype( np.float32 )
        dSharp5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * dSharp5Freq / fs ) ).astype( np.float32 )
        e5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * e5Freq / fs ) ).astype( np.float32 )
        f5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * f5Freq / fs ) ).astype( np.float32 )
        fSharp5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * fSharp5Freq / fs ) ).astype( np.float32 )
        g5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * g5Freq / fs ) ).astype( np.float32 )
        gSharp5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * gSharp5Freq / fs ) ).astype( np.float32 )
        a5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * a5Freq / fs ) ).astype( np.float32 )
        aSharp5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * aSharp5Freq / fs ) ).astype( np.float32 )
        b5_4 = ( np.sin( 2 * np.pi * np.arange( fs * quarter ) * b5Freq / fs ) ).astype( np.float32 )
        Octave5_4 = [c5_4, cSharp5_4, d5_4, dSharp5_4, e5_4, f5_4, fSharp5_4, g5_4, gSharp5_4, a5_4, aSharp5_4, b5_4]


        ###########################################
        #                 Chords                  #
        ###########################################
        chordI = [c3_8, e3_8, g3_8]
        chordII = [d3_8, f3_8, a3_8]
        chordIII = [e3_8, g3_8, b3_8]
        chordIV = [c3_8, f3_8, a3_8]
        chordV = [d3_8, g3_8, b3_8]
        chordVI = [c3_8, e3_8, a3_8]

    #sum chords, return total value
    def chordSum( chordName ):
        chordBeat = 0
        for i in chordName:
            chordBeat += i
        return chordBeat


    def test_chromatic( octave ):
        p = pyaudio.PyAudio()
        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format = pyaudio.paFloat32,
                            channels = 1,
                            rate = fs,
                            output = True)
        for note in octave:
            beat = note
            stream.write( volume * beat )

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
