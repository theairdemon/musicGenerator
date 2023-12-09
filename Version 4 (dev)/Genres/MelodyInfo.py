class MelodyInfo:

    def __init__(self):
        # Basic choices that we have:
        # 1. adjusting repeated measures
        #   a. Should we perfectly repeat the notes no matter what chord lies underneath?
        #   b. Should we invert the progression? (i.e., if starting high and going low, should we instead be starting low and going high?)
        #   c. Should we adjust the notes to move longer notes to closest chord notes?
        #   d. Should we adjust the notes to a scale variation starting with the chord root note?
        # 2. strictness of progressions (tending to move up or down)
        #   a. How often should we tend to keep our direction of movement the same w/in 1 measure?
        #   b. How often should we invert progression from one measure to the next?
        #   c. How often should we have a starting_note that is close to the last note of the directly procedding measure?
        #   d. How often should we keep a similar progression?
        #   e. How close to the previous measure's total range should we be?
        
        # sequential, don't need to sum to 1
        self.measure_adjustments = {
            "perfect": 0.0, # identical repetition
            "inverted": 0.0, # invert progression
            "chord": 0.0, # same scale movement, but starting on current chord root
            "slight": 0.0 # pull longer notes to current chord notes
        }
        
        self.progressions = {
            "in-measure": 0.0,
            "inverted": 0.0,
            "range": 0.0,
            "pickup": 0.0,
            "same": 0.0
        }
        
    def set_melodic_choices(self, adjustment_probabilities):
        self.measure_adjustments = adjustment_probabilities
        print("setting melody info")
