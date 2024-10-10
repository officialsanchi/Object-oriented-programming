class Ac:

    def __init__(self):
        self. isOn = False

    def turn_on(self):
        if not self.isOn:
            self.isOn = True
            print("Ac is On now")
            return self.isOn

    def turn_off(self):
        if self.isOn:
            self.isOn = False
            print("Ac is Off  now ")
            return self.isOn

    def temperture_increase(self,temperture):
        if  not self.isOn == True :
            print("Ac is On now")

        if temperture < 16  and temperture > 30:
            return temperture



