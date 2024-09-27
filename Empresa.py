from Auto import Auto
from Camioneta import Camioneta
from Moto import Moto
import csv


class Empresa:
    def __init__(self):
        self.vehiculos = []
        self.cargar_datos_csv()

    def cargar_datos_csv(self):
        file = open('./vehiculos.csv', 'rt')
        for line in file:
            campos = line[:-1].split(',')
            tipo = int(campos[0])
            marca = campos[1]
            matricula = campos[2]
            modelo = int(campos[3])
            costo_base = int(campos[4])
            if tipo == 1:
                kilometraje = int(campos[5])
                vehiculo = Auto(matricula, marca, modelo, costo_base, kilometraje)
            elif tipo == 2:
                capacidad_carga = int(campos[5])
                vehiculo = Camioneta(matricula, marca, modelo, costo_base, capacidad_carga)
            else:
                cilindrica = int(campos[5])
                vehiculo = Moto(matricula, marca, modelo, costo_base, cilindrica)
            self.vehiculos.append(vehiculo)
        file.close()

    def __str__(self):
        txt = "=======DATOS ARCHIVOS=======\n"
        for vehiculo in self.vehiculos:
            txt += str(vehiculo) + "\n"
        txt +="============================"
        return txt

    def get_costo_total(self):
        costo_total = 0
        for vehiculo in self.vehiculos:
            costo_total += vehiculo.get_costo()
        return costo_total

    def get_costo_mas_alto(self):
        costo_mas_alto = 0
        vehiculo_mayor = self.vehiculos[0]
        for vehiculo in self.vehiculos:
            if vehiculo.get_costo() > costo_mas_alto:
                costo_mas_alto = vehiculo.get_costo()
                vehiculo_mayor = vehiculo
        return vehiculo_mayor, costo_mas_alto

    def camionetas_mas_carga(self):
        contador = 0
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, Camioneta) and vehiculo.capacidad_carga > 1000:
                contador += 1
        return contador

    def motos_alta_cilindrica(self):
        contador = 0
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, Moto) and vehiculo.cilindrica > 500:
                contador += 1
        return contador