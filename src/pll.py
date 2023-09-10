from src.osc import Osc
from src.det import Detector
from src.filter import SequentialFilter
from src.globals import DEFAULT_PHASE, DEFAULT_STEP


class PLL:
    """
    Container class for all components creating PLL circuit.
    """
    def __init__(self, ref_period, dco_period, lead_lag_cnt_max, sum_cnt_max):
        self.input_osc = Osc(ref_period)
        self.local_osc = Osc(dco_period)
        self.local_osc.tics = DEFAULT_PHASE
        self.detector = Detector()
        self.filter = SequentialFilter(lead_lag_cnt_max, sum_cnt_max)
        self.step = DEFAULT_STEP

    def run(self) -> list:
        input_value = self.input_osc.run()
        local_value = self.local_osc.run()
        lead, lag = self.detector.run(input_value, local_value)
        delta = self.filter.run(lead, lag)
        self.local_osc.tics += delta * self.step
        return [input_value, local_value, lead, lag, delta]
