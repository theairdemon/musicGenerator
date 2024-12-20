# Genres
To better create specific variations among the music that is generation, it makes sense to make different weighted probabilities for a few genres of music, which will hopefully make it easier to feel like that's the type of song we're listening to.

---

## Anime
To me, the *anime* genre means something in-between pop, classical, and indie rock. The primary instrument for the melody would be piano and/or violins, with cellos for the harmonies/chords and woodwinds playing secondary melodies on top.

### Anime - Rhythm
The *anime* genre should rhythmically have some repetition between measures, but it's not a guarantee for every song. Verse-to-verse, we want some differences, but we also want to be able to revist previous rhymic ideas later in the song. I think the most imnportant rhytmic repetition will occur in the first half of the measures; this will tie the structure for each verse together quite nicely. We want the fourth measure to have a smaller probability of repeating, as it should be the end of our "breath" for this verse.

To keep things moving, we don't want any 1/2 notes at all. We can retain 1/16 notes, but they shouldn't appear very frequently. 1/4 and 1/8 notes can appear with the same frequency, since we know we'll be trying to double-up 1/8 notes.

### Anime - Melody
Repetition is desired but not required; whenever we have a repeating rhythm, we should have a decent chance of repeating it exactly, with high probability of at least copying the shape with 'chord' and 'slight' variations. We want movement, and we don't want high jumps between the measures, so we push for having `note_weights` of 1 being the highest.

### Anime - Instrumentation
Woodwinds, piano, strings, and bells. Nothing brassy here, maybe some electronic sounds occasionally.

---

## Classical
The genre of *classical* music has so much variation, so much history, that
 attempting to define it within the bounds of a few paragraphs would be a 
Sisyphean endeavor. Instead, we'll define a general "feeling" of classical 
music, where a song could sound similar to the pop-culture concept of a 
classical piece. For me, this genre of *classical* music could have either long flowing runs, or short, staccato notes - potentially both in the same song. A key component is in the instrumentation; we can have any single instrument (or rotation of instruments) taking the lead melody, but we want a full orchestral mix for harmonies and chords. A suite of pianos, strings, woodwinds, brass, and percussion  instruments will create the sense of space that this genre needs.

### Classical - Rhythm
The more important repetition for the classical *genre* will appear in the melody; but to allow that to flourish, we should have some chance of repeating the first half of measures 1, 2, or 3, in any combination. Of course, this shouldn't be a guarantee, and there will be some variation amongst the generated pieces. In general, we want movement and charisma throughout the piece; thus, less quarter notes and more eighth notes.

### Classical - Melody
This will be one of the most open and flowing melody infos here; keep it loose and open for a wide variety of sounds. Classical is all over the place with the melodies, so let it go wild with the melody.

### Classical - Instrumentation
Keep it light and classy - stick with piano, violins, and woodwinds. If we end up increasing number of chord layers, then maybe add horns as another chords possibility.

---

## Cyberpunk
A difficult and amorphous genre to define, *cyberpunk* in this project will encompass a wide variety of electronic ambient music. Directly inspired by the music of the movie *Blade Runner* and the game *Ghostrunner*, our genre of *cyberpunk* will be synthesizer-heavy with a sturdy percussive backbone. We want ambient, morphing synths for chords (changing in anything but pitch), with a lean towards clean synths for our melody. Slow down the tempo too.

### Cyberpunk - Rhythm 
It's okay to space out the notes, and we don't need much repetition throughout. Maybe we have a medium chance of repeating measures 2/4, but otherwise each measure can stand on its own. We can repeat the first half of measures 2 and 4, we don't need repetition elsewhere. The notes that we want to be played quickly will be repetitive arpeggios, so our "main" rhythm should be slower, for better atmosphere and ambience.

### Cyberpunk - Melody
We want pretty solid chord melodies here; nothing too off the beaten path. Maybe a small chance of inverted repetition, but mostly just focusing on pulling notes around to the relative chords. 

### Cyberpunk - Instrumentation
Synths, synths, synths! Can use strings as chord layers, but primarily will be using synths from various VSTs.

---

## Fantasy
Powerful strings, deep horns, beautiful flutes; this *fantasy* genre evokes images of riding across vast plains, setting sail into a glorious sunset, or otherwise beginning to weave a tale of magic and wonder. We want notes to flow naturally from one another, like a stream in an elven forest. 

### Fantasy - Rhythm
The fantasy rhythm is similar to cyberpunk in how it can be a bit slower than others, but we still want the ability for openness and flowing sounds like in anime. Fantasy will differ more from anime in its ambience and instrumentation (covered below). We certainly want rhythms to be repeated sometimes.

## Fantasy - Melody
Definitely high chances of repeated melodies here! Tying back into the rhythm, we want to only have half-measures that are repeated, so we can be more "perfect" than with other genres. More so than in any other genre, fantasy should try and build out leitmotifs in the song.

### Fantasy - Instrumentation
Horns, woodwinds, bells, strings, violin, flute; these are work excellent for fantasy music! Possibly even include drums for the arps too, something to think about.

---

## Lofi
This should be much, *much* slower than other genres. Spacing and slow notes are the name of the game here; conbine with pianos, guitars, and synth pads for optimal impact. Add in a vinyl record overlay, and this is a golden song. 

### Lofi - Rhythm
Unlike the others so far, lofi is a great genre for having exact repetition. I think there should be some solid full measures-worth of repetition for sure, and high chances of repetition elsewhere.

### Lofi - Melody
Lots of repetition here as well! Definitely high probability of perfect repetition.

### Lofi - Instrumentation
Mostly piano and synths, with vinyl filter on top of that.