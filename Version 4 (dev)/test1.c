#include <stdio.h>
#include <stdlib.h>
#include <fluidsynth.h>
#include <fluidsynth/sfont.h>

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
    // fluid_settings_setint(settings, "audio.thread-priority", 0);
    // fluid_settings_setint(settings, "synth.verbose", 1);

    synth = new_fluid_synth(settings);
    player = new_fluid_player(synth);

    /* process command line arguments */
    /*
    argv[1] - midifile
    argv[2] - chord instrument
    argv[3] - melody instrument
    argv[4] - arpeggio instrument
    */ 
    if (fluid_is_midifile(argv[1])) {
        fluid_player_add(player, argv[1]);
    }

    int default_instruments[3] = {2, 0, 3};

    // Define instruments, if they're defined in the args
    if (argc > 2) {
        default_instruments[0] = atoi(argv[2]);
    }
    if (argc > 3) {
        default_instruments[1] = atoi(argv[3]);
    }
    if (argc > 4) {
        default_instruments[2] = atoi(argv[4]);
    }

    int synth_array[5] = {fluid_synth_sfload(synth, "/mnt/DATA/Documents/Github/musicGenerator/soundfonts/1115_Alaska.sf2", 1),
        fluid_synth_sfload(synth, "/mnt/DATA/Documents/Github/musicGenerator/soundfonts/1_FantasyPiano.sf2", 1),
        fluid_synth_sfload(synth, "/mnt/DATA/Documents/Github/musicGenerator/soundfonts/198_u20_alto_sax.SF2", 1),
        fluid_synth_sfload(synth, "/mnt/DATA/Documents/Github/musicGenerator/soundfonts/336_Massive_strings.sf2",  1),
        fluid_synth_sfload(synth, "/mnt/DATA/Documents/Github/musicGenerator/soundfonts/LustyVoices.sf2",  1)
    };

    fluid_synth_sfont_select  (synth, 0, synth_array[default_instruments[0]]);
    fluid_synth_program_select(synth, 0, synth_array[default_instruments[0]], 0, 0);

    fluid_synth_sfont_select  (synth, 1, synth_array[default_instruments[1]]);      
    fluid_synth_program_select(synth, 1, synth_array[default_instruments[1]], 0, 0);

    fluid_synth_sfont_select  (synth, 2, synth_array[default_instruments[2]]);      
    fluid_synth_program_select(synth, 2, synth_array[default_instruments[2]], 0, 0);

    // Change the player's behavior

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

    // Can copy/paste back after synths are defined if we want debugging logs
    // int sfcount = fluid_synth_sfcount(synth);
    // for (int si = 0; si < sfcount; si++) {
    //     fluid_sfont_t* sfont = fluid_synth_get_sfont(synth, si);
    //     if (!sfont) continue;

    //     int sfid = fluid_sfont_get_id(sfont);
    //     printf("SoundFont #%d (ID %d) presets:\n", si, sfid);

    //     // Iterate presets
    //     fluid_sfont_iteration_start(sfont);
    //     fluid_preset_t* preset;
    //     while ((preset = fluid_sfont_iteration_next(sfont)) != NULL) {
    //         int bank = fluid_preset_get_banknum(preset);
    //         int prog = fluid_preset_get_num(preset);
    //         const char* name = fluid_preset_get_name(preset);
    //         printf("  bank %3d, prog %3d → %s\n", bank, prog, name);
    //     }
    // }