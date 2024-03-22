from actuators import ESC
from machine import Pin
import time
pin1=Pin(1,Pin.OUT)
esc1 = ESC(Pin(0,Pin.OUT))
esc2 = ESC(Pin(2,Pin.OUT))
esc3 = ESC(Pin(3,Pin.OUT))
esc4 = ESC(Pin(1,Pin.OUT))
esc1.thrust(1)
esc2.thrust(1)
esc3.thrust(1)
esc4.thrust(1)
def throttle(thr):
    esc1.thrust(thr)
    esc2.thrust(thr)
    esc3.thrust(thr)
    esc4.thrust(thr)
# esc1.thrust(0)
# esc2.thrust(0)
# esc3.thrust(0)
# esc4.thrust(0)