class Detector:
    """
    Lead Lag phase detector.
    """
    def __init__(self, lead_lag_max, total_max):
        self.ref_osc_last = 0  # previous local_osc state
        self.loc_osc_last = 0
        self.output = (0, 0)
    
    def run(self, osc_ref: int, osc_loc: int) -> (int, int):
        """
        Returns:
            tuple of (lead, lag) signals
        """
        if not(self.loc_osc_last == 0 and osc_loc == 1):
            # Early return if rising edge of local oscillator(dco) not detected.
            self.output = (0, 0)
        else:
            # check if ref_osc generated rising edge alongside loc_osc
            if self.ref_osc_last == 0 and osc_ref == 1:
                self.output = (0, 0)

            if osc_ref:
                self.output = (1, 0)
            else:
                self.output = (0, 1)

        self.loc_osc_last = osc_loc
        self.ref_osc_last = osc_ref
        return self.output
