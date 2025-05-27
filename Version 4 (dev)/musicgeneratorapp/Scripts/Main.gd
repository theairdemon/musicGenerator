extends Node2D

@export var debugInfo: RichTextLabel
@export var FluidSynthInstrumentsLabel: Label

var pid_file = "/tmp/test1_pid"

var playing_music: bool
var selected_key := 0
var selected_genre := 0
var selected_style := 0

var instrument_chords := 0
var instrument_melody:= 0
var instrument_arp := 0
var synth_gain := 1.0

func _ready():
	playing_music = false

func generate_music():
	# Call scripts to generate music and play it
	OS.create_process("/bin/bash", ["/mnt/DATA/Documents/Github/musicGenerator/Version 4 (dev)/e2eSongGen.sh", 
		selected_key, selected_genre, selected_style, 
		instrument_chords, instrument_melody, instrument_arp, synth_gain])
	terminal_log()

func terminal_log():
	debugInfo.clear()
	await get_tree().create_timer(1.0).timeout

	if FileAccess.file_exists("/tmp/test_shell_log.txt"):
		var log = FileAccess.open("/tmp/test_shell_log.txt", FileAccess.READ)
		while not log.eof_reached():
			#print(log.get_line())
			debugInfo.append_text(log.get_line())
			debugInfo.append_text("\n")

func _process(delta):
	pass

func _exit_tree():
	kill_music()

func get_pid() -> String:
	var pid_str = ""
	if FileAccess.file_exists(pid_file):
		var f = FileAccess.open(pid_file, FileAccess.READ)
		pid_str = f.get_line()
		f.close()
	
	return pid_str

func kill_music():
	var pid_str = get_pid()
	
	if pid_str:
		OS.create_process("/usr/bin/kill", ["-9", pid_str])

	DirAccess.remove_absolute("/tmp/test1_pid")

# =====================
# BUTTON CONTROLS
# =====================
func _on_play_pressed() -> void:
	if !playing_music:
		generate_music()
		playing_music = true
	else:
		kill_music()
		generate_music()

func _on_stop_pressed() -> void:
	if playing_music:
		kill_music()
		playing_music = false

func _on_quit_pressed() -> void:
	kill_music()
	get_tree().quit() 


func _on_key_list_item_selected(index: int) -> void:
	selected_key = index

func _on_genre_list_item_selected(index: int) -> void:
	selected_genre = index

func _on_style_list_item_selected(index: int) -> void:
	selected_style = index


func _on_chord_list_item_selected(index: int) -> void:
	instrument_chords = index

func _on_melody_list_item_selected(index: int) -> void:
	instrument_melody = index

func _on_arpeggio_list_item_selected(index: int) -> void:
	instrument_arp = index

func _on_volume_slider_value_changed(value: float) -> void:
	synth_gain = value


func _on_feeling_lucky_button_pressed() -> void:
	var total_instruments = FluidSynthInstrumentsLabel.FLUIDSYNTH_INSTRUMENTS.size()
	instrument_chords = randi_range(0, total_instruments - 1)
	instrument_melody = randi_range(0, total_instruments - 1)
	instrument_arp = randi_range(0, total_instruments - 1)
	
	FluidSynthInstrumentsLabel.ChordList.select(instrument_chords)
	FluidSynthInstrumentsLabel.MelodyList.select(instrument_melody)
	FluidSynthInstrumentsLabel.ArpeggioList.select(instrument_arp)
