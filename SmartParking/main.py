# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:54:21 2020

@author: Crist
"""

from Vehiculo import *

if __name__ == '__main__':
    a = Vehiculo("AUO448", int(1))
    a.mostrarHora()
    b = input("a: ")
    a.calcularTiempo()
