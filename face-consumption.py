# Consumo de la FACE API de Azure para obtener información de rostros
# Para más información consulta: https://docs.microsoft.com/es-mx/rest/api/face/
import json, os, requests, pprint
from IPython.core.display import Image, display


# Obtener el API KEY de la aplicación
subscription_key = "AQUÍ_PONES_TU_CLAVE_DEL_RECURSO_DE_AZURE"

# Obtener el endpoint de la aplicación
face_api_url = "AQUÍ_PONES_TU_URL_DESTINO_DEL_RECURSO_DE_AZURE" + '/face/v1.0/detect'

image_url = 'AQUÍ_PONES_TU_IMAGEN'
# Imagen de prueba: https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg

# Headers necesarios para que funcione la aplicación
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

# Parametros que se utilizan en la llamada de la API
params = {
    'returnFaceId': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion'
}

# Aquí se hace la petición al servicio de FACE API de Azure
response = requests.post(
    face_api_url, params=params,
    headers=headers, json={"url": image_url}
)

# Muestras la imagen 
display(Image(url = image_url, width = 500, unconfined = True))

# Aquí obtienes tu edad
print("Edad " + str(response.json()[0]['faceAttributes']['age']))
# Aquí obtienes tu genero
print("Genero " + str(response.json()[0]['faceAttributes']['gender']))
# Aquí obtienes si usas lentes o no
print("¿Lentes?: " + str(response.json()[0]['faceAttributes']['glasses']))

# Aquí oobtienes el listado de emociones
emociones = response.json()[0]['faceAttributes']['emotion']

# Aquí obtenemos la emoción predominante de acuerdo a la probabilidad que nos arroja FACE API
listaEmociones = []
for e in emociones.keys() :
    listaEmociones.append(e)

listaProbabilidades = []
for e in emociones.values() :
    listaProbabilidades.append(e)
m = max(listaProbabilidades)
indexMax = [i for i, j in enumerate(listaProbabilidades) if j == m]

# Imprimimos la emoción predominante
print("Emoción predominante: " + str(listaEmociones[indexMax[0]]))
