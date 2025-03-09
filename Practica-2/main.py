from inmobiliaria import Inmobiliaria


def main():
    inmobiliaria = Inmobiliaria()
    print(inmobiliaria)
    suma = inmobiliaria.suma_importe_alquileres()
    cantidad_casas_premium = inmobiliaria.cantidad_casas_premium()
    propietario_importe_mas_bajo = inmobiliaria.propietario_importe_mas_bajo()

    print(f"El total a recaudar en concepto de alquileres si todos los inmuebles se encuentran alquilados es: {suma} ")
    print(f"Cantidad de casas premium: {cantidad_casas_premium}")
    print(f"Propietario con el importe más bajo: {propietario_importe_mas_bajo}")



if __name__ == '__main__':
    main()

