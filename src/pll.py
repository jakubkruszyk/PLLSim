from src.osc import Osc


class PLL:
    """
    Container class for all components creating PLL circuit.
    """
    def __init__(self):
        self.ref_osc = Osc()
        # Placeholder code
        self.i = 0
        self.a = [1, 1]

    def run(self) -> list:
        x = self.ref_osc.run()
        # Placeholder code
        self.i += 1
        if 40 > self.i > 20:
            self.a[0] = 0
        elif self.i > 40:
            self.i = 0
            self.a[0] = 1

        self.a[1] = x
        return self.a

