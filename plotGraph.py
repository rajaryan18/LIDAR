import serial
import matplotlib.pyplot as plt
import math
import time

plt.ion()
fig = plt.figure()
plt.axis([-9, 9, -9, 9])
plt.scatter (0, 0, c="black", marker='s', s=5.5)
ser = serial.Serial('COM3', 115200)

angle = 0
x=0
while True:
    data = ser.readline()#reading from serial monitor
    try:
        print(data.decode())
    except:pass
    r = 0
    try :
        r = float(data.decode())
    except : pass
    begin=time.time()
    if r > 0.10:
        r = 0.10
    angle = angle + 3
    if angle >= 360.0:     #resetting everything
        angle = angle - 360
        plt.clf()
        plt.axis([-9, 9, -9, 9])
    
    sine = math.sin(math.radians(angle))
    cosine = math.cos(math.radians(angle))
    plt.scatter(r * cosine * 100, r * sine * 100, s=4.4, c="red")
    plt.pause(0.001)
    #end=time.time()
    print(end-begin)
    x=x+1
    if x==360:
        break

plt.close()
