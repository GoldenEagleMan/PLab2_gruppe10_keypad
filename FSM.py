from rule import *


class FSM:
    def __init__(self, file_name):
        self.rules = []
        self.current_state = "S-OFF"
        f = open(file_name, 'r')
        f
        for line in f:
            line = line.strip()
            info = line.split(" ")
            start_state = info[0]
            end_state = info[1]
            signal = info[2]
            action = info[3]
            new_rule = Rule(start_state, end_state, signal, action)
            self.rules.append(new_rule)
        f.close()
