__author__ = 'Jesse'

import os
import string
import socket
from wsgiref.simple_server import make_server
from wsgiref.util import request_uri

port = 8080
ip = socket.gethostbyname(socket.gethostname())


def main():
	print("Serving on: " + str(ip) + ":" + str(port))
	httpd = make_server(ip, port, webHandler)
	httpd.serve_forever()


def webHandler(environ, start_response):
	status = '200 OK'
	headers = [('Content-type', 'text/plain')]
	start_response(status, headers)

	urlString = request_uri(environ, include_query=0)

	splitter = str(port)+"/"
	splitObj = string.split(urlString, splitter)
	command = splitObj[1]

	if command == "rebootForgeLand":
		os.system("reboot")
	return ""

main()