#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
from sense_hat import SenseHat
sense = SenseHat()

#Get the IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("www.google.co.uk",80))

#print message (then close connection)
sense.rotation = 180
sense.show_message(s.getsockname()[0], scroll_speed=0.5)
s.close()
