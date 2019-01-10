import serial
ser = serial.Serial('/dev/ttyUSB1')
while True:
	data = ser.read()
	print(data)
