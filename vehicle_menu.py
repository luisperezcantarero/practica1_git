"""
Autor: Luis Pérez Cantarero

Date: 28/02/2024

Menu
"""
from POO.Tanda2.ej8_menu import Menu
from bike import Bike
from car import Car
from vehicle import Vehicle


def main():
    bike = Bike()
    car = Car()

    menu = Menu("Anda con la bicicleta.", "Haz el caballito con la bicicleta.", "Anda con el coche.",
                "Quema rueda con el coche.", "Llena el depósito del coche.", "Ver kilometraje de la bicicleta.",
                "Ver kilometraje del coche.", "Ver el combustible que queda en el depósito del coche.", "Ver kilometraje total."
                "Salir.")

    while True:
        opc = menu.choose()
        match opc:
            case 1:
                km = float(input("¿Cuantos kilometros desea recorrer en bici? "))
                bike.travel(km)
            case 2:
                bike.wheelie()
            case 3:
                km = float(input("¿Cuantos kilometros desea recorrer en coche? "))
                car.travel(km)
            case 4:
                car.burnout()
            case 5:
                combustible = float(input("¿Cuanto combustible desea llenar? "))
                car.refuel(combustible)
            case 6:
                print(f"El kilometraje de la bicicleta: {bike.kilometers_traveled} km.")
            case 7:
                print(f"El kilometraje del coche: {car.kilometers_traveled} km.")
            case 8:
                print(f"El Combustible en el depósito: {car.fuel} L")
            case 9:
                print(f"El kilometraje total es de: {Vehicle.kilometers_traveled} km.")
            case 10:
                break


if __name__ == "__main__":
    main()
