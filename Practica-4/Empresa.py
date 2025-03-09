import csv
from Hiper import Hiper
from Mini import Mini
from Super import Super


class Empresa:
    def __init__(self):
        self.sucursales = []
        self.cargar_sucursales_csv()

    def cargar_sucursales_csv(self):
        file = open('./sucursales.csv', 'rt')
        for line in file:
            campos = line[:-1].split(',')
            tipo = int(campos[0])
            numero = campos[1]
            superficie = int(campos[2])
            facturacion = float(campos[3])
            if tipo == 1:
                importe_ganado_alquiler = float(campos[4])
                sucursal = Hiper(numero, superficie,facturacion, importe_ganado_alquiler)
            elif tipo == 2:
                es_mayorista = float(campos[4])
                sucursal = Super(numero, superficie, facturacion, es_mayorista)
            else:
                importe_pagado_alquiler = float(campos[4])
                sucursal = Mini(numero, superficie, facturacion, importe_pagado_alquiler)
            self.sucursales.append(sucursal)
        file.close()

    def __str__(self):
        txt = '=========DATOS DE LAS SUCURSALES=========' + "\n"
        for sucursal in self.sucursales:
            txt = txt + str(sucursal) + "\n"
        txt += '=========================================' + "\n"
        return txt

    def suma_total(self):
        suma = 0
        for sucursal in self.sucursales:
            suma += sucursal.get_resultado_comercial()
        return suma

    def sucursales_no_rentables(self):
        cantidad_sucursales = 0
        for sucursal in self.sucursales:
            if not sucursal.es_rentable():
                cantidad_sucursales += 1
        return cantidad_sucursales

    def sucursal_mas_rentable(self):
        mayor = 0
        numero_mayor= 0
        tipo_mayor = 0
        tipo = 0
        for sucursal in self.sucursales:
            tipo = sucursal.get_tipo()
            if sucursal.get_indice_rentabilidad() > mayor:
                mayor = sucursal.get_indice_rentabilidad()
                numero_mayor = sucursal.numero
                tipo_mayor = tipo
        return numero_mayor, tipo_mayor