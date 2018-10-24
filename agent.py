from keypad import *
from ledboard import *


class Agent:

    def __init__(self, fsm, rows, cols, ledpins, file_name):
        self.keypad = Keypad(rows, cols)  # pin raspberrypi
        self.led_board = LedBoard(ledpins)  # pins ledboard
        self.fsm = fsm
        self.attempted_password = ""
        self.cached = ""
        self.file_name = file_name
        # read password from file
        file = open(file_name)
        for line in file:
            line.strip()
            self.password = line
        file.close()

        def boot_up(args=None):
            self.led_board.start_up()

        def reset_pw_acc(args=None):

            if self.fsm.current_state == "S-Read-2":
                print("****** Reset Password ****")
                print("Type in new password")
            self.attempted_password = ""

        def append_next_pw_digit(digit):
            self.attempted_password += str(digit)
            print("Building password: " + self.attempted_password)

        def verify_pw(args=None):
            if self.attempted_password == self.password:
                self.actions["A5"]()
                self.led_board.twinkle_all_leds()
            else:
                self.actions["A4"]()
                self.led_board.flash_all_leds()
            self.attempted_password = ""

        def reset_agent(args=None):
            self.attempted_password = ""
            self.fsm.current_state = "S-Init"

        def activate_agent(args=None):
            self.fsm.current_state = "S-Active"

        def refresh_agent(args=None):
            self.cached = ""
            self.attempted_password = ""

        def cache_first_pw(args=None):
            print("Type new password again")
            self.cached = self.attempted_password
            self.attempted_password = ""

        def compare_pw(args=None):
            if self.cached == self.attempted_password:
                self.password = self.cached
                file = open(self.file_name, "w")
                file.write(self.password)
                file.close()
            self.cached = ""
            self.attempted_password = ""

        def store_pin(pin_num):
            self.pin = pin_num

        def light_led(seconds):
            self.led_board.light_led(int(self.pin) - 1, seconds)
            # light self.pin_number for 'seconds' seconds

        def shut_down(args=None):
            # shut down-lights
            self.led_board.shut_down()

        # dict with all functions
        self.actions = {
            "A0": boot_up,
            "A1": reset_pw_acc,
            "A2": append_next_pw_digit,
            "A3": verify_pw,
            "A4": reset_agent,
            "A5": activate_agent,
            "A6": refresh_agent,
            "A7": cache_first_pw,
            "A8": compare_pw,
            "A9": store_pin,
            "A10": light_led,
            "A11": shut_down
        }

    def update(self, signal):
        active_rule = ""
        for rule in self.fsm.rules:
            #print("current state is: " + self.fsm.current_state + " and evalueting state is: " + rule.start_state)
            if self.fsm.current_state == rule.start_state and signal in rule.signal:
                active_rule = rule
                break
        self.fsm.current_state = active_rule.end_state
        self.actions[active_rule.action](signal)
        print("current state is: " + self.fsm.current_state)

    def check_input_keypad(self):
        input = self.keypad.next_signal()
        print("input from keypad: " + input)
        return input

    def run(self):
        while True:
            self.update(self.check_input_keypad())
