
import os  #libreria para el acceso portable a funciones específicas del sistema operativo
import json # libreria que se usa para guardar listas en un archivo en este caso tipo json.



# se abre el archivo donde esta guardad la matriz de parametros intrinsecos
path = "C:/Users/Steven/Documents/8 semestre/Procesamiento de imagenes/taller5ce"
file_name = 'calibration.json'
json_file = os.path.join(path, file_name)

with open(json_file) as fp:
    json_data = json.load(fp)

k=json_data["K"]
print(k)
# Se crea el archivo calibra.json donde se guarda la matriz K, tilt, pan, d y h
path = "C:/Users/Steven/Documents/8 semestre/Procesamiento de imagenes/taller5ce"
file_name = 'calibra.json'
json_file = os.path.join(path, file_name)
tilt=0
pan=5
d=2
h=1
data = {
    'K': k,
    'tilt':tilt,
    'pan' :pan,
     'd':d,
     'h':h
}
with open(json_file, 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=1, ensure_ascii=False)



