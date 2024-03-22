from imu import MPU6050
import time
from math import acos , sqrt ,degrees ,atan2
from machine import Pin, I2C
a = 0.9
i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
imu = MPU6050(i2c)
t1 = 0
t0 = time.ticks_ms()
for i in range (100000):
    ax=(imu.accel.x)
    ay=(imu.accel.y)
    az=(imu.accel.z)
    gx=(imu.gyro.x)
    gy=(imu.gyro.y)
    gz=(imu.gyro.z)
    if (ax==0 and ay == 0 and az == 0):
        ax=0.001
        ay=0.001
        az=0.001
        
    t1 = time.ticks_ms()
    dt = t1 - t0
    t0 = t1
    g_roll = gx*dt*0.001
    g_pitch = gy*dt*0.001
    g_yaw = gz*dt*0.001
    a_roll = degrees(acos(az/sqrt(ax**2+az**2)))
    a_pitch = degrees(acos(az/sqrt(ay**2+az**2)))
    a_yaw=degrees(atan2(ay, ax))
    roll = 0.8*g_roll + 0.1*a_roll
    pitch = 0.8*g_pitch + 0.1*a_pitch
    yaw = 0.99*g_yaw+ 0.1*a_yaw
    print(roll,pitch,yaw)
    
    
    
    
    #print("ax:",ax,"\t","ay:",ay,"\t","az:",az,"\t","gx:",gx,"\t","gy:",gy,"\t","gz:",gz)
print(time.time()) 