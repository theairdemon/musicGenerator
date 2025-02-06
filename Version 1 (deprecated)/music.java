package music;

import org.jfugue.*;
import java.util.Random;

public class music {
	static String [] octave6 = {"C6", "D6", "E6", "F6", "G6", "A6", "B6"};
	static String [] duration = {"h", "i", "q"};
	
	static Random rand = new Random(); //random number generator
	
	static String note(String [] list){
		
		//s is a random number from 0 to n-1
		int s = rand.nextInt(list.length);
		
		//print the s-th word from the list of words
		return list[s];
	}
	
	//random verb
	static String octave6(){
		return note(octave6);
	}
	
	//random verb
	static String duration(){
		return note(duration);
	}
	
	public static void main(String[] args) 	 {
		Player player = new Player();
		Pattern pattern = new Pattern(octave6() + duration() + " " + octave6() + duration() + " " + octave6() + duration() + " " + octave6() + duration() + " " + octave6() + duration() + " " + octave6() + duration() + " " + octave6() + duration() + " " + octave6() + duration() + " " + octave6() + duration() + " ");
		player.play(pattern);
	}
}
