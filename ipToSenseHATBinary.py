#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import time
from sense_hat import SenseHat
sense = SenseHat()
ipArray = []
ipBinary = []

# Create the binary digits (in green)
# Y=1, N=0
Y = [0,255,0]
N = [0,0,0]
zero   = [N,N,N,N]
one    = [N,N,N,Y]
two    = [N,N,Y,N]
three  = [N,N,Y,Y]
four   = [N,Y,N,N]
five   = [N,Y,N,Y]
six    = [N,Y,Y,N]
seven  = [N,Y,Y,Y]
eight  = [Y,N,N,N]
nine   = [Y,N,N,Y]

# Dot will be in blue
Y = [0,0,255]
dot    = [Y,Y,Y,Y]

#Get the IP address (by making connection to google)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("www.google.co.uk",80))
#Put IP into array
ipArray = list(s.getsockname()[0])
#Close connection 
s.close()

#find the right binary digit to match the decimal
for digit in ipArray:
	if digit == "0":
		ipBinary = ipBinary + zero
	elif digit == "1":
		ipBinary = ipBinary + one
	elif digit == "2":
		ipBinary = ipBinary + two
	elif digit == "3":
		ipBinary = ipBinary + three
	elif digit == "4":
		ipBinary = ipBinary + four
	elif digit == "5":
		ipBinary = ipBinary + five
	elif digit == "6":
		ipBinary = ipBinary + six
	elif digit == "7":
		ipBinary = ipBinary + seven
	elif digit == "8":
		ipBinary = ipBinary + eight
	elif digit == "9":
		ipBinary = ipBinary + nine
	elif digit == ".":
		ipBinary = ipBinary + dot

#if the IP isn't long enough to fill the display then add red squares
Y= [255,0,0]
blank = [Y,Y,Y,Y]
while len(ipBinary)<64:
	ipBinary = ipBinary + blank
	
sense.set_pixels(ipBinary)
time.sleep(30)

reset = [
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N
]
sense.set_pixels(reset)




