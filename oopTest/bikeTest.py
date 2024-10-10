
import unittest
from oop import bike



class BikeTest(unittest.TestCase):

    def setUp(self):
        self.bike = bike.Bike()


    def test_that_bike_class_exist(self):
        pass

    def test_that_bike_is_on(self):
       turn_on =  self.bike.turn_on()
       self.assertTrue(turn_on, "bike is turn on")

    def test_that_bike_is_off(self):
        turn_on = self.bike.turn_on()
        self.assertTrue(turn_on, "bike is turn on")
        turn_off = self.bike.turn_off()
        self.assertFalse(turn_off,"bike is not turn off")

    def test_that_bike_can_accelerate_By_gear_1(self):
        turn_on = self.bike.turn_on()
        self.assertTrue(turn_on, "bike is turn on")
        bike_speed = self.bike.bike_speed = 15
        accelerate_by_gear_1 = self.bike.accelerate_by_gear_levels(1)
        self.assertEqual(accelerate_by_gear_1,  16)

    def test_that_bike_can_accelerate_By_gear_2(self):
        turn_on = self.bike.turn_on()
        self.assertTrue(turn_on, "bike is turn on")
        bike_speed = self.bike.bike_speed = 24
        accelerate_by_gear_2 = self.bike.accelerate_by_gear_levels(2)
        self.assertEqual(accelerate_by_gear_2, 26)

    def test_that_bike_can_accelerate_By_gear_3(self):
        turn_on = self.bike.turn_on()
        self.assertTrue(turn_on, "bike is turn on")
        bike_speed = self.bike.bike_speed = 35
        accelerate_by_gear_3 = self.bike.accelerate_by_gear_levels(3)
        self.assertEqual(accelerate_by_gear_3, 38)

    def test_that_bike_can_accelerate_By_gear_4(self):
        turn_on = self.bike.turn_on()
        self.assertTrue(turn_on, "bike is turn on")
        bike_speed = self.bike.bike_speed = 44
        accelerate_by_gear_4 = self.bike.accelerate_by_gear_levels(4)
        self.assertEqual(accelerate_by_gear_4, 48)

    def test_that_bike_can_deccelerated_by_gear_1(self):
        turn_on = self.bike.turn_on()
        self.assertTrue(turn_on, "bike is turn on")
        bike_speed = self.bike.bike_speed = 15
        accelerate_by_gear_1 = self.bike.deccelerated_by_gear_levels(1)
        self.assertEqual(accelerate_by_gear_1, 14)

    def test_that_bike_can_deccelerated_by_gear_2(self):
        turn_on = self.bike.turn_on()
        self.assertTrue(turn_on, "bike is turn on")
        bike_speed = self.bike.bike_speed = 24
        accelerate_by_gear_2 = self.bike.deccelerated_by_gear_levels(2)
        self.assertEqual(accelerate_by_gear_2, 22)

    def test_that_bike_can_deccelerate_By_gear_3(self):
        turn_on = self.bike.turn_on()
        self.assertTrue(turn_on, "bike is turn on")
        bike_speed = self.bike.bike_speed = 35
        accelerate_by_gear_3 = self.bike.deccelerated_by_gear_levels(3)
        self.assertEqual(accelerate_by_gear_3, 32)

    def test_that_bike_can_deccelerate_By_gear_4(self):
        turn_on = self.bike.turn_on()
        self.assertTrue(turn_on, "bike is turn on")
        bike_speed = self.bike.bike_speed = 44
        accelerate_by_gear_4 = self.bike.deccelerated_by_gear_levels(4)
        self.assertEqual(accelerate_by_gear_4, 40)