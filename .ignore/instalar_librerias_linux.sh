#!/bin/bash

# Script para instalar bibliotecas de Python en Linux

echo "Verificando si Python está instalado..."
if ! command -v python3 &> /dev/null
then
    echo "Python no está instalado. Por favor, instala Python antes de ejecutar este script."
    exit
fi

echo "Python detectado. Instalando bibliotecas necesarias..."

# Verificar Tkinter
echo "Verificando Tkinter..."
if ! python3 -c "import tkinter" &> /dev/null
then
    echo "Tkinter no está disponible en esta instalación de Python."
    echo "Intentando instalar Tkinter..."
    if command -v apt &> /dev/null; then
        sudo apt update
        sudo apt install -y python3-tk
    elif command -v yum &> /dev/null; then
        sudo yum install -y python3-tkinter
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3-tkinter
    else
        echo "No se puede instalar Tkinter automáticamente. Instálalo manualmente."
    fi
else
    echo "Tkinter está disponible."
fi

# Instalar bibliotecas con pip
LIBRARIES="PySimpleGUI openpyxl SQLAlchemy"

for LIB in $LIBRARIES
do
    echo "Instalando $LIB..."
    python3 -m pip install $LIB
done

echo "Todas las bibliotecas han sido instaladas."
