class Bike:

    def __init__(self):
        self.isOn = False
        self.bike_speed = 1

    def turn_on(self):
        if not self.isOn:
            self.isOn = True
            print("BIke is ON Now")
            return  self.isOn

    def turn_off(self):
        if self.isOn:
            self.isOn = False
            print("Bike is OFF Now")
            return self.isOn

    def accelerate_by_gear_levels(self, gear_level):
        if not self.isOn == True:
            print("bike is on")

        if gear_level == 1:
            self.bike_speed += 1

        elif gear_level == 2:
            self.bike_speed += 2

        elif gear_level == 3:
            self.bike_speed += 3

        elif gear_level == 4:
            self.bike_speed += 4

        else:
            raise ValueError("Invalid  increase gear level")

        return self.bike_speed


    def deccelerated_by_gear_levels(self, gear_level):
        if not self.isOn == True:
            print("bike is on")

        if gear_level == 1:
            self.bike_speed -= 1

        elif gear_level == 2:
            self.bike_speed -= 2

        elif gear_level == 3:
            self.bike_speed -= 3

        elif gear_level == 4:
            self.bike_speed -= 4

        else:
            raise ValueError("Invalid gear decrease level")

        return self.bike_speed








    
    
