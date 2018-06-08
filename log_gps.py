# log_gps.py
# Read GPS coordinates from USB module in real time and
# Log coordinates to file 
# Author: Omar Metwally, MD 
#	  omar@analog.earth
# License: MIT

import serial, sys, os

ser = serial.Serial('/dev/ttyACM0')
latitude = ''
longitude = ''

while True:
	line = str(ser.readline())
	print('GPS data: ',line)
	if '$GPGGA' in line:
	    line = line.split(',')
	    print(str(line[2]), str(line[4]))
	    lat_dd = float(str(line[2])[0:1])
	    lat_mm = float(str(line[2])[2:])/60
	    latitude = float(str(line[2])[0:2]) + float(str(line[2][2:]))/60
	    longitude = -1 * float(str(line[4])[0:3]) + float(str(line[4][3:]))/60

	    print('Latitude: ', latitude)
	    print('Longitude: ', longitude)
	    filehandle = open('/home/pi/Desktop/way.csv', 'a')
	    filehandle.write(str(latitude)+', '+str(longitude)+', '+'A Walk\n')
	    filehandle.close()


