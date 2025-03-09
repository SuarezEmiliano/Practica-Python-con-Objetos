from casa import Casa
from departamento import Departamento
import csv

class Inmobiliaria():
    def __init__(self):
        self.inmuebles = []
        self.cargar_datos_csv()

    def cargar_datos_csv(self):
        file = open('./inmuebles_100.csv', 'rt')
        for linea in file:
            campos = linea[:-1].split(',')
            tipo = int(campos[0])
            codigo = int(campos[1])
            nombre_propietario = campos[2]
            importe_base = float(campos[3])
            superficie = int(campos[4])
            if tipo == 1:
                cantidad_habitaciones = int(campos[5])
                tiene_pileta = int(campos[6])
                inmueble = Casa(codigo, nombre_propietario, superficie, importe_base, cantidad_habitaciones, tiene_pileta)
            else:
                importe_expensas = float(campos[5])
                numero_piso = int(campos[6])
                inmueble = Departamento(codigo, nombre_propietario,superficie, importe_base, importe_expensas, numero_piso)
            self.inmuebles.append(inmueble)
        file.close()

    def __str__(self):
        txt = "============INMUEBLES============\n"
        for inmueble in self.inmuebles:
            txt += str(inmueble) + "\n"
        txt += "=================================="
        return txt

    def suma_importe_alquileres(self):
        suma = 0
        for inmueble in self.inmuebles:
            suma += inmueble.get_importe_alquiler()
        return suma

    def cantidad_casas_premium(self):
        cantidad = 0
        for inmueble in self.inmuebles:
            if isinstance(inmueble, Casa):
                if inmueble.es_casa_premium():
                    cantidad +=1
        return cantidad

    def propietario_importe_mas_bajo(self):
        bandera = False
        for inmueble in self.inmuebles:
            if isinstance(inmueble, Departamento):
                if bandera == False:
                    menor = inmueble.get_importe_alquiler()
                    propietario = inmueble.nombre_propietario
                    bandera = True
                else:
                    if inmueble.get_importe_alquiler() < menor:
                        menor = inmueble.get_importe_alquiler()
                        propietario = inmueble.nombre_propietario
        return propietario