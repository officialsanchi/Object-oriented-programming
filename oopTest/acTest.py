import unittest
from oop import ac



class AcTest (unittest.TestCase):

    def  setUp(self):
        self.ac = ac.Ac()

    def test_that_ac_class_exists(self):
       pass

    def test_that_ac_can_turn_on(self):
        turn_on = self.ac.turn_on()
        self.assertTrue(turn_on,"Ac is On now")

    def test_that_ac_can_turn_off(self):
        turn_on = self.ac.turn_on()
        self.assertTrue(turn_on,"Ac is On now")
        turn_off = self.ac.turn_off()
        self.assertFalse(turn_off,"Ac is Off now")

    def test_that_ac_temperture_can_increase(self):
        turn_on = self.ac.turn_on()
        self.assertTrue(turn_on,"Ac is On now")
        temperture = self.ac.temperture()
