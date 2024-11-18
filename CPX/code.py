from adafruit_circuitplayground import cp
import time
while True:
    for i in range(0,10):
        cp.pixels[i] = (0,1,0)
        time.sleep(0.2)
        cp.picels[i] = (0,0,0)