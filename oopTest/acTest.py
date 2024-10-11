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

    def test_that_ac_temperature_can_increase(self):
        turn_on = self.ac.turn_on()
        self.assertTrue(turn_on,"Ac is On now")
        temperature_increase = self.ac.temperature_increase = 15
        self.assertEqual(temperature_increase,16)



