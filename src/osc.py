class Osc:
    def __init__(self, freq):
        self.tics = 0
        self.freq = freq
        self.amp = 0

    def run(self):
        self.tics += 1
        if (self.tics % self.freq) == 0:
            self.amp = not self.amp
        return self.amp
