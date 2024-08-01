import pandas as pd
import os

excel_file = "model.xlsx"

df = pd.read_excel(excel_file,  usecols='D, E, F' )

apellido = ''
nombre = ''
legajo = ''


def crearCarpeta(nombre, apellido, legajo):

    directory = f"{nombre}_{apellido}_{legajo}"

    parent_dir = r"C:\Users\name\Desktop\folder"  
    

    path = os.path.join(parent_dir, directory)

    try: 
        os.makedirs(path, exist_ok = True) 
        print("Carpeta '%s' creada" % directory) 

    except OSError as error: 
        print("Carpeta '%s' no se puede crear" % directory) 


def leerArchivo(df):

        for index, row in df.iterrows(): 
                apellido = row.iloc[0]
                nombre = row.iloc[1]
                legajo = row.iloc[2]

                crearCarpeta(nombre, apellido, legajo)



leerArchivo(df)
print("Secuencia completada.")
