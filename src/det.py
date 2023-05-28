class Det:
    """
    Container class for all components creating PLL circuit.
    """
    def __init__(self, osc_loc):
        self.lead_c = 0                 #lead counter
        self.lag_c = 0                  #lag counter
        self.last = osc_loc.amp         #previous_local_osc_state
    
    def run(self, osc_in, osc_loc):
        if (self.osc_loc != self.last):
            self.last = osc_loc.amp
            if (osc_in.amp == 1):       #zbocze wysokie
                self.lead_c += 1
            else:                       #zbocze niskie
                self.lag_c += 1
        if(self.lead_c+self.lag_c>=5):
            self.lead_c = 0
            self.lag_c = 0
            return 0;
        if (self.lag_c>=4):
            return -1;
        if (self.lead_c>4):
            return(1)
