import RPi.GPIO as GPIO
import time


class Keypad:

    def __init__(self, rows, cols):  #rows og cols are arrays with relative pins in RPi
        self.keypad =[['1','2','3'],
                      ['4','5','6'],
                      ['7','8','9'],
                      ['*','0','#']]
        self.rows_len = 4 #len(self.keypad)
        self.cols_len = 3 #len(self.keypad[1])
        self.rows = rows
        self.cols = cols
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BCM)
        for row in rows:
            self.GPIO.setup(row, GPIO.OUT)
        for col in cols:
            self.GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def do_polling(self):
        self.reset_all_pins()
        for i in range(0, self.rows_len):
            self.GPIO.output(self.rows[i], GPIO.HIGH)
            for j in range(0, self.cols_len):
                if self.GPIO.input(self.cols[j]) == GPIO.HIGH:
                        time.sleep(0.01)
                        if self.GPIO.input(self.cols[j]) == GPIO.HIGH:
                            c = self.keypad[i][j]
                            while self.GPIO.input(self.cols[j]) == GPIO.HIGH:
                                self.dontdoshit()
                            return str(self.keypad[i][j])
            self.GPIO.output(self.rows[i], GPIO.LOW)
        return None

    def dontdoshit(self):
        pass

    def next_signal(self):
        signal = self.do_polling()
        while signal is None:
            signal = self.do_polling()
        return signal

    def reset_all_pins(self):
        for row in self.rows:
            self.GPIO.output(row, GPIO.LOW)