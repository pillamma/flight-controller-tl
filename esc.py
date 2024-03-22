from machine import Pin , PWM
import time

class ESC :
    def __init__(self , pin):
        self.pin = pin
        self.control = PWM(Pin(self.pin))
        self.control.freq(50)
    
    def calibrate (self):
        print("calibrating esc please connetc battery within 10 sseconds")
        time.sleep(2)
        self.control.duty_u16(6552)
        time.sleep(10)
        self.control.duty_u16(3276)
        time.sleep(2)
        
        
    def thrust (self,x=0):
        if x<0 :
            x=0
        if x>1 :
            x=1
        self.control.duty_u16(int(x*3276 + 3276))