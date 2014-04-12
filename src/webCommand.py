__author__ = 'Jesse'

import os
from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults
import socket

port = 8080
ip = socket.gethostbyname(socket.gethostname())


def sshCommand(commandIn):
	# Runs command on local machine if string matches
	if commandIn == "reboot":
		os.system("reboot")


def main():
	print("Serving on: " + str(ip) + ":" + str(port))
	httpd = make_server(ip, port, webHandler)
	httpd.serve_forever()


def webHandler(environ, start_response):
	status = '200 OK'
	headers = [('Content-type', 'text/plain')]
	start_response(status, headers)




	ret = "fuck"
	return ret


main()