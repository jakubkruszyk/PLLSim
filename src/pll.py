from src.osc import Osc
from src.det import Detector
from src.filter import SequentialFilter


class PLL:
    """
    Container class for all components creating PLL circuit.
    """
    def __init__(self, ref_freq, dco_freq, lead_cnt_max, lag_cnt_max):
        self.ref_osc = Osc(ref_freq)
        self.dco = Osc(dco_freq)
        self.detector = Detector()
        self.filter = SequentialFilter(lead_cnt_max, lag_cnt_max)

    def run(self) -> list:
        x = self.ref_osc.run()
        y = self.dco.run()
        lead, lag = self.detector.run(x, y)
        return [x, y, lead, lag]
