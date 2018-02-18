import RPi.GPIO as GPIO
import time

class GPIOLibs:
    def __init__(self):
        self.GPIO_PIN = 16 #GPIO PIN IN BOARD
        
        #here we are going to use BOARD mode
        GPIO.setmode(GPIO.BOARD)
        print "GPIO MODE SET TO BOARD"
        
        #here this command makes python not to show GPIO warnings
        GPIO.setwarnings(False)
        print "GPIO WARNING TO NONE"

        #here Initilize GPIO PIN to Output mode
        GPIO.setup(self.GPIO_PIN, GPIO.OUT)
        print "GPIO PIN SET"

    def LedState(self, state):
        #make GPIO pin change its state
        GPIO.output(self.GPIO_PIN, state)

        print "GPIO PIN STATE CHANGE:", state
        
        #pause python for 0.1 second
        time.sleep(0.1)
