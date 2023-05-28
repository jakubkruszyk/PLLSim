class OSC:
    def __init__(self):
        self.tics = 0
        self.freq = 10
        self.amp = 0

    def run(self):
        self.tics += 1
        if self.freq < self.tics:
            self.amp ^= 1
            self.tics=0
        return self.amp
