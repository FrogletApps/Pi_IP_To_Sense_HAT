#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import time
from sense_hat import SenseHat
sense = SenseHat()
ipArray = []
ipBinary = []

# Create the binary digits, dot and blank
#Power of the LED (between 0 and 255)
P = 255
# G = Green, R = Red, B = Blue, N = off
G = [0,P,0]
R = [P,0,0]
B = [0,0,P]
N = [0,0,0]

#Digits are green
digits = [
	[N,N,N,N], #0
	[N,N,N,G], #1
	[N,N,G,N], #2
	[N,N,G,G], #3
	[N,G,N,N], #4
	[N,G,N,G], #5
	[N,G,G,N], #6
	[N,G,G,G], #7
	[G,N,N,N], #8
	[G,N,N,G]  #9
]
#Dot is blue
dot    = [B,B,B,B]
#Blank is red
blank = [R,R,R,R]

#Get the IP address (by making connection to google)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("www.google.co.uk",80))
#Put IP into array
ipArray = list(s.getsockname()[0])
#Close connection 
s.close()

#find the right binary digit to match the decimal
for digit in ipArray:
	if digit.isdigit():
		ipBinary += digits[int(digit)]
	elif digit == ".":
		ipBinary = ipBinary + dot

#if the IP isn't long enough to fill the display then add red squares
while len(ipBinary)<64:
	ipBinary = ipBinary + blank
	
sense.set_pixels(ipBinary)

#Display this on the sense hat display for 30 seconds
time.sleep(30)
sense.clear()
