import numpy as np #librería en la que se define un tipo de dato que representa matrices multidimensionales
# además incluye algunas funcionalidades básicas para trabajar con ellas

import os  #libreria para el acceso portable a funciones específicas del sistema operativo
import cv2 #OpenCV es una biblioteca libre de visión artificial originalmente desarrollada por Intel

import glob #libreria usada como módulo que encuentra todos los nombres de ruta que coinciden con un patrón
# específico de acuerdo con las reglas utilizadas por el shell de Unix.
import json # libreria que se usa para guardar listas en un archivo en este caso tipo json.



CHECKERBOARD = (5,7)  # Patron de esquinas que se buscara en las fotos tomadas

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# Preparar los objetos con las dimensiones dependientes del patron de esquinas fijado
objp = np.zeros((CHECKERBOARD[0]*CHECKERBOARD[1] , 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[1], 0:CHECKERBOARD[0]].T.reshape(-1, 2)

# Matrices para almacenar puntos de objeto y puntos de imagen de todas las imágenes.
objpoints = []  # Puntos 3D en el espacio del mundo real
imgpoints = []  # Puntos 2D en la imagen.

# ruta de la carpeta donde se encuentran las imagenes
path = "C:/Users/Steven/Documents/8 semestre/Procesamiento de imagenes/taller5ce"

#Busca todas las imagenes que comiencen en "c" y de formato jpg  en la carpeta dicha.
path_file = os.path.join(path, 't*.jpg')
images = glob.glob(path_file)

# Se recorre cada imagen encontrada
for fname in images:
    image = cv2.imread(fname) # Se carga la imagen que corresponda con el item del for


    scale_percent = 21  # porcentaje de la imagen original
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)   # dimensiones nuevas
    # Se reduce el tamaño de la imagen
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # Se transforma la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Busca esquinas con el patron de dado
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    # si encuentra el patron, agrega puntos de objeto , puntos de imagen
    if ret == True:

        objpoints.append(objp) # agrega los puntos de objeto

        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)# agrega los puntos de imagen

        #Dibuja las el patron encontrado en la imagen original
        # img = cv2.drawChessboardCorners(image, CHECKERBOARD, corners2, ret)
        # cv2.imshow('img', img)
        # cv2.waitKey(250)

#Se cierran las ventanas
cv2.destroyAllWindows()
#
# se calibra la camara
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# se imprime la matriz de
print(mtx)


#Nombre del archivo json
file_name = 'calibration.json'

#Se guarda la matriz K en el archivo json
json_file = os.path.join(path, file_name)

data = {
    'K': mtx.tolist(),
}

with open(json_file, 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=1, ensure_ascii=False)

