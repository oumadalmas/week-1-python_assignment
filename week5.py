class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.__weakness = weakness  # Encapsulated attribute

    def display_info(self):
        print("Superhero: {}".format(self.name))
        print("Power: {}".format(self.power))

    def reveal_weakness(self):
        print("{}'s weakness is {}".format(self.name, self.__weakness))


class FlyingHero(Superhero):
    def __init__(self, name, power, weakness, flight_speed):
        super().__init__(name, power, weakness)  # No arguments required in Python 3
        self.flight_speed = flight_speed

    def display_info(self):
        super().display_info()
        print("Flight Speed: {} km/h".format(self.flight_speed))


# Testing the classes
hero1 = Superhero("Invisiboy", "Invisibility", "Loud Noises")
hero2 = FlyingHero("FalconWing", "Flight", "Heavy Winds", 500)

hero1.display_info()
hero1.reveal_weakness()
print("\n")
hero2.display_info()
hero2.reveal_weakness()

