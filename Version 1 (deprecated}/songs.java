package music;

import org.jfugue.*;

public class songs {
	public static void main(String[] args) 	 {
		/*
		//I'm Blue
		for (int i = 0; i < 10; i++){
			Player player = new Player();
			Pattern pattern = new Pattern("KBbmaj I[54] A6q B6i D6i G6i B6i C7i F6i A6i B6q G6i B6i D7i E7i G6i D7i C7i B6i D6i G6i B6i C7i F6i A6i B6q G6i B6i D7i E7i G6i D7i C7i B6i D6i G6i B6i C7i F6i A6i B6q G6i B6i D7i E7i G6i D7i C7i B6i D6i G6i B6i A6i C6i F6i G6q C6i F6i G6q");
			player.play(pattern);
		}
		*/
		
		/*
		//Spooky Scary Skeletons
		Player player = new Player();
		Pattern pattern = new Pattern("E6i E6i D#6i D#6i G#5i B5s G#5s G#5i E6i E6i D#6i D#6i G#5h E6i E6i D#6i D#6i G#5i B5s G#5s G#5q B5i C#6i A#5i A#5i G#5h E6i E6i D#6i D#6i G#5i B5s G#5s G#5q E6i E6i D#6i D#6i G#5h E6i E6i D#6i D#6i G#5i B5s G#5s G#5q B5i C#6i A#5i A#5i G#5h G#5w ");
		player.play(pattern);
		*/
		
		/*
		//This is Halloween
		Player player = new Player();
		Pattern pattern = new Pattern("I[64] E6i Ri E6i Ri E6i Ri G#6i A6i B6h B6q B6i A6i G#6h Ri G#6s E6s C#6s G#5s E6s C#6s B5w E6i E6i E6i E6i E6s F6s D6i D6i Ri D6s D6s D6i D6s D6s D6i D6s E6s F6i E6q E6i E6i E6i E6s F6s G6i F6s E6s D6q D6i D6i D6s E6s F6i E6i C6i B5i E6i G6i G6i G6s F#6s E6i G6i G6i G6s F#6s E6i G6i D6i D6i C6s A#5s A5i E6i F6q G#6i G#6i G#6s G6s F6i G#6s G#6s G#6s G#6s G#6s G6s F6i G#6i E6i E6i D#6s C#6s A#5i F6i F#6q D#6i D#6i E6q D#6s D#6s D#6s D#6s E6i D#6i F#5i D6i D6i F#5i F5i F#5s G#5s A#5q Ri F#6i F6q F6i D#6i C6i A#5i C6i D#6i F6q F6i G6i A#5q A#5i A#6i G#6q G#6i F#6i C6i F#6i F6i D#6i G6h C6i C6i C6s B5s A6i C6i C6i C6s B5s A5i G#6s G6s F6i G#6s G6s F6i F6s E6s D6i F6s E6s D6i F6s E6s D6s A5s D6s E6s F6s G6s C7i C7i C#7q C6i C6i G#6q G#6s G#6s G#6i");
		player.play(pattern);
		*/
		
		/*
		//Star Wars Medley
		Player player = new Player();
		Pattern pattern = new Pattern("T[Presto] I[54] E5h A5w B5h B5q C6i D6i C6w E5h E5q E5q A5h A5q B5q C6q E5q C6q* A5q* E6q* D6w Rh E5h A5h A5q B5q C6q C6i A5i E6q E6i C6i A6w A5h C6q* B5q* A5q* E6h E6q C6i A5i E5h E5q E5q A5w A5h E5h A5w B5h B5q C6i D6i C6w E5h E5q E5q A5h A5q B5q C6q E5q C6q* A5q* E6q* D6w Rh E5h A5h A5q B5q C6q C6i A5i E6q E6i C6i A6w A5h C6q* B5q* A5q* E6h E6q C6i A5i E5h E5q E5q A5w A5h");
		player.play(pattern);
		*/
		
		/*
		//Hey There Delilah
		//V1 T[Moderato] I[Piano] Rw | Rw | Rw | Rw | A5q A5i A5s A5i G5i F#5i G5i A5s | A5i A5i A5s B5i. A5s G5i. F#5i G5i | A5i A5i A5i A5s A5i. G5i F#5i G5s A5s | A5i A5i A5i B5i A5s G5i. F#5i E5i | F#5w | G5q G5i G5s F#5i. E5i D5i E5i | F#5h Ri F#5i F#5i D5i E5w | A5q A5i A5s A5i G5i F#5i G5i A5s | A5i A5i A5s B5i. A5s G5i. F#5i G5i | A5i A5i A5i A5s A5i. G5i F#5i G5s A5s | A5i A5i A5i B5i A5s G5i. F#5i E5i | F#5w | Ri G5s G5s G5i G5s F#5i. E5i D5i E5i F#5h Ri F#5i F#5i D5i E5w |
		Pattern hey_there_delilah = new Pattern("V0 T[Moderato] I[40] D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i | F#4i A4i+C#5i F#4i A4i+C#5i F#4i A4i+C#5i F#4i A4i+C#5i | D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i | F#4i A4i+C#5i F#4i A4i+C#5i F#4i A4i+C#5i F#4i A4i+C#5i | D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i | F#4i A4i+C#5i F#4i A4i+C#5i F#4i A4i+C#5i F#4i A4i+C#5i | D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i | F#4i A4i+C#5i F#4i A4i+C#5i F#4i A4i+C#5i F#4q | B3i D4i+F#4i B3i D4i+F#4i B3i D4i+F#4i A3q+A4q | G3i B3i+D4i G3i B3i+D4i A3i C#4i+E4i A3i C#4i+E4i | B3i D4i+F#4i B3i D4i+F#4i B3i D4i+F#4i B3i D4i+F#4i | A3i C#4i+E4i A3i C#4i+E4i A3i C#4i+E4i A3i C#4i+E4i | D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i | F#4i A4i+C#5i F#4i A4i+C#5i F#4i A4i+C#5i F#4i A4i+C#5i | D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i D4i A4i+D5i | F#4i A4i+C#5i F#4i A4i+C#5i F#4i A4i+C#5i F#4q | B3i D4i+F#4i B3i D4i+F#4i B3i D4i+F#4i A3q+A4q | G3i B3i+D4i G3i B3i+D4i A3i C#4i+E4i A3i C#4i+E4i | B3i D4i+F#4i B3i D4i+F#4i B3i D4i+F#4i B3i D4i+F#4i | A3i C#4i+E4i A3i C#4i+E4i A3i C#4i+E4i A3i C#4i+E4i |");
		Player player = new Player();
		player.play(hey_there_delilah);
		*/
		
	}
}
