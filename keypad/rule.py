class Rule:
    def __init__(self, start_state, end_state, signal, action):
        self.start_state = start_state
        self.end_state = end_state
        self.signal = signal
        self.action = action
