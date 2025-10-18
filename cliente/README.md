# Cliente Python para la API de Predicción – Dockerizado

## Presentado por
**Omar Alberto Torres**  
Estudiante de Ingeniería de Sistemas  
Proyecto Machine Learning: *Predictor en Actividades Bancarias*

## Entregado a
**Raúl Ramos Pollán, Jonathan Granda**  
Facultad de Ingeniería  
Universidad de Antioquia

## Fecha de entrega
Noviembre 23 de 2025

---

## Descripción del proyecto

Este proyecto complementa la API Flask principal (*Predict Bank*) con un **cliente Python** ejecutado dentro de su propio contenedor Docker.  
El cliente permite interactuar con la API de predicción a través de un **menú en consola**, sin necesidad de Postman u otras herramientas externas.  
Desde el menú, el usuario puede:

1. Entrenar el modelo de Machine Learning.
2. Ejecutar predicciones por archivo (`test.csv`).
3. Probar una predicción individual a partir de un registro JSON (`data.json`).

## Estructura del proyecto completo
```text
fase-3/
├── datos/ # Carpeta externa (inicialmente vacía)
│ # Se llenará con datasets, modelo y resultados
│
├── predict_bank/ # Contenedor del servidor Flask (API REST)
│ ├── app/
│ │ ├── apirest.py # API con endpoints /train, /predict_file, /predict_one
│ │ ├── train.py # Entrenamiento del modelo
│ │ ├── predict.py # Lógica de predicción
│ ├── Dockerfile # Imagen del servidor Flask
│ ├── requirements.txt # Dependencias del servidor
│ └── README.md # Documentación del API
│
└── cliente/ # Contenedor del cliente Python
├── cliente.py # Menú interactivo para consumir la API
├── Dockerfile # Imagen del cliente
└── README_cliente.md # Documentación del cliente
```
---

##  Construcción de la imagen Docker

Ubíquese en la raíz del proyecto del cliente (donde se encuentra el archivo `Dockerfile`) y ejecute el siguiente comando:

```bash
# Imagen
docker build -t predict_bank_client .


# ejecutando el cliente
Para ejecutar el cliente en modo interactivo, use

docker run -it --rm predict_bank_client

Debe salir un menu como el siguiente:
--- CLIENTE ML ---
1. Entrenar modelo
2. Predecir archivo
3. Predecir registro individual
4. Salir

# Al seleccionar
Seleccione una opción: 1
El proceso de entrenamiento del modelo puede demorar algunos minutos.

Entrenamiento completado
{'mensaje': 'Entrenamiento completado', 'metrics': None}

Seleccione una opción: 2
El proceso de predict, evalua el modelo con test.csv, al finalizar muestra algo como esto:

Predicción por archivo lista
{'mensaje': 'Predicción realizada con éxito', 'preview': [{'id': 750000, 'y': 0}, {'id': 750001, 'y': 0}, {'id': 750002, 'y': 0}, {'id': 750003, 'y': 0}, {'id': 750004, 'y': 1}]}

Se muestra algunas de las predicciones durante la prueb del modelo.

Seleccione una opcion: 3
Predicción individual
{'pred': 1, 'proba': 0.6749939364047577}

el modelo recibe una entrada en formato json, el modelo procesa la entrada y retorna la predicción

# Salir 
Seleccione una opción: 4
## Sale esto 
Saliendo del cliente...

# Gestion
Ver imagenes

docker ps -a

parar todos los docker

for /f "tokens=*" %i in ('docker ps -aq') do docker rm -f %i
```

Autor

Omar Alberto Torres
Proyecto: Predict Bank – Cliente Python
Universidad de Antioquia – Facultad de Ingeniería
Correo: omar.torresm@udea.edu.co

Teléfono: 304 344 0112




