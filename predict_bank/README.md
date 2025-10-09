# Predicción con Modelo de Machine Learning – Dockerizado

## Presentado por
**Omar Torres**  
Estudiante de Ingeniería de Sistemas  
Proyecto Machine Learning: *Predictor en Actividades Bancarias*

## Entregado a
**Raul Ramos Pollan, Jonathan Granda**  
Facultad de Ingeniería  
Universidad de Antioquia

## Fecha de entrega
Octubre 23 de 2025

---

## Descripción del proyecto

Este proyecto implementa un modelo de Machine Learning en Python para predecir el resultado de ciertas actividades bancarias.  
El modelo y el flujo de predicción se ejecutan dentro de un contenedor Docker, lo cual garantiza un entorno limpio y reproducible.

## Nota 1
El profesor debe descargar el repositorio ubicado en la siguiente dirección
```bash
https://github.com/hombremono873/entrega_fase_2_con_descarga_kaggle.git

```
## Nota 2
```bash
El profesor debe unirse a la competencia de Kaggle fuente de este trabajo en los enlaces,

https://www.kaggle.com/competitions/playground-series-s5e8/overview
https://www.kaggle.com/competitions/playground-series-s5e8/data

```
El profesor debe obtener un token de acceso "kaggle.json" para acceder a los datasets 
train.csv, test.csv.
Debe ubicarse el archivo kaggle.json a la misma altura del archivo Dockerfile dentro de la carpeta,
predick_bank.

---

## Requisitos previos

- Docker Desktop instalado y ejecutándose
- Sistema operativo Windows con acceso a terminal (CMD o PowerShell)
- Proyecto organizado con la siguiente estructura:
# Proyecto: Taller IA Fase 3 - PREDICT_BANK

taller_IA_fase3/
├── datos/                          # Carpeta externa (inicialmente vacía, se llena al entrenar/predict)
│
└── predict_bank/                   # Proyecto principal
    ├── app/                        # Código fuente principal
    │   ├── apirest.py              # API REST con endpoints (train, predict_file, predict_one)
    │   ├── main.py                 # Script principal (si aplica, arranque o pruebas)
    │   ├── predict.py              # Lógica de predicción
    │   └── train.py                # Lógica de entrenamiento
    │
    ├── .dockerignore               # Archivos a ignorar por Docker
    ├── docker/                     # Configuración extra de Docker (si aplica)
    ├── Dockerfile                  # Imagen de Docker para la app
    ├── doker                       # (posible archivo auxiliar, revisar si es necesario)
    ├── kaggle.json                 # Credenciales para descargar datasets de Kaggle
    ├── prueba.txt                  # Archivo de prueba (auxiliar)
    ├── README.md                   # Documentación del proyecto
    └── requirements.txt            # Dependencias de Python


# Notas importantes
La carpeta datos externa al docker esta pensada para:
1. kaggle.json debe ser actualizado por el profesor para tener un token que permita la descarga,
   sin la clave de acceso el programa no funcionará.
2. En la etapa de entrenamiento el programa busca los datasets en Kaggle y los lleva a la carpeta de datos
   temporal dentro del docker, pero ademas los deja disponibles en la carpeta datos externa.
3. Despues de ser entrenado el modelo(modelo_entrenado.pkl) se deja disponible en la carpeta externa datos.
4. Despues de ser probado el modelo con test.csv, el resultado de las predicciones se dejan
   en el directorio externo datoscomo(predicciones.txt y predicciones.csv).
5. De ser necesario puedo suministrar mi clave, kaggle.json 
      
---
## Ejecución del proyecto
## Construcción de la imagen Docker

1. Inicie la aplicación docker desktop
1. Arranque la aplicacion Doker Desktop
2. Ubíquese en la raíz del proyecto predict_bank

```bash

---

## Construcción de la imagen Docker

```bash
# Ubíquese en la raíz del proyecto a la altura de Dokerfile. Por ejemplo (Mi caso):
cd C:\Users\OMAR TORRES\Desktop\taller_IA_fase2\predict_bank

## Construir la imagen Docker
docker build -t predict_bank .

```
## Ejecución del contenedor Docker

Para correr la API REST dentro de un contenedor Docker y montar la carpeta de datos externa, se utiliza el siguiente comando:

```bash
docker run -p 5001:5000 -v "C:/Users/OMAR TORRES/Desktop/taller_IA_fase3/datos:/app/datos" predict_bank
```
En mi caso esta es mi ruta "C:/Users/OMAR TORRES/Desktop/taller_IA_fase3/datos.
datos es una carpeta externa al lado de la carpeta del proyecto docker, pensada para descargar 
elmodelo entrenado y predicciones durante la prueba.

En este proyecto quedan disponibles los siguientes endpoints:
1. train : Al ejecutarse se entrena el modelo, descarga modelo entrenado y *.csv.
2. predict_file : Al ejecutarse se prueba el modelo con test.csv y descarga predicciones.txt 
   y predicciones.csv.
3. predict_one : al ejecutarse en el cuerpo de la petición se envía un json con datos de entrada y obtener
   La respuesta a la predicción.

Durante las pruebas uso la herramienta de postman.

**postman**
http://localhost:5001/train
http://localhost:5001/predict_file
http://localhost:5001/predict_one

## En caso de consulta contactar a:
Omar Alberto Torres
tel: 3043440112
Correo: omar.torresm@udea.edu.co

**Nota:** En caso de requerir orientación adicional sobre la ejecución o los detalles técnicos del proyecto, puede contactarme al correo institucional o revisar los comentarios en el código fuente.





