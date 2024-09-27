from Empresa import Empresa


def main():
    empresa = Empresa()
    print(empresa)
    costo_total = empresa.get_costo_total()
    vehiculo_costo_mas_alto, costo_mas_alto = empresa.get_costo_mas_alto()
    cantidad_camionetas_mas_carga = empresa.camionetas_mas_carga()
    cantidad_motos_alta_cilindrica = empresa.motos_alta_cilindrica()


    print(f"EL COSTO TOTAL DE MANTENIMIENTO DE TODOS LOS VEHÍCULOS ES: {costo_total}")
    print(f"CAMIONETA CON MANTENIMIENTO MÁS CARO: {vehiculo_costo_mas_alto} , CON UN VALOR DE {costo_mas_alto}")
    print(f"LA CANTIDAD DE CAMIONETA CON MÁS DE 1000kg DE CAPACIDAD DE CARGA ES: {cantidad_camionetas_mas_carga}")
    print(f"LA CANTIDAD DE MOTOS DE ALTA CILINDRICA ES: {cantidad_motos_alta_cilindrica}")

if __name__ == '__main__':
    main()