import requests  # Importar la biblioteca requests para hacer solicitudes HTTP
import csv  # Importar la biblioteca csv para trabajar con archivos CSV
import time  # Importar la biblioteca time para manejar intervalos de tiempo

while True:  # Bucle infinito para ejecutar la tarea repetidamente
    response = requests.get('http://localhost:5000/data')  # Hacer una solicitud GET a la API
    data = response.json()  # Obtener los datos en formato JSON
    with open('data.csv', mode='w') as file:  # Abrir un archivo CSV en modo escritura
        writer = csv.writer(file)  # Crear un escritor de CSV
        writer.writerow(['Column1', 'Column2'])  # Escribir los encabezados de las columnas
        for row in data:  # Iterar sobre los datos obtenidos
            writer.writerow(row)  # Escribir cada fila en el archivo CSV
    time.sleep(3600)  # Esperar una hora antes de la siguiente ejecución
