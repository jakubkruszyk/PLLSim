class Osc:
    def __init__(self, period):
        self.tics = 0
        self.period = period
        self.amp = 0

    def run(self):
        self.tics += 1
        if (self.tics % self.period) == 0:
            self.amp = not self.amp
        return self.amp

    def reset(self):
        self.tics = 0
        self.amp = 0
