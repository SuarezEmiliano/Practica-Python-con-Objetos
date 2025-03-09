from Maquina import Maquina


def main():
    maquina = Maquina()
    print(maquina)

    print(f"Costo total de los mantenimientos: {maquina.suma_gastos()}")
    print(f"Cantidad de mantenimientos 'caros': {maquina.cant_mantenimientos_caros()}")
    maquina.rotura_mas_larga()

if __name__ == "__main__":
    main()
