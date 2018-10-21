import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime, timedelta

class LedBoard:


    def __init__(self):
        self.pins = [18, 23, 24]
        self.pin_led_states = [[1, 0, -1],
                               [0, 1, -1],
                               [-1, 1, 0],
                               [-1, 0, 1],
                               [1, -1, 0],
                               [0, -1, 1]]
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BCM)





    # Initialises the led pins with GPIO.setmode(GPIO.BCM)
    #def set_up(self):


    # runs every time the system is powering up. Blink half of the lights and switches a couple of times.
    # Activates when keypad receives the very first press
    def start_up(self, k):
        end_time = datetime.now() + timedelta(seconds=k)
        while datetime.now() < end_time:
            for i in range(0, 3):
                self.light_led(i, 0.05)
            sleep(0.4)
            for i in range(3, 6):
                self.light_led(i, 0.05)
        self.reset()

    # Sets the current state of a specified pin
    def set_pin(self, pin_index, pin_state):
        if pin_state == -1:
            self.GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            self.GPIO.setup(self.pins[pin_index], GPIO.OUT)
            self.GPIO.output(self.pins[pin_index], pin_state)

    # Lights an user-specified led for a user specified time
    def light_led(self, led_number, time):
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)
        sleep(time)
        self.reset()

        
    # flashes all the leds on and off for k seconds
    def flash_all_leds(self, k):
        end_time = datetime.now() + timedelta(seconds=k)
        while datetime.now() < end_time:
            for i in range(0, 6):
                self.light_led(i, 0.02)
        self.reset()


    # twinkles all leds in a sequence on and off for k seconds
    def twinkle_all_leds(self, k):
        end_time = datetime.now() + timedelta(seconds=k)
        while datetime.now() < end_time:
            for i in range(0, 6):
                self.light_led(i, 0.3)
        self.reset()

    # runs every time the system is shutting down. Lights up all of the leds and then shuts them down 1-by-1
    def shut_down(self, k):
        j = 6
        while j>= 0:
            end_time = datetime.now() + timedelta(seconds=k)
            while datetime.now() < end_time:
                for i in range(0, j):
                    self.light_led(i, 0.02)
            j -= 1
        self.reset()

    # Sets all the pins to low
    def reset(self):
        self.set_pin(0, -1)
        self.set_pin(1, -1)
        self.set_pin(2, -1)

def main():
    l = LedBoard()
    print("START UP")
    l.start_up(3)
    print("FLASHING ALL LEDS")
    l.flash_all_leds(3)
    print("TWINKLE ALL LEDS")
    l.twinkle_all_leds(3)
    print("SHUT DOWN")
    l.shut_down(0.5)



if __name__ == '__main__':
    main()














# Behavior
'''The following are mandatory behaviors that your LED board needs to perform:
1. A display of lights (of your choosing) that indicates ”powering up”. This should be performed when the user does the very first keystroke of a session.
2. Flashing of all lights in synchrony when the user enters the wrong password during login.
3. Twinkling the lights (in any sequence you choose) when the user successfully logs in.
4. A fourth type of light display (of your choosing) that indicates ”powering down”. This should be performed immediately after the user logs out.
5. Turn one user-specified LED on for a user-specified number of seconds, where information about the particular LED and duration are entered via the keypad.'''


