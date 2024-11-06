def getAnio(fecha):
    return fecha[:4]


def getMes(fecha):
    return fecha[5:7]


def getDia(fecha):
    return fecha[8:10]


def main():
    fecha = "2024-06-18 17:13:59"
    print(getAnio(fecha))
    print(getMes(fecha))
    print(getDia(fecha))


if __name__ == "__main__":
    main()
