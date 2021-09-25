import serial
import matplotlib.pyplot as plt
import math

plt.ion()
fig = plt.figure()
plt.axis([-9, 9, -9, 9])
plt.scatter(0, 0, c="black", marker='s', s=5.5)
ser = serial.Serial('COM4', 9600)
angle = 0
while True:
    data = ser.readline()
    print(data.decode())
    r = float(data.decode())
    angle = angle + 5
    if angle >= 360.0:
        angle = angle - 360
        plt.clf()
        plt.axis([-9, 9, -9, 9])
        plt.scatter(0, 0, c="black", marker='s', s=5.5)
    sine = math.sin(math.radians(angle))
    cosine = math.cos(math.radians(angle))
    plt.scatter(r * cosine, r * sine, s=0.4, c="red")
    plt.pause(0.001)
