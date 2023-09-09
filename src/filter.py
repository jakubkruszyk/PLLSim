class SequentialFilter:
    def __init__(self, lead_lag_cnt_max, sum_cnt_max):
        self.lead_lag_cnt_max = lead_lag_cnt_max
        self.sum_cnt_max = sum_cnt_max
        self.lead = 0
        self.lag = 0
        self.output = 0

    def run(self, lead, lag):
        """
        Returns:

        - 1 if lag counter is greater or equal its maximum value
        - -1 if lead counter is greater or equal its maximum value
        - 0 if sum of lead and lag counter is greater or equal than respective maximum value
        """
        self.lead += lead
        self.lag += lag
        if (self.lead + self.lag) > self.sum_cnt_max:
            self.output = 0
        elif self.lag > self.lead_lag_cnt_max:
            self.output = 1
        elif self.lead > self.lead_lag_cnt_max:
            self.output = -1
        else:
            # early return if none of counters overflows
            return 0

        # if any of counter overflows resets all of them and return selected output
        self.lead = 0
        self.lag = 0
        return self.output
