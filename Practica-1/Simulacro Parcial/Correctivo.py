from Mantenimiento import Mantenimiento


class Correctivo(Mantenimiento):
    def __init__(self, nombreOperario, fecha, importeRespuestos, horasParada, importeTecnico):
        super().__init__(nombreOperario, fecha, importeRespuestos)
        self.horasParada = horasParada
        self.importeTecnico = importeTecnico

    def __str__(self):
        mant_str = super().__str__()
        str = f"<< PREVENTIVO >> {mant_str} -> INSUMOS:{self.horasParada} - RESULTADO:{self.importeTecnico}"
        return str

    def get_gastos(self):
        return self.importeTecnico + self.importeRespuestos

    def get_duracion(self):
        return self.horasParada
