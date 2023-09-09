from src.osc import Osc
from src.det import Detector
from src.filter import SequentialFilter


class PLL:
    """
    Container class for all components creating PLL circuit.
    """
    def __init__(self, ref_freq, dco_freq, lead_lag_cnt_max, sum_cnt_max):
        self.input_osc = Osc(ref_freq)
        self.local_osc = Osc(dco_freq)
        self.detector = Detector()
        self.filter = SequentialFilter(lead_lag_cnt_max, sum_cnt_max)

    def run(self) -> list:
        input_value = self.input_osc.run()
        local_value = self.local_osc.run()
        lead, lag = self.detector.run(input_value, local_value)
        delta = self.filter.run(lead, lag)
        # self.dco.freq += delta
        return [input_value, local_value, lead, lag, delta]
