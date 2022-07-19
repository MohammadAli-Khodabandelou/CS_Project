class Timer:
    def __init__(self):
        self.period = 0

    def is_finished(self):
        return self.period == 0

    def tick(self):
        if self.period > 0:
            self.period -= 1

    def set_period(self, new_period):
        self.period = new_period
