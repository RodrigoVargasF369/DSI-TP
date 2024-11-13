from LogicaDeNegocio.Pais import Pais
from LogicaDeNegocio.Provincia import Provincia
from LogicaDeNegocio.RegionVitivinicola import RegionVitivinicola
from LogicaDeNegocio.Bodega import Bodega
from LogicaDeNegocio.Varietal import Varietal
from LogicaDeNegocio.Vino import Vino
from LogicaDeNegocio.Resenia import Resenia
from datetime import date


def datos():
    pais1 = Pais("Pais 1")
    pais2 = Pais("Pais 2")
    paises = [pais1, pais2]

    provincia1 = Provincia("Prov 1", pais1)
    provincia2 = Provincia("Prov 2", pais1)
    provincia3 = Provincia("Prov 4", pais2)
    provincia4 = Provincia("Prov 5", pais2)
    provincias = [provincia1, provincia2, provincia3, provincia4]

    region1 = RegionVitivinicola("Descripción1", "Region 1", provincia1)
    region2 = RegionVitivinicola("Descripción2", "Region 2", provincia2)
    region3 = RegionVitivinicola("Descripción3", "Region 3", provincia3)
    region4 = RegionVitivinicola("Descripción4", "Region 4", provincia4)
    regiones = [region1, region2, region3, region4]

    bodega1 = Bodega("Descripción 1", "Bodega 1", "a", "Bod 1", "c", region1)
    bodega2 = Bodega("Descripción 2", "Bodega 2", "a", "Bod 2", "c", region1)
    bodega3 = Bodega("Descripción 3", "Bodega 3", "a", "Bod 3", "c", region2)
    bodega4 = Bodega("Descripción 4", "Bodega 4", "a", "Bod 4", "c", region3)
    bodega5 = Bodega("Descripción 5", "Bodega 5", "a", "Bod 5", "c", region4)
    bodegas = [bodega1, bodega2, bodega3, bodega4, bodega5]

    varietal1 = Varietal("Varietal 1", 75, "Tipo uva 1")
    varietal2 = Varietal("Varietal 2", 38, "Tipo uva 2")
    varietal3 = Varietal("Varietal 3", 90, "Tipo uva 3")
    varietal4 = Varietal("Varietal 4", 46, "Tipo uva 4")
    varietal5 = Varietal("Varietal 5", 20, "Tipo uva 5")
    varietales = [varietal1, varietal2, varietal3, varietal4, varietal5]

    vino1 = Vino("Vino 1", 50, "", 5.7, 86715.24, varietal1, bodega1, [])
    vino2 = Vino("Vino 2", 90, "", 6.8, 47200.70, varietal2, bodega2, [])
    vino3 = Vino("Vino 3", 40, "", 7.1, 76800.22, varietal3, bodega3, [])
    vino4 = Vino("Vino 4", 30, "", 9.3, 20574.67, varietal4, bodega4, [])
    vino5 = Vino("Vino 5", 70, "", 2.8, 39864.88, varietal5, bodega5, [])
    vino6 = Vino("Vino 6", 60, "", 5.4, 12345.67, varietal1, bodega1, [])
    vino7 = Vino("Vino 7", 30, "", 3.8, 23456.78, varietal2, bodega2, [])
    vino8 = Vino("Vino 8", 85, "", 6.1, 34567.89, varietal3, bodega3, [])
    vino9 = Vino("Vino 9", 45, "", 8.8, 45678.90, varietal4, bodega4, [])
    vinoa = Vino("Vino A", 20, "", 9.1, 56789.01, varietal5, bodega5, [])
    vinob = Vino("Vino B", 50, "", 3.7, 67890.12, varietal1, bodega1, [])
    vinoc = Vino("Vino C", 95, "", 8.4, 78901.23, varietal2, bodega2, [])
    vinod = Vino("Vino D", 40, "", 4.6, 89012.34, varietal3, bodega3, [])
    vinoe = Vino("Vino E", 35, "", 4.6, 90123.45, varietal4, bodega4, [])
    vinof = Vino("Vino F", 75, "", 2.5, 99012.56, varietal5, bodega5, [])
    vinos = [
        vino1,
        vino2,
        vino3,
        vino4,
        vino5,
        vino6,
        vino7,
        vino8,
        vino9,
        vinoa,
        vinob,
        vinoc,
        vinod,
        vinoe,
        vinof,
    ]

    resenia1 = Resenia("Comentario 1", False, "2024-02-15", 2.3, vino1)
    resenia2 = Resenia("Comentario 2", False, "2024-03-24", 4.3, vino2)
    resenia3 = Resenia("Comentario 3", True, "2024-05-16", 1.1, vino3)
    resenia4 = Resenia("Comentario 4", False, "2024-03-24", 3.6, vino4)
    resenia5 = Resenia("Comentario 5", True, "2024-02-21", 2.2, vino5)
    
    resenia6 = Resenia("Comentario 6", True, "2024-02-18", 1.6, vino1)
    resenia7 = Resenia("Comentario 7", False, "2024-03-16", 2.7, vino2)
    resenia8 = Resenia("Comentario 8", False, "2024-02-02", 2.9, vino3)
    resenia9 = Resenia("Comentario 9", True, "2024-04-11", 4.7, vino4)
    resenia10 = Resenia("Comentario 10", False, "2024-04-20", 2.0, vino5)

    resenia11 = Resenia("Comentario 11", False, "2024-04-24", 3.1, vino1)
    resenia12 = Resenia("Comentario 12", True, "2024-02-12", 1.9, vino2)
    resenia13 = Resenia("Comentario 13", False, "2024-05-09", 2.6, vino3)
    resenia14 = Resenia("Comentario 14", True, "2024-01-21", 2.4, vino4)
    resenia15 = Resenia("Comentario 15", True, "2024-03-05", 4.8, vino5)

    resenia16 = Resenia("Comentario10", False, "2023-07-04", 4.7, vino5)
    resenia17 = Resenia("Comentario20", True, "2023-10-03", 1.4, vino8)
    resenia18 = Resenia("Comentario30", False, "2024-01-24", 0.9, vino6)
    resenia19 = Resenia("Comentario40", False, "2024-03-04", 1.9, vino9)
    resenia20 = Resenia("Comentario50", True, "2023-07-12", 1.1, vino9)

    resenia21 = Resenia("Comentario60", False, "2024-05-04", 4.2, vinof)
    resenia22 = Resenia("Comentario70", True, "2024-02-26", 3.3, vinof)
    resenia23 = Resenia("Comentario80", False, "2023-06-11", 0.7, vinod)
    resenia24 = Resenia("Comentario90", True, "2023-08-28", 1.0, vino3)
    resenia25 = Resenia("Comentario100", True, "2023-09-18", 3.2, vinob)

    resenia26 = Resenia("Comentario101", True, "2023-11-26", 3.5, vinoa)
    resenia27 = Resenia("Comentario102", True, "2023-07-05", 2.0, vinoc)
    resenia28 = Resenia("Comentario103", False, "2023-08-01", 3.8, vinoc)
    resenia29 = Resenia("Comentario104", True, "2023-10-23", 3.8, vino6)
    resenia30 = Resenia("Comentario105", False, "2024-01-10", 2.0, vinoa)
    
    resenia31 = Resenia("Comentario106", False, "2023-12-16", 1.8, vino9)
    resenia32 = Resenia("Comentario107", True, "2023-12-18", 4.0, vino3)
    resenia33 = Resenia("Comentario108", True, "2024-03-16", 4.0, vino2)
    resenia34 = Resenia("Comentario109", False, "2023-08-26", 1.4, vino1)
    resenia35 = Resenia("Comentario200", True, "2023-12-25", 1.2, vino8)

    resenias = [
        resenia1,
        resenia2,
        resenia3,
        resenia4,
        resenia5,
        resenia6,
        resenia7,
        resenia8,
        resenia9,
        resenia10,
        resenia11,
        resenia12,
        resenia13,
        resenia14,
        resenia15,
        resenia16,
        resenia17,
        resenia18,
        resenia19,
        resenia20,
        resenia21,
        resenia22,
        resenia23,
        resenia24,
        resenia25,
        resenia26,
        resenia27,
        resenia28,
        resenia29,
        resenia30,
        resenia31,
        resenia32,
        resenia33,
        resenia34,
        resenia35,
    ]

    return vinos
