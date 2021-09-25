import serial
import matplotlib.pyplot as plt
import math

plt.ion()
fig = plt.figure()
plt.axis([-3, 3, -3, 3])
ser = serial.Serial('/dev/ttyACMo', 9600)
ser.close()
ser.open()
angle = 0

while True:
	data = ser.readline()
	print(data.decode())
	r = float(data.decode())
	#r = float(random.randint(0, 20))/10
	angle = angle + 1.8
	if angle >= 360.0:
		angle = angle - 360
		plt.clf()
	sine = math.sin(angle)
	cosine = math.cos(angle) 
	plt.scatter(r*cosine, r*sine)
	plt.pause(0.0001)
		
plt.close()
