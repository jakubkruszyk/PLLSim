from src.osc import Osc


class PLL:
    """
    Container class for all components creating PLL circuit.
    """
    def __init__(self):
        self.ref_osc = Osc(20)
        self.dco = Osc(10)

    def run(self) -> list:
        x = self.ref_osc.run()
        y = self.dco.run()
        return [x, y]
