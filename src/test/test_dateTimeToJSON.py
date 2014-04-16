from unittest import TestCase
from src.main import webCommand
import json
__author__ = 'Jesse'


class TestDateTimeToJSON(TestCase):
	def test_dateTimeToJSON(self):

		if json.dumps(webCommand.dateTimeObj().__dict__, sort_keys=True):
			pass
		else:
			self.fail("JSON Parser Error")

		if webCommand.dateTimeObj().hour >= 23 or webCommand.dateTimeObj().hour < 0:
			self.fail("Hour Parser Broken")

		if webCommand.dateTimeObj().minute >= 59 or webCommand.dateTimeObj().minute < 0:
			self.fail("Minute Parser Broken")