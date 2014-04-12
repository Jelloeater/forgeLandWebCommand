__author__ = 'Jesse'

import os
from wsgiref.simple_server import make_server, demo_app, WSGIRequestHandler
from io import StringIO
import socket

port = 8080
ip = socket.gethostbyname(socket.gethostname())


def sshCommand(commandIn):
	# Runs command on local machine if string matches
	if commandIn == "reboot":
		os.system("reboot")


def main():
	print("Serving on: " + str(ip) + ":" + str(port))
	server_address = (ip, port)
	httpd = make_server(ip, port, webHandler.parser)
	httpd.serve_forever()


class webHandler(WSGIRequestHandler):
	def parser(environ, start_response):
		from io import StringIO

		stdout = StringIO()
		print"Hello world!FUCK"
		h = sorted(environ.items())
		for k, v in h:
			print k, '=', repr(v)

		start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
		return [stdout.getvalue().encode("utf-8")]


main()