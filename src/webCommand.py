__author__ = 'Jesse'

import os
import string
import socket
from wsgiref.simple_server import make_server
from wsgiref.util import request_uri

# port = 9000
# ip = socket.gethostbyname(socket.gethostname())
ip = "localhost"
port = 8080

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
	if urlString != "http://" + str(ip) + ":"+ str(port) + "/":  # Parses off end of URL if present
		splitter = str(port) + "/"
		splitObj = string.split(urlString, splitter)
		command = splitObj[1]

		if command == "rebootForgeLand":
			retStr = "Rebooting NOW!"
			os.system("reboot")

		if command == "time":
			retStr = timeStringOutput(4,20)

			# TODO Change to proper time input


	return retStr

def dateTimeToJSON():
	import time
	import json
	# Example: "Mon Apr 14 23:20:23 2014"
	rawJSON = ""

	timeStr = time.asctime()
	year = int(timeStr[20:24])
	month = parseMonth(timeStr[4:7])
	day = int(timeStr[8:10])
	hour = int(timeStr[10:13])
	minute = int(timeStr[14:16])
	second = int(timeStr[17:19])
	dayOfWeek = parseDay(timeStr[0:3])

	# FIXME Need to add either class or dictionary to hold values for JSON converter

	rawJSON = json.JSONEncoder.encode()



	return rawJSON

def parseDay(dayStr):
	if dayStr == "Sun": dayInt = 1
	if dayStr == "Mon": dayInt = 2
	if dayStr == "Tue": dayInt = 3
	if dayStr == "Wed": dayInt = 4
	if dayStr == "Thr": dayInt = 5
	if dayStr == "Fri": dayInt = 6
	if dayStr == "Sat": dayInt = 7
	return dayInt

def parseMonth(monthStr):
	if monthStr == "Jan": monthInt = 1
	if monthStr == "Feb": monthInt = 2
	if monthStr == "Mar": monthInt = 3
	if monthStr == "Apr": monthInt = 4
	if monthStr == "May": monthInt = 5
	if monthStr == "Jun": monthInt = 6
	if monthStr == "Jul": monthInt = 7
	if monthStr == "Aug": monthInt = 8
	if monthStr == "Sep": monthInt = 9
	if monthStr == "Oct": monthInt = 10
	if monthStr == "Nov": monthInt = 11
	if monthStr == "Dec": monthInt = 12
	return monthInt

def timeStringOutput(hour, minute):
	minFormat = ""

	# Convert to local time
	hour += 5
	amPm = "p"

	if hour > 12: # This is twice in-case the time is over 24 hours, due to my bad math
		hour -= 12
		amPm = "a"

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


# main() # TODO Re-enable main when done
dateTimeToJSON()