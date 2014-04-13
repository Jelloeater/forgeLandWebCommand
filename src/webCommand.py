__author__ = 'Jesse'

import os
import string
import socket
from wsgiref.simple_server import make_server
from wsgiref.util import request_uri
import time

port = 9000
ip = socket.gethostbyname(socket.gethostname())


def main():
	print("Serving on: " + str(ip) + ":" + str(port))
	httpd = make_server(ip, port, webHandler)
	httpd.serve_forever()


def webHandler(environ, start_response):
	retStr = ""
	status = '200 OK'
	headers = [('Content-type', 'text/plain')]
	start_response(status, headers)

	urlString = request_uri(environ, include_query=0)
	if urlString != "http://"+str(ip)+":"+str(port)+"/":  # Parses off end of URL if present
		splitter = str(port)+"/"
		splitObj = string.split(urlString, splitter)
		command = splitObj[1]

		if command == "rebootForgeLand":
			retStr = "Rebooting NOW!"
			os.system("reboot")

		if command == "time":
			timeStr = time.asctime()
			print(timeStr)
			timeStrHr = timeStr[11:12]
			hour = int(timeStrHr)
			timeStrMin = timeStr[14:16]
			minute = int(timeStrMin)
			minFormat = ""

			hour += 5
			amPm = "p"
			if hour > 12:
				hour -= 12
				amPm = "a"

			if minute < 9:
				minFormat = "0"

			hour = str(hour)
			minute = str(minute)
			separator = ":"
			retStr = hour + separator + minFormat + minute + amPm

	return retStr

main()