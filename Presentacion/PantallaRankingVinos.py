from LogicaDeNegocio.GestorRankingVinos import GestorRankingVinos
from LogicaDeNegocio.auxFunc import *
from datetime import datetime, date

# python -m pip install PySimpleGUI para instalar PySimpleGUI
# Importamos la biblioteca PySimpleGUI
import PySimpleGUI as sg


class PantallaRankingVinos:
    def __init__(
        self,
        fechaDesde: date,
        fechaHasta: date,
        tipoResenia: str,
        tipoVisualizacion: str,
        btnConfirmar: bool,
    ) -> None:
        self.fechaDesde = fechaDesde
        self.fechaHasta = fechaHasta
        self.tipoResenia = tipoResenia
        self.tipoVisualizacion = tipoVisualizacion
        self.btnConfirmar = btnConfirmar

    # Métodos GET

    def __get_fechaDesde(self):
        return self.fechaDesde

    def __get_fechaHasta(self):
        return self.fechaHasta

    def __get_tipoResenia(self):
        return self.tipoResenia

    def __get_tipoVisualizacion(self):
        return self.tipoVisualizacion

    def __get_btnConfirmar(self):
        return self.btnConfirmar

    # Metodos SET

    def __set_fechaDesde(self, fechaDesde):
        self.fechaDesde = fechaDesde

    def __set_fechaHasta(self, fechaHasta):
        self.fechaHasta = fechaHasta

    def __set_tipoResenia(self, tipoResenia):
        self.tipoResenia = tipoResenia

    def __set_tipoVisualizacion(self, tipoVisualizacion):
        self.tipoVisualizacion = tipoVisualizacion

    def __set_btnConfirmar(self, btnConfirmar):
        self.btnConfirmar = btnConfirmar

    # Métodos de Negocio

    def tomarSelFechaDesde(self, fecha):
        self.__set_fechaDesde(fecha)

    def tomarSelFechaHasta(self, fecha):
        self.__set_fechaHasta(fecha)

    def tomarSelTipoResenia(self, tipoResenia):
        self.__set_tipoResenia(tipoResenia)

    def tomarSelTipoVisualizacion(self, tipoVisualizacion):
        self.__set_tipoVisualizacion(tipoVisualizacion)

    def tomarConfirmacionGenResenia(self, btnConfirmar):
        self.__set_btnConfirmar(btnConfirmar)

    def habilitarPantalla(self):
        # Inicicializamos el gestor de vinos
        GRV = GestorRankingVinos("", "", "", "", None)
        # Definimos el layout de la ventana
        layout = [
            # Titulo de la ventana
            [sg.Text("Menu de opciones")],
            # Grupo de botones de opciones
            [sg.Radio("Generar ranking de vinos", "group1", key="-RADIO1-")],
            # Botones para aceptar o cancelar la opcion seleccionada
            [sg.Button("Aceptar"), sg.Button("Cancelar")],
        ]

        # Creamos la ventana con el layout definido
        window = sg.Window("Menu de opciones", layout)

        while True:
            event, values = window.read()
            # Si se cierra la ventana o se presiona "Cancelar"...
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cancelar = True
                break
            # Al clickear para generar ranking de vinos:
            elif event == "Aceptar":
                if values["-RADIO1-"]:
                    GRV.opcionGenerarRankingVinos(self)
            window.close()

    def opcionGenerarRankingVinos(self):
        self.habilitarPantalla()

    def validarPeriodo(self, fechaDesde, fechaHasta):

        if (fechaDesde) > (fechaHasta):
            sg.Popup("Periodo invalido, cancelando operación")
            return False

        return True

    def solicitarSelFechaDesdeHasta(self, GRV):
        fechaDesde = None
        fechaHasta = None
        layout = [
            [sg.Text("Seleccione las fechas desde y hasta:")],
            [
                sg.CalendarButton("Desde", target="-CAL1-", key="-CAL1-"),
                sg.CalendarButton("Hasta", target="-CAL2-", key="-CAL2-"),
            ],
            [sg.Text(size=(20, 1), key="-DATE1-")],
            [sg.Text(size=(20, 1), key="-DATE2-")],
            [sg.Button("Aceptar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Seleccionar fechas", layout)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                break
            elif event == "-CAL1-":
                window["-DATE1-"].update(values["-CAL1-"])
            elif event == "-CAL2-":
                window["-DATE2-"].update(values["-CAL2-"])
            elif event == "Aceptar":
                fechaDesde = datetime.strptime(values["-CAL1-"][:10], "%Y-%m-%d").date()
                fechaHasta = datetime.strptime(values["-CAL2-"][:10], "%Y-%m-%d").date()

                # validar que la fecha hasta no sea posterior a la fecha actual, o asignar fecha actual como limite

                if not self.validarPeriodo(fechaDesde, fechaHasta):
                    sg.Popup("Periodo invalido, cancelando operación")
                    return None
                GRV.tomarSelFechaDesde(fechaDesde)
                GRV.tomarSelFechaHasta(fechaHasta)
                return None
        window.close()

        # Utiliza los metodos de Pantalla para setear los atributos
        self.tomarSelFechaDesde(fechaDesde)
        self.tomarSelFechaHasta(fechaHasta)
        # Retorna las fechas desde y hasta, para que el Gestor las utilice
        return fechaDesde, fechaHasta

    def solicitarSelTipoResenia(self, GRV):
        tipoResenia = None
        layout = [
            [sg.Text("Seleccionar tipo de resenia:")],
            [sg.Radio("Resenias normales", "group2", key="-RADIO4-")],
            [sg.Radio("Resenias de Sommelier", "group2", key="-RADIO5-")],
            [sg.Radio("Resenia de Amigos", "group2", key="-RADIO6-")],
            [sg.Button("Aceptar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Seleccionar tipo resenia", layout)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                break
            elif values["-RADIO4-"] == True:
                tipoResenia = "Normal"
            elif values["-RADIO5-"] == True:
                tipoResenia = "Sommelier"
            elif values["-RADIO6-"] == True:
                tipoResenia = "Amigos"
            break

        window.close()
        GRV.tomarSelTipoResenia(tipoResenia)
        return None

    def solicitarSelTipoVisualizacion(self, GRV):
        tipoVisualizacion = None
        layout = [
            [sg.Text("Seleccionar tipo de visualizacion:")],
            [sg.Radio("PDF (No implementado)", "group3", key="-RADIO7-")],
            [sg.Radio("Archivo Excel", "group3", key="-RADIO8-")],
            [sg.Radio("Pantalla", "group3", key="-RADIO9-")],
            [sg.Button("Aceptar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Seleccionar tipo visualizacion", layout)
        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                break
            elif values["-RADIO7-"] == True:
                tipoVisualizacion = "PDF"
            elif values["-RADIO8-"] == True:
                tipoVisualizacion = "Excel"
            elif values["-RADIO9-"] == True:
                tipoVisualizacion = "Pantalla"
            break

        window.close()
        GRV.tomarSelTipoVisualizacion(tipoVisualizacion)
        # return tipoVisualizacion
        return None

    def solicitarConfirmacionGenResenia(self, GRV):
        layout = [
            [sg.Text("¿Desea confirmar?:")],
            [sg.Button("Confirmar"), sg.Button("Rechazar")],
        ]
        window = sg.Window("Seleccionar Confirmacion", layout)
        confirmacion = None
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                break
            elif event == "Confirmar":
                confirmacion = True
            elif event == "Rechazar":
                confirmacion = False
            break
        window.close()

        GRV.tomarConfirmacionGenResenia(confirmacion)
        return None

    def mostrarRankingPorPantalla(self, vinosFinales, titulo, cabeceras):
        # Crear una ventana con un título y un tamanio determinado
        window = sg.Window(titulo)

        # Crear una tabla para mostrar los registros
        table = sg.Table(
            values=[],
            headings=cabeceras,  # reemplazar con los nombres de las columnas de los registros
            key="-TABLE-",
            justification="center",
            alternating_row_color="lightblue",
            num_rows=11,
        )

        # Crear un botón para cerrar la ventana
        close_button = sg.Button("Cerrar", key="-CLOSE-")

        # Crear un layout para la ventana
        layout = [[table], [close_button]]

        # Mostrar la ventana
        window.Layout(layout)

        # Agregar los registros a la tabla
        for vino in vinosFinales:
            table.Values.append(
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

        # Event loop para manejar los eventos de la ventana
        while True:
            event, values = window.read()
            if event == "-CLOSE-" or event == sg.WINDOW_CLOSED:
                break

        # Cerrar la ventana
        window.close()

    def informarCreacion(self):
        sg.Popup("El ranking ha sido creado exitosamente")
