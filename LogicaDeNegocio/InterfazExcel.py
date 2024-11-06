import openpyxl


class InterfazExcel:
    def __init__(self) -> None:
        self

    def generarArchivo(self, vinosFinales, nombre_archivo, cabeceras=None):
        # Crear un libro de Excel
        wb = openpyxl.Workbook()

        # Seleccionar la hoja activa
        ws = wb.active

        # Asignar las cabeceras si se proporcionaron
        if cabeceras is not None:
            ws.append(cabeceras)

        # Agregar los registros a la hoja
        for vino in vinosFinales:
            ws.append(
                [
                    vino["nombre"],
                    vino["puntaje"],
                    vino["precio"],
                    vino["nombreBodega"],
                    vino["varietal"],
                    vino["nombreRegionVitivinicola"],
                    vino["nombrePais"],
                ]
            )
        # Guardar el archivo
        wb.save(nombre_archivo)
