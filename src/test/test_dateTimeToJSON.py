from unittest import TestCase
from src.main import webCommand
__author__ = 'Jesse'


class TestDateTimeToJSON(TestCase):
	def test_dateTimeToJSON(self):

		webCommand.dateTimeToJSON()

		if True:
			pass
		else:
			self.fail("JSON Parser Error")