import machine
import uasyncio as asyncio
import ustruct

class Reciever :
    
    
    def __init__ (self,uart):
            
        self.uart1 = machine.UART(uart, baudrate=115200, tx=17, rx=16)
        self.throttle = 0
        self.pitch = 0
        self.roll = 0
        self.yaw = 0
        self.buffer = bytearray(12)
        self.fstr = "<hhhhhh"
        self.tolarance=0

    async def update(self):
        space = ' '.encode()
        at_ = '@'.encode()
        while True:
            if self.uart1.any():
                byte = self.uart1.read(1)
                if byte == space:
                    byte = self.uart1.read(1)                    
                    if byte == at_:
                        self.buffer = self.uart1.read(12)
                        if len(self.buffer)==12:
                            tup = ustruct.unpack(self.fstr,self.buffer)
                            if any(x < 0 for x in tup):
                                self.tolarance += 1
                            else :
                                self.tolarance =0
                                self.roll=tup[0]
                                self.pitch=tup[1]
                                self.throttle=tup[2]
                                self.yaw=tup[3] 
            await asyncio.sleep(0.0001)  # Check every 100ms

