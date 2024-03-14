"""
Autor: Luis Pérez Cantarero

Date: 27/02/2024

Bici
"""
from vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.__wheelie = "            o       _      _          _\n" \
            + "   _o      /\\_    _ \\\\o   (_)\\__/o   (_)\n" \
            + " _< \\_    _>(_)  (_)/<_     \\_| \\    _|/' \\/\n" \
            + "(_)>(_)  (_)         (_)    (_)     (_)'  _\\o_\n" \
            + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1DAW~~\n"

    def wheelie(self):
        print(self.__wheelie)
