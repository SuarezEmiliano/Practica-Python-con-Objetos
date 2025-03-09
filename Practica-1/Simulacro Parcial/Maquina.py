
import csv

from Correctivo import Correctivo
from Preventivo import Preventivo


class Maquina:
    def __init__(self):
        self.mantenimientos = []
        self.cargar_datos_desde_csv()


    def cargar_datos_desde_csv(self):
        file = open('./mantenimientos.csv','rt')
        for linea in file:
            #Se saca el salto de línea con el -1
            campos = linea[:-1].split(',')
            tipo = int(campos[0])
            fecha = campos[1]
            nombreOperario = campos[2]
            importeRespuestos = float(campos[3])
            if tipo == 1:
                resultado = int(campos[4])
                importeInsumos = float(campos[5])
                mantenimiento = Preventivo(fecha, nombreOperario, importeRespuestos , resultado, importeInsumos)
            else:
                horasParada = int(campos[4])
                importeTecnico = float(campos[5])
                mantenimiento = Correctivo(fecha, nombreOperario, importeRespuestos, horasParada, importeTecnico)
            self.mantenimientos.append(mantenimiento)
        file.close()

    def suma_gastos(self):
        suma = 0
        for mant in self.mantenimientos:
            suma += mant.get_gastos()
        return suma

    def cant_mantenimientos_caros(self):
        cantidad = 0
        for mant in self.mantenimientos:
            if mant.get_gastos() > 10000:
                cantidad += 1
        return cantidad

    def rotura_mas_larga(self):
        #Defino la mayor duracion como 0 para recorrer e ir encontrando el mayor
        mayor_duracion = 0
        #Defino operario y fecha para poder definirlos cuando encuentro uno mayor al actual
        operario = None
        fecha = None

        #Recorro todos los mantenimientos
        for m in self.mantenimientos:
            #Ya que el preventivo no tiene horasParada, utilizamos isinstance
            if isinstance(m,Correctivo):
                if (m.horasParada > mayor_duracion):
                    mayor_duracion = m.horasParada
                    operario = m.nombreOperario
                    fecha = m.fecha
        #Puede que en el archivo no haya mantenimientos correctivos
        if mayor_duracion != 0:
            print(f"El mantenimiento correctivo más largo demandó {mayor_duracion} horas, fué realizado por {operario} en fecha {fecha}")
        else:
            print ("No hubo mantenimientos correctivos con duración mayor a 0")

    def __str__(self):
        txt = "--- INFORME DE MANTENIMENTOS ---\n"
        for mant in self.mantenimientos:
            txt += str(mant)+"\n"
        txt += "--- ######################## ---"
        return txt
