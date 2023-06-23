class SequentialFilter:
    def __init__(self, lead_lag_cnt_max, sum_cnt_max):
        self.lead_lag_cnt_max = lead_lag_cnt_max
        self.sum_cnt_max = sum_cnt_max
        self.lead_cnt = 0
        self.lag_cnt = 0
        self.output = 0

    def run(self, lead, lag):
        """
        Returns:

        - 1 if lead counter is greater or equal its maximum value
        - -1 if lag lead counter is greater or equal its maximum value
        - 0 if sum of lead and lag counter is greater or equal than respective maximum value
        """
        self.lead_cnt += lead
        self.lag_cnt += lag

        if self.lead_cnt + self.lag_cnt >= self.sum_cnt_max:
            self.output = 0  # do nothing, counters are balanced
        elif self.lead_cnt >= self.lead_lag_cnt_max:
            self.output = 1  # increment
        elif self.lag_cnt >= self.lead_lag_cnt_max:
            self.output = -1  # decrement

        else:
            return 0  # early return if none of counters overflows

        # if any of counter overflows resets all of them and return selected output
        self.lead_cnt = 0
        self.lag_cnt = 0
        return self.output

