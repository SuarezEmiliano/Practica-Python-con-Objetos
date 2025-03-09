class Mantenimiento:
    def __init__(self, nombreOperario, fecha, importeRespuestos):
        self.nombreOperario = nombreOperario
        self.fecha = fecha
        self.importeRespuestos = importeRespuestos

    def __str__(self):
        return f"OPERARIO:{self.nombreOperario} - FECHA:{self.fecha} - IMPORTE:{self.importeRespuestos}"
