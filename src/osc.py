class Osc:
    def __init__(self, period):
        self.tics = 0
        self.next_update = period/2
        self.period = period
        self.amp = 0

    def run(self):
        self.tics += 1
        if self.tics >= self.next_update:
            self.amp = not self.amp
            self.next_update += self.period/2
        return self.amp

    def reset(self):
        self.tics = 0
        self.amp = 0
        self.next_update = self.period/2
