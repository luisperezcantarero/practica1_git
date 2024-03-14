"""
Autor: Luis Pérez Cantarero

Date: 30/02/2024

Crea la clase abstracta Vehicle, así como las clases Bike y Car como subclases de la primera. Para la clase Vehicle, crea los atributos de clase vehicles_created y total_kilometers, así como el atributo de instancia kilometers_traveled.

En la clase Vehicle crea un método para viajar (travel) que incremente los kilómetros recorridos.

En la clase Bike haz un método para hacer el caballito.

En la clase Car:

    Tendremos una variable de instancia con los litros de combustible que quedan en el deposito, inicialmente cero.
    Tendremos un método para quemar rueda y otro para llenar el depósito.
     Cuando el coche viaje disminuirá el número de litros en el depósito en relación a los kilómetros viajados. Si no hay combustible suficiente, el coche recorrerá únicamente los kilómetros que pueda.
    Para simplificar, cada kilómetro recorrido consumirá 0,1 litros de combustible, en un depósito caben 50 litros y quemar rueda consume 1 litro de combustible.

Prueba las clases creadas mediante un programa con un menú (usando la clase de la tanda anterior) como el que se muestra a continuación:
VEHÍCULOS
=========
1. Anda con la bicicleta.
2. Haz el caballito con la bicicleta.
3. Anda con el coche.
4. Quema rueda con el coche.
5. Llena el depósito del coche.
6. Ver kilometraje de la bicicleta.
7. Ver kilometraje del coche.
8. Ver el combustible que queda en el depósito del coche.
9. Ver kilometraje total.
10. Salir.

Elige una opción (1-8):
"""
from abc import ABC

from typeguard import typechecked


@typechecked
class Vehicle(ABC):
    vehicles = 0
    total_kilometers = 0

    def __init__(self):
        self.kilometers_traveled = 0
        Vehicle.vehicles += 1

    def travel(self, kilometers: float):
        self.kilometers_traveled += kilometers
        Vehicle.total_kilometers += kilometers
