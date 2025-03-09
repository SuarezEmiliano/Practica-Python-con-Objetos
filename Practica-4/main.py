from Empresa import Empresa


def main():
    empresa = Empresa()
    suma = empresa.suma_total()
    cantidad_sucursales_no_rentables = empresa.sucursales_no_rentables()
    numero_sucursal, tipo_sucursal = empresa.sucursal_mas_rentable()
    print(empresa)

    print(f"Total del resultado comercial de todas las sucursales: {suma}")
    print(f"Cantidad de sucursales no rentables: {cantidad_sucursales_no_rentables}")
    print(f"La sucursal de tipo {tipo_sucursal} con número {numero_sucursal} es la más rentable")



if __name__ == '__main__':
    main()
