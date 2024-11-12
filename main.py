# python -m pip install tkinter
# python -m pip install PySimpleGUI
# python -m pip install openpyxl
# python -m pip install SQLAlchemy

import PySimpleGUI as sg
from Presentacion.PantallaRankingVinos import PantallaRankingVinos


def main():

    PRV = PantallaRankingVinos("", "", "", "", False)
    PRV.opcionGenerarRankingVinos()


if __name__ == "__main__":
    main()
