"""
Autor: Luis Pérez Cantarero

Date: 27/02/2024

Coche
"""
from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.fuel = 0
        self.__burnout = "      ____\n" \
                         + "   __/  |_\_\n" \
                         + "c==|  _     _``-.\n" \
                         + "c=='-(_)---(_)--'"

    def burnout(self):
        if self.fuel >= 1:
            print(self.__burnout)
            self.fuel -= 1
        else:
            print("No se puede quemar rueda sin combustible suficiente.")

    def refuel(self, liters):
        if liters > 0:
            self.fuel = min(50, self.fuel + liters)
            print(f"Depósito lleno.")

    def travel(self, kilometers):
        max_fuel = kilometers * 0.1
        if self.fuel >= max_fuel:
            super().travel(kilometers)
            self.fuel -= max_fuel
        else:
            distance = self.fuel * 10
            if distance > 0:
                super().travel(distance)
                self.fuel = 0
                print(f"El coche ha viajado {distance} km.")
            else:
                print("No se puede viajar sin combustible suficiente.")
