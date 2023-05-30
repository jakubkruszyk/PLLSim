from src.osc import Osc
from src.det import Detector


class PLL:
    """
    Container class for all components creating PLL circuit.
    """
    def __init__(self, ref_freq, dco_freq):
        self.ref_osc = Osc(ref_freq)
        self.dco = Osc(dco_freq)
        self.detector = Detector()

    def run(self) -> list:
        x = self.ref_osc.run()
        y = self.dco.run()
        lead, lag = self.detector.run(x, y)
        return [x, y, lead, lag]
