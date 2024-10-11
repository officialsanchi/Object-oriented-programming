class Tv:

     def __init__(self):
        self.channel = 1
        self.volume_level = 0
        self.isOn = False

     def turn_on(self):
         if not self.isOn:
             self.isOn = True
             print("tv is on Now")
             return self.isOn

     def turn_off(self):
         if self.isOn:
             self.isOn = False
             print("tv is off Now")
             return self.isOn

     def set_channel(self, channel):
         if not self.isOn == True:
             print("tv is on")
         if 1 <= channel <= 100:
             self.channel = channel
         else:
            raise ValueError("channel must be between 1 and 100")

     def get_channel(self):
        return self.channel

     def channel_up(self):
         self.channel += 1
         return self.channel

     def channel_down(self):
         self.channel -= 1
         return self.channel
     def set_volume(self, volume_level):
         if not self.isOn == True:
             print("tv is on")
         if 1<= volume_level <= 10:
             self.volume_level = volume_level
         else:
             raise ValueError("volume_level must be between 1 and 10")
     def get_volume(self):
         return self.volume_level

     def volume_up(self):
         self.volume_level += 1
         return self.volume_level

     def volume_down(self):
         self.volume_level -= 1
         return self.volume_level

