@echo off
REM Script para instalar bibliotecas de Python en Windows

echo Verificando si Python está instalado...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python no está instalado o no está en la variable de entorno PATH.
    echo Por favor, instala Python y agrega Python al PATH antes de ejecutar este script.
    pause
    exit /b
)

echo Python detectado. Instalando bibliotecas necesarias...

REM Verificar Tkinter
echo Verificando Tkinter...
python -c "import tkinter" >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Tkinter no está disponible en esta instalación de Python.
    echo Asegúrate de que Tkinter está incluido en tu instalación de Python.
) ELSE (
    echo Tkinter está disponible.
)

REM Lista de bibliotecas a instalar
set LIBRARIES=PySimpleGUI openpyxl SQLAlchemy

REM Instalar cada biblioteca
for %%L in (%LIBRARIES%) do (
    echo Instalando %%L...
    python -m pip install %%L
)

echo Todas las bibliotecas han sido instaladas.
pause
