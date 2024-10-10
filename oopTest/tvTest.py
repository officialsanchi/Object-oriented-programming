import unittest
from oop import tv



class TvTest(unittest.TestCase):
    def setUp(self):
        self.tv = tv.Tv()

    def test_that_tv_class_exist(self):
        pass

    def test_that_tv_can_turn_on(self):
        turn_on = self.tv.turn_on()
        self.assertTrue(turn_on,"tv is on Now")

    def test_that_tv_can_turn_off(self):
        turn_on = self.tv.turn_on()
        self.assertTrue(turn_on,"tv is on Now")
        turn_off = self.tv.turn_off()
        self.assertFalse(turn_off,"tv is off Now")

    def test_that_tv_channel_can_increase(self,):
        turn_on = self.tv.turn_on()
        self.assertTrue(turn_on,"tv is on Now")
        channel = self.tv.channel = 1
        current_channel = self.tv.channel_up()
        self.assertEqual(current_channel, 2)

    def test_that_tv_channel_can_decrease(self,):
        turn_on = self.tv.turn_on()
        self.assertTrue(turn_on,"tv is on Now")
        channel = self.tv.channel = 1
        current_channel = self.tv.channel_down()
        self.assertEqual(current_channel, 0)

    def test_that_tv_has_volume(self):
        turn_on = self.tv.turn_on()
        self.assertTrue(turn_on,"tv is on Now")
        channel = self.tv.channel = 1
        volume_level = self.tv.volume_level = 0


    def test_that_tv_volume_can_increase(self):
        turn_on = self.tv.turn_on()
        self.assertTrue(turn_on, "tv is on Now")
        channel = self.tv.channel = 1
        volume_level = self.tv.volume_level = 1
        current_volume_level = self.tv.volume_up()
        self.assertEqual(current_volume_level, 2)

    def test_that_tv_volume_can_decrease(self):
        turn_on = self.tv.turn_on()
        self.assertTrue(turn_on, "tv is on Now")
        channel = self.tv.channel = 1
        volume_level = self.tv.volume_level = 1
        current_volume_level = self.tv.volume_down()
        self.assertEqual(current_volume_level, 0)







