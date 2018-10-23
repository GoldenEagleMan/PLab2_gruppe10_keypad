from Agent import *
from keypad import *
from ledboard import *
from FSM import *


if __name__ == "__main__":

    fsm = FSM()
    agent = Agent(fsm, file_name = "password")
    agent.run()
