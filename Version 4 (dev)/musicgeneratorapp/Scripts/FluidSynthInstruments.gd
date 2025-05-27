extends Label

@export var ChordList: OptionButton
@export var MelodyList: OptionButton
@export var ArpeggioList: OptionButton
@export var FLUIDSYNTH_INSTRUMENTS = ['Violins', 'Electric Piano', 'Organ', 'Plucked Guitar', 'Choir','Trumpet', '40s brass', 'Synth & Keys', 'Harpsichord', 'Fantasy Piano', 'Alto Sax', 'Strings', 'Voices', 'Alaska Synth']

func _ready():
	for instrument in FLUIDSYNTH_INSTRUMENTS:
		ChordList.add_item(instrument)
		MelodyList.add_item(instrument)
		ArpeggioList.add_item(instrument)
	
