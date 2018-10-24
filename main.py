from agent import *
from FSM import *


if __name__ == "__main__":
    
    rows =[5, 6, 13, 19]
    cols = [4, 17, 22]
    ledpins = [18, 23, 24]
    fsm = FSM("/home/pi/Desktop/p5dir/rules")
    agent = Agent(fsm, rows, cols, ledpins, file_name = "/home/pi/Desktop/p5dir/password")
    agent.run()
