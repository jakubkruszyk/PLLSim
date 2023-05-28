class Osc:
    def __init__(self, freq):
        self.tics = 0
        self.freq = freq
        self.amp = 0

    def run(self):
        self.tics += 1
        if self.tics >= self.freq:
            self.amp ^= 1
            self.tics = 0
        return self.amp
