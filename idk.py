from Ibus import commands
from state import MOTOR,orientation
import time


FRmotor = MOTOR(0)
FLmotor = MOTOR(1)
RLmotor = MOTOR(2)
RRmotor = MOTOR(3)
def kill():   
    FRmotor.thrust(0)#anticlockwise
    FLmotor.thrust(0)#clockwise****
    RLmotor.thrust(0)#anticlockwise
    RRmotor.thrust(0)#clockwise**
def thrust(t):
    FRmotor.thrust(t)#anticlockwise
    #FLmotor.thrust(t)#clockwise****
    RLmotor.thrust(t)#anticlockwise
    #RRmotor.thrust(t)#clockwise****
    
recieved_command = commands()

#drone_orientation = orientation()


set_pitch = 0


#drone_orientation.pitch-set_pitch

t1 = time.ticks_ms()
# for i in range (1000):
#     drone_orientation.update()
#     recieved_command.update()
# t2 = time.ticks_ms()

# for i in range (10000):
#     drone_orientation.update()
#     print(drone_orientation.pitch,drone_orientation.roll,drone_orientation.yaw)
#     recieved_command.update()
#     if recieved_command.is_good:
#         thrust(recieved_command.throttle)
# # print(recieved_command.is_good)
#thrust(0)
recieved_command.update()

while recieved_command.is_good :
    #drone_orientation.update()
    recieved_command.update()
    print(recieved_command.throttle)
    if recieved_command.is_good:
        FRmotor.thrust(recieved_command.throttle )
        RLmotor.thrust(recieved_command.throttle )
    else:
        kill()
kill()
