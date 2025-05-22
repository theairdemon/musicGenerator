#include <stdio.h>
#include <fluidsynth.h>

/*
Build command: gcc -I./fluidsynth/include test1.c -L./fluidsynth/build/src -lfluidsynth -lm -lpthread -ldl -o test1
Run command: ./test1 ../soundfonts/1_FantasyPiano.sf2 ../midi_files/album_2/cyberpunk_2/fullSong.mid
*/
 
int main(int argc, char** argv) 
{
    int i;
    fluid_settings_t* settings;
    fluid_synth_t* synth;
    fluid_player_t* player;
    fluid_audio_driver_t* adriver;

    // Create then change the settings
    settings = new_fluid_settings();
    fluid_settings_setint(settings, "synth.polyphony", 512);
    // fluid_settings_setint(settings, "synth.verbose", 1);

    synth = new_fluid_synth(settings);
    player = new_fluid_player(synth);

    /* process command line arguments */
    for (i = 1; i < argc; i++) {
        if (fluid_is_soundfont(argv[i])) {
           fluid_synth_sfload(synth, argv[i], 1);
        }
        if (fluid_is_midifile(argv[i])) {
            fluid_player_add(player, argv[i]);
        }
    }

    // Change the player's behavior
    fluid_player_set_tempo(player, FLUID_PLAYER_TEMPO_EXTERNAL_BPM, 110);
    // fluid_player_set_loop(player, -1);

    /* start the synthesizer thread */
    adriver = new_fluid_audio_driver(settings, synth);
    /* play the midi files, if any */
    fluid_player_play(player);
    /* wait for playback termination */
    fluid_player_join(player);
    /* cleanup */
    delete_fluid_audio_driver(adriver);
    delete_fluid_player(player);
    delete_fluid_synth(synth);
    delete_fluid_settings(settings);
    return 0;
}