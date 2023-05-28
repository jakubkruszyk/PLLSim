class DET:
    """
    Container class for all components creating PLL circuit.
    """
    def __init__(self):
        self.lead_count = 0
        self.lag_count = 0
    
    def run(self, osc_in, osc_loc):
        if osc_in.amp!=osc_loc.amp:
            self.lead += 1
        else:
            self.lag +=1
        if(self.lead+self.lag>=5):
            self.lead = 0
            self.lag = 0
            return 0;
        if (self.lag>=4):
            return -1;
        if (self.lead>4):
            return(1)
