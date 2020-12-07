class Car:
    def __init__(self, speed, color, make, cost):
        self.__speed = speed
        self.__color = color
        self.__make = make
        self._cost = cost

    def _set_speed(self, value):
        self.__speed = value

    def _get_speed(self):
        return self.__speed

    def _set_color(self, value):
        self.__color = value

    def _get_color(self):
        return self.__color
    
    def _set_make(self, value):
        self.__make = value
    
    def _get_make(self):
        return self.__make

    def _set_cost(self, value):
        self._cost = value

    def _get_cost(self):
        return self._cost

     

Mazda = Car(137, "red", "Mazda", "$30,000")
Ferrari = Car(211, "blue", "Ferrari", "$400,000" )
Lambo = Car(202, "black", "Lamborghini", "$500,000")

Mazda._set_speed(188)
Ferrari._set_speed(225)
Lambo._set_speed(255)

Mazda._set_color("Dark Blue")
Ferrari._set_color("Red")
Lambo._set_color("Jet Black and Lime Green")

Mazda_Spd_Msg = "The speed of the {} is: {:>5}".format(Mazda._get_make(), Mazda._get_speed())
Mazda_Clr_Msg = "The color of the {} is: {:>8}".format(Mazda._get_make(), Mazda._get_color())
Mazda_Cost_Msg = "The cost of the {} is: {:>8}\n".format(Mazda._get_make(), Mazda._get_cost())

Ferrari_Spd_Msg = "The speed of the {} is: {:>5}".format(Ferrari._get_make(), Ferrari._get_speed())
Ferrari_Clr_Msg = "The color of the {} is: {:>6}".format(Ferrari._get_make(), Ferrari._get_color())
Ferrari_Cost_Msg = "The cost of the {} is: {:>8}\n".format(Ferrari._get_make(), Ferrari._get_cost())

Lambo_Spd_Msg = "The speed of the {} is: {:>5}".format(Lambo._get_make(), Lambo._get_speed())
Lambo_Clr_Msg = "The color of the {} is: {:>10}".format(Lambo._get_make(), Lambo._get_color())
Lambo_Cost_Msg = "The cost of the {} is: {:>8}".format(Lambo._get_make(), Lambo._get_cost())


print(Mazda_Spd_Msg)
print(Mazda_Clr_Msg)
print(Mazda_Cost_Msg)

print(Ferrari_Spd_Msg)
print(Ferrari_Clr_Msg)
print(Ferrari_Cost_Msg)

print(Lambo_Spd_Msg)
print(Lambo_Clr_Msg)
print(Lambo_Cost_Msg)









    




