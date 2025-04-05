# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:39:54 2023

@author: ES45877372P
"""
import pandas as pd
import os
import re
import shutil
#ORGANIZADOR DOCUMENTOS Y CARPETAS

#Importamos el excel con los códigos
# df_datos=pd.read_excel('C:/Users/ES45877372P/Desktop/eDRD_BT_PROGRAMADAS_2022.xlsx',sheet_name='Muestra eDRD Programadas ',dtype=str)
df_datos=pd.read_excel('C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/OneDrive_1_19-4-2023/01_MT_eDRD/eDRD_MT_FUERZA MAYOR_2022.xlsx',sheet_name='Muestra MT FM',dtype=str)
# df_datos=pd.read_excel('C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/OneDrive_1_19-4-2023/01_MT_eDRD/eDRD_MT_GENERACIÓN_2022.xlsx',sheet_name='INCIDENCIAS MT GENERACIÓN',dtype=str)
# df_datos=pd.read_excel('C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/OneDrive_1_19-4-2023/01_MT_eDRD/eDRD_MT_PROGRAMADAS_2022.xlsx',sheet_name='MUESTRA MT PROGRAMADAS',dtype=str)
# df_datos=pd.read_excel('C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/OneDrive_1_19-4-2023/01_MT_eDRD/eDRD_MT_TERCEROS_2022.xlsx',sheet_name='MUESTRA MT TERCEROS',dtype=str)
# df_datos=pd.read_excel('C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/OneDrive_1_19-4-2023/02_BT_eDRD/eDRD_BT_PROGRAMADAS_2022.xlsx',sheet_name='Muestra eDRD Programadas',dtype=str)
# df_datos=pd.read_excel('C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/OneDrive_1_19-4-2023/02_BT_eDRD/eDRD_BT_IMPREVISTAS_2022.xlsx',sheet_name='Muestra eDRD Imprevistas',dtype=str)

# Ruta de la carpeta principal
# ruta_principal = r'C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/BT_PROG'
ruta_principal = r'C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/MT_FM'
# ruta_principal = r'C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/MT_GEN'
# ruta_principal = r'C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/MT_PROG'
# ruta_principal = r'C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/MT_TERC'
# ruta_principal = r'C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/BT_PROG'
# ruta_principal = r'C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/BT_TERC'

# Ruta de la carpeta con los documentos a mover
# ruta_documentos = os.path.join('C:/Users/ES45877372P/OneDrive - Enel Spa/ARCHIVOS_TRABAJO/ORGANIZADOR CARPETAS Y DOCS/BT_PROG_CATALUNYA')
ruta_documentos = os.path.join('C:/Users/ES45877372P/Desktop/DOCS MT FM')
# ruta_documentos = os.path.join('C:/Users/ES45877372P/Desktop/DOCS_MT_GEN')
# ruta_documentos = os.path.join('C:/Users/ES45877372P/Desktop/DOCS_MT_PROG')
# ruta_documentos = os.path.join('C:/Users/ES45877372P/Desktop/DOCS_MT_TERC')
# ruta_documentos = os.path.join('C:/Users/ES45877372P/Desktop/DOCS_BT_PROG')
# ruta_documentos = os.path.join('C:/Users/ES45877372P/Desktop/DOCS_BT_FM')

# Crea la carpeta principal si no existe
if not os.path.exists(ruta_principal):
    os.mkdir(ruta_principal)

# Agrupa los datos por identificador y referencia
grupos = df_datos.groupby(['ZONA', 'Referencia'])

# Itera sobre los grupos y crea las carpetas correspondientes
for (zona, referencia), _ in grupos:
    # Crea la carpeta para el identificador si no existe
    carpeta_identificador = os.path.join(ruta_principal, zona)
    if not os.path.exists(carpeta_identificador):
        os.mkdir(carpeta_identificador)
    
    # Crea la carpeta para la referencia si no existe
    carpeta_referencia = os.path.join(carpeta_identificador, referencia)
    if not os.path.exists(carpeta_referencia):
        os.mkdir(carpeta_referencia)

# Itera sobre los grupos y mueve los archivos correspondientes
for (zona, referencia), grupo in grupos:
    # Ruta de la carpeta correspondiente a la referencia
    carpeta_referencia = os.path.join(ruta_principal, zona, referencia)
    
    # Itera sobre los archivos en la carpeta de documentos
    for archivo in os.listdir(ruta_documentos):
        # Busca el número de referencia en el nombre del archivo
        if re.search(referencia, archivo):
            # Ruta completa del archivo a mover
            ruta_origen = os.path.join(ruta_documentos, archivo)
            
            # Ruta completa de destino del archivo
            ruta_destino = os.path.join(carpeta_referencia, archivo)
            
            # Mueve el archivo a la carpeta correspondiente
            shutil.move(ruta_origen, ruta_destino)

#Carpetas vacias
# Lista de carpetas vacías
carpetas_vacias = []

# Itera sobre los grupos y verifica si las carpetas están vacías
for (zona, referencia), _ in grupos:
    # Ruta de la carpeta correspondiente a la referencia
    carpeta_referencia = os.path.join(ruta_principal, zona, referencia)
    
    # Verifica si la carpeta está vacía
    if not os.listdir(carpeta_referencia):
        carpetas_vacias.append(os.path.basename(carpeta_referencia))

# Imprime la lista de carpetas vacías
print(carpetas_vacias)


























