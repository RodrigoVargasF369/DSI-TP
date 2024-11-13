from LogicaDeNegocio.Pais import Pais
from LogicaDeNegocio.Provincia import Provincia
from LogicaDeNegocio.RegionVitivinicola import RegionVitivinicola
from LogicaDeNegocio.Bodega import Bodega
from LogicaDeNegocio.Varietal import Varietal
from LogicaDeNegocio.Vino import Vino
from LogicaDeNegocio.Resenia import Resenia
from datetime import date

def datos():
    # Países
    pais1 = Pais("Argentina")
    pais2 = Pais("Chile")
    paises = [pais1, pais2]

    # Provincias
    provincia1 = Provincia("Mendoza", pais1)
    provincia2 = Provincia("San Juan", pais1)
    provincia3 = Provincia("Maipo", pais2)
    provincia4 = Provincia("Casablanca", pais2)
    provincias = [provincia1, provincia2, provincia3, provincia4]

    # Regiones Vitivinícolas
    region1 = RegionVitivinicola("Famosa por sus Malbec", "Valle de Uco", provincia1)
    region2 = RegionVitivinicola("Área de buen Cabernet", "Pedernal", provincia2)
    region3 = RegionVitivinicola("Clima ideal para Carmenere", "Valle Central", provincia3)
    region4 = RegionVitivinicola("Viñas costeras", "Casablanca", provincia4)
    regiones = [region1, region2, region3, region4]

    # Bodegas
    bodega1 = Bodega("34° 36' S 68° 19' W", "Bodega Familiar", "Fundada en 1960", "Viña Monte", "Trimestral", region1)
    bodega2 = Bodega("31° 32' S 68° 31' W", "Productor de tintos", "Desde 1980", "El Pedernal", "Mensual", region1)
    bodega3 = Bodega("33° 24' S 70° 40' W", "Especialidad en tintos", "Fundada en 1975", "Viña Carmen", "Semestral", region2)
    bodega4 = Bodega("33° 19' S 71° 24' W", "Viñas a nivel del mar", "Desde 1992", "Casa Blanca", "Anual", region3)
    bodega5 = Bodega("33° 13' S 73° 20' W", "Productor de tintos", "Desde 1970", "Viña Rosa", "Cuatrimestral", region4)
    bodegas = [bodega1, bodega2, bodega3, bodega4, bodega5]

    # Varietales
    varietal1 = Varietal("Malbec 75%", 75, "Malbec")
    varietal2 = Varietal("Cabernet Sauvignon 38%", 38, "Cabernet Sauvignon")
    varietal3 = Varietal("Carmenere 90%", 90, "Carmenere")
    varietal4 = Varietal("Chardonnay 46%", 46, "Chardonnay")
    varietal5 = Varietal("Merlot 20%", 20, "Merlot")
    varietales = [varietal1, varietal2, varietal3, varietal4, varietal5]

    # Vinos
    vinos = [
        Vino("Vino Monte Malbec", 2019, "URLHostImagen/imagen", 5.7, 86715.24, varietal1, bodega1, []),
        Vino("El Pedernal Gran Cabernet", 2020, "URLHostImagen/imagen", 6.8, 47200.70, varietal2, bodega2, []),
        Vino("Carmenere Reserva", 2018, "URLHostImagen/imagen", 7.1, 76800.22, varietal3, bodega3, []),
        Vino("Casablanca Chardonnay", 2021, "URLHostImagen/imagen", 9.3, 20574.67, varietal4, bodega4, []),
        Vino("Mendoza Gran Malbec", 2020, "URLHostImagen/imagen", 2.8, 39864.88, varietal5, bodega5, []),
        Vino("Pedernal Syrah Blend", 2019, "URLHostImagen/imagen", 5.4, 12345.67, varietal1, bodega1, []),
        Vino("Central Valley Merlot", 2017, "URLHostImagen/imagen", 3.8, 23456.78, varietal2, bodega2, []),
        Vino("Blanco Costero Chardonnay", 2022, "URLHostImagen/imagen", 6.1, 34567.89, varietal3, bodega3, []),
        Vino("Carmen Gran Reserva", 2019, "URLHostImagen/imagen", 8.8, 45678.90, varietal4, bodega4, []),
        Vino("El Pedernal Premium", 2018, "URLHostImagen/imagen", 9.1, 56789.01, varietal5, bodega5, []),
        Vino("Monte Alto Cabernet", 2020, "URLHostImagen/imagen", 3.7, 67890.12, varietal1, bodega1, []),
        Vino("Mendoza Chardonnay Especial", 2021, "URLHostImagen/imagen", 8.4, 78901.23, varietal2, bodega2, []),
        Vino("Syrah Selection", 2018, "URLHostImagen/imagen", 4.6, 89012.34, varietal3, bodega3, []),
        Vino("Reserva Sauvignon", 2017, "URLHostImagen/imagen", 4.6, 90123.45, varietal4, bodega4, []),
        Vino("Blanco de Viñas", 2022, "URLHostImagen/imagen", 2.5, 99012.56, varietal5, bodega5, []),
    ]

    # Reseñas
    resenias = [
        Resenia("Excelente Malbec de altura", False, date(2024, 2, 15), 2.3, vinos[0]),
        Resenia("Cabernet con carácter", False, date(2024, 3, 24), 4.3, vinos[1]),
        Resenia("Gran elección para carne", True, date(2024, 5, 16), 1.1, vinos[2]),
        Resenia("Chardonnay muy frutal", False, date(2024, 3, 24), 3.6, vinos[3]),
        Resenia("Delicioso y bien estructurado", True, date(2024, 2, 21), 2.2, vinos[4]),

        Resenia("Aromas intensos", True, date(2024, 2, 18), 1.6, vinos[0]),
        Resenia("Buen vino con buen final", False, date(2024, 3, 16), 2.7, vinos[1]),
        Resenia("Frescura de Chardonnay", False, date(2024, 2, 2), 2.9, vinos[2]),
        Resenia("Muy buena calidad", True, date(2024, 4, 11), 4.7, vinos[3]),
        Resenia("Calidad premium", False, date(2024, 4, 20), 2.0, vinos[4]),

        Resenia("Cuerpo y sabor intenso", False, date(2024, 4, 24), 3.1, vinos[0]),
        Resenia("Elegante Chardonnay", True, date(2024, 2, 12), 1.9, vinos[1]),
        Resenia("Notas ahumadas", False, date(2024, 5, 9), 2.6, vinos[2]),
        Resenia("Frutal y refrescante", True, date(2024, 1, 21), 2.4, vinos[3]),
        Resenia("Estructura compleja", True, date(2024, 3, 5), 4.8, vinos[4]),

        Resenia("Delicado pero robusto", False, date(2023, 7, 4), 4.7, vinos[4]),
        Resenia("Perfecto para cena", True, date(2023, 10, 3), 1.4, vinos[7]),
        Resenia("Agradable al paladar", False, date(2024, 1, 24), 0.9, vinos[5]),
        Resenia("Exquisito sabor", False, date(2024, 3, 4), 1.9, vinos[8]),
        Resenia("Inigualable", True, date(2023, 7, 12), 1.1, vinos[8]),

        Resenia("Muy refrescante", False, date(2024, 5, 4), 4.2, vinos[14]),
        Resenia("Aroma frutal intenso", True, date(2024, 2, 26), 3.3, vinos[14]),
        Resenia("Notas de madera", False, date(2023, 6, 11), 0.7, vinos[12]),
        Resenia("Elegante y sutil", True, date(2023, 8, 28), 1.0, vinos[2]),
        Resenia("Toques florales", True, date(2023, 9, 18), 3.2, vinos[10]),

        Resenia("Perfecto con carnes", True, date(2023, 11, 26), 3.5, vinos[9]),
        Resenia("Ideal para cenas", True, date(2023, 7, 5), 2.0, vinos[11]),
        Resenia("Ligero y refrescante", False, date(2023, 8, 1), 3.8, vinos[11]),
        Resenia("Balanceado y suave", True, date(2023, 10, 23), 3.8, vinos[5]),
        Resenia("Sabor persistente", False, date(2024, 1, 10), 2.0, vinos[9]),

        Resenia("Delicada textura", False, date(2023, 12, 16), 1.8, vinos[8]),
        Resenia("Robusto y elegante", True, date(2023, 12, 18), 4.0, vinos[2]),
        Resenia("Perfecto equilibrio", True, date(2024, 3, 16), 4.0, vinos[1]),
        Resenia("Ideal para celebrar", False, date(2023, 8, 26), 1.4, vinos[0]),
        Resenia("Sabores complejos", True, date(2023, 12, 25), 1.2, vinos[7]),
    ]

    return vinos
