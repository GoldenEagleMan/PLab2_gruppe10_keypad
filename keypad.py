import RPi.GPIO as GPIO
import time


class Keypad:

    def __init__(self, rows, cols):  #rows og cols are arrays with relative pins in RPi
        self.keypad =[['1','2','3'],
                      ['4','5','6'],
                      ['7','8','9'],
                      ['#','0','*']]
        self.rows_len = len(self.keypad) - 1
        self.cols_len = len(self.keypad[1]) - 1
        self.rows = rows
        self.cols = cols
        for row in rows:
            GPIO.setup(row, GPIO.OUT)
        for col in cols:
            GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def do_polling(self):
        for i in range(0, self.rows_len):
            GPIO.output(self.rows[i], GPIO.HIGH)
            for j in range(0, self.cols_len):
                if GPIO.input(self.cols[j]) == GPIO.HIGH:
                    time.sleep(0.001)
                    if GPIO.input(self.cols[j]) == GPIO.HIGH:
                        return self.keypad[i][j]
            GPIO.output(self.rows[i], GPIO.LOW)
        return None

    def next_signal(self):
        while self.do_polling() is None:
            self.do_polling()




'''The keypad has a few essential methods:
  • setup - Set the proper mode via: GPIO.setmode(GPIO.BCM).
    Also, use GPIO functions to set the row pins as outputs and the column pins as inputs.
  • do polling - Use nested loops (discussed above) to determine the key currently being pressed on the keypad. 
  • get next signal - This is the main interface between the agent and the keypad. It should initiate repeated calls to do polling until a key press is detected.
    '''