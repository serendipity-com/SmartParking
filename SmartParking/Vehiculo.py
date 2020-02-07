# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:03:33 2020

@author: Crist
"""
from datetime import datetime

class Vehiculo:
    
    placa = ""
    tipo = ""
    #El formato de los datos en la lista es hora, minutos, dia, mes, año
    datosEntrada = ""
    datosSalida = ""
    tiempoTranscurrido = 0 #Es en horas
    valor = 0
    
    def __init__(self, placa, tipo):
        
        self.placa = placa
        self.tipo = tipo
        
        #Agregamos los datos de hora y fecha de ingreso
        self.datosEntrada = datetime.now()
    
    def calcularTiempo(self):
        
        #Agregamos los datos de hora y fecha de salida
        self.datosSalida = datetime.now();
        tiempo = self.datosSalida - self.datosEntrada
        
        print(round((tiempo.seconds / 360 ), 2))
        
    #def calcularValor(self, tarifa):
        
    
    def mostrarHora(self):
        
        print(self.datosEntrada)
        print(type(self.datosEntrada))    