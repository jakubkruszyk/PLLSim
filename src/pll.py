class PLL:
    """
    Container class for all components creating PLL circuit.
    """
    def __init__(self):
        # Placeholder code
        self.i = 0
        self.a = [1, 1]

    def run(self) -> list:
        # Placeholder code
        self.i += 1
        if 40 > self.i > 20:
            self.a = [0, 0]
        elif self.i > 40:
            self.i = 0
            self.a = [1, 1]

        return self.a

