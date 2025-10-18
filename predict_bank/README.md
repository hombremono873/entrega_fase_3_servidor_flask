# Predicción con Modelo de Machine Learning (Dockerizado)

> **Proyecto:** Predictor en Actividades Bancarias  
> **Autor:** Omar Torres — Estudiante de Ingeniería de Sistemas  
> **Entregado a:** Raúl Ramos Pollán, Jonathan Granda – Facultad de Ingeniería, Universidad de Antioquia  
> **Fecha de entrega:** 23 de noviembre de 2025

## Resumen
Este proyecto implementa un flujo completo de *Machine Learning* para predecir resultados en actividades bancarias.  
La solución está **contenedorizada con Docker** y expone una **API REST con Flask** para:
- Entrenar el modelo
- Probar el modelo con `test.csv`
- Obtener la predicción de un único registro enviado como JSON

El uso de Docker garantiza un entorno **limpio, reproducible y portable**.

## Endpoints (vista general)
- `POST /train`  
  Entrena el modelo desde cero (descarga los datos de Kaggle si no existen), calcula métricas y **serializa el modelo** en `datos/modelo_entrenado.pkl`.  
  **Salida:** `{ mensaje, metrics }`

- `GET /predict_file`  
  Carga el modelo entrenado y genera predicciones para `datos/test.csv`.  
  **Salida:** `{ mensaje, preview }` y archivos `datos/predicciones.txt` y `datos/predicciones.csv`.

- `POST /predict_one`  
  Recibe un **JSON** con un registro, aplica el mismo preprocesamiento y retorna la predicción y su probabilidad.  
  **Entrada (JSON):** campos del dataset (excepto los eliminados en preprocesamiento)  
  **Salida:** `{ pred, proba }`

---
## Acceso a los datos de Kaggle

El proyecto utiliza los datasets de la competencia **[Playground Series – Season 5, Episode 8](https://www.kaggle.com/competitions/playground-series-s5e8/overview)**.  
Para que el contenedor pueda descargar automáticamente los datos al momento de entrenar el modelo, es necesario configurar tus credenciales de Kaggle.

### Pasos para configurar el acceso
1. Únete a la competencia en los enlaces oficiales:
   - [Competencia (overview)](https://www.kaggle.com/competitions/playground-series-s5e8/overview)
   - [Datos (data)](https://www.kaggle.com/competitions/playground-series-s5e8/data)
2. En tu perfil de Kaggle, ve a:  
   **Account → Create New API Token**  
   Esto descargará un archivo llamado `kaggle.json`.
3. Coloca `kaggle.json` **en la raíz del proyecto**, al mismo nivel del `Dockerfile`.  
   Ejemplo:

```text
taller_IA_fase3/
├──  predict_bank/                   # Proyecto principal
    ├── app/                        # Código fuente principal
    │   ├── apirest.py              # API REST con endpoints (train, predict_file, predict_one)
    │   |     
    │   ├── predict.py              # Lógica de predicción
    │   └── train.py                # Lógica de entrenamiento
    │
    ├── .dockerignore               # Archivos a ignorar por Docker
    ├──datos/ se llena con archivos generados en el train, si no existe se crea
    ├── Dockerfile                  # Imagen de Docker para la app
    ├── doker                       # (posible archivo auxiliar, revisar si es necesario)
    ├── kaggle.json                 # > Sin este archivo, el modelo no podrá descargar ni entrenar los datos.
    ├── prueba.txt                  # Archivo de prueba (auxiliar)
    ├── README.md                   # Documentación del proyecto
    └── requirements.txt            # Dependencias de Python
```
---
# Notas importantes

La carpeta **`datos`** (externa al contenedor Docker) está diseñada para mantener todos los archivos generados durante la ejecución del proyecto. si no existe se crea en automático 

1. El archivo **`kaggle.json`** debe ser actualizado por el profesor con un token válido de Kaggle.  
   Sin esta clave de acceso, el programa **no podrá descargar los datasets**.

2. Durante la etapa de **entrenamiento**, el programa descarga los datasets desde Kaggle, los copia a la carpeta temporal dentro del contenedor y, además, los deja disponibles en la carpeta externa `datos`.

3. Una vez **entrenado el modelo**, el archivo `modelo_entrenado.pkl` se guarda automáticamente en la carpeta externa `datos`.

4. Al ejecutar la **predicción con `test.csv`**, los resultados (`predicciones.txt` y `predicciones.csv`) se generan dentro del contenedor y se guardan también en la carpeta externa `datos`.

5. En caso de ser necesario, puedo suministrar mi archivo `kaggle.json` con las credenciales configuradas para facilitar la ejecución.

      
---
## Ejecución del proyecto

### Construcción de la imagen Docker

1. Asegúrese de tener **Docker Desktop** instalado y en ejecución.  
2. Abra una terminal (**CMD** o **PowerShell**) en su sistema.  
3. Ubíquese en la **raíz del proyecto `predict_bank`**, es decir, en el mismo nivel donde se encuentra el archivo **`Dockerfile`**.

   **Ejemplo (en Windows):**
   ```bash
   cd C:\Users\OMAR TORRES\Desktop\taller_IA_fase3\predict_bank

```bash

---

## Construcción de la imagen Docker

```bash
## Construcción de la imagen Docker
# Ubíquese en la raíz del proyecto, a la altura del archivo Dockerfile. 
# Por ejemplo (en mi caso):
cd C:\Users\OMAR TORRES\Desktop\taller_IA_fase3\predict_bank

# Construir la imagen Docker
docker build -t predict_bank .

```
## Ejecución del contenedor Docker
## Ejecución del contenedor Docker

```bash
# Para correr la API REST dentro de un contenedor Docker 
# y montar la carpeta de datos externa al proyecto, utilice el siguiente comando:

# El siguiente comando ejecuta la imagen y coordina el dialogo entre puertos
docker run -p 5001:5000 predict_bank

# El siguiente comando ademas de coordinar puertos salva los datos generados en carpeta externa al
# docker datos
docker run -it --rm -v "%cd%\datos:/app/datos" -p 5001:5000 banco

Para correr la API REST dentro de un contenedor Docker y montar la carpeta de datos externa, se utiliza el siguiente comando:
```
El comando anterior ejecuta el contenedor a partir de la imagen predict_bank,
expone el puerto 5000 del contenedor en el puerto 5001 de tu máquina local,
y monta la carpeta datos como volumen compartido entre tu sistema y el contenedor,
permitiendo guardar los modelos y resultados fuera del entorno Docker.
---

## Eliminación y administración rápida de Docker

```bash
#  Detener contenedores en ejecución
docker stop $(docker ps -q)

#  Eliminar contenedores detenidos o en ejecución
docker rm -f $(docker ps -aq)

#  Eliminar imágenes específicas o todas
docker rmi <nombre_o_id_imagen>
for /f %i in ('docker images -q') do docker rmi -f %i

#  Limpieza automática con Docker Prune
docker system prune          # elimina contenedores, redes y caché no usados
docker system prune -a       # incluye imágenes no utilizadas
```

## Ruta de datos y endpoints

En mi caso, la ruta del volumen de datos es:
**"C:/Users/OMAR TORRES/Desktop/taller_IA_fase3/datos"**.  
La carpeta **datos** es externa al proyecto Docker y se usa para **guardar el modelo entrenado** y las **predicciones** durante las pruebas.

### Endpoints disponibles
1. **POST /train**  
   Entrena el modelo (descarga los datasets de Kaggle si no existen) y guarda `modelo_entrenado.pkl` en `datos/`.

2. **GET /predict_file**  
   Usa `datos/test.csv` y genera `predicciones.txt` y `predicciones.csv` en `datos/`.

3. **POST /predict_one**  
   Recibe un JSON con un registro y retorna `{ "pred": int, "proba": float }`.

**Pruebas con Postman**
- http://localhost:5001/train  
- http://localhost:5001/predict_file  
- http://localhost:5001/predict_one

> Ejemplo rápido (predict_one):
> ```json
```json
{
  "age": 42,
  "job": "admin.",
  "marital": "married",
  "education": "secondary",
  "default": "no",
  "balance": 500,
  "housing": "yes",
  "loan": "no",
  "contact": "cellular",
  "campaign": 1,
  "pdays": 999,
  "previous": 0,
  "poutcome": "unknown"
}
> ```
## Uso del cliente Python (`cliente.py`)

Además de Postman, el proyecto incluye un cliente en Python llamado **`cliente.py`**,  
que permite interactuar fácilmente con la API REST directamente desde la línea de comandos.  
el cliente está diseñado para consumir los mismos endpoints que el servidor Flask.

### Ejecución

Asegúrese de que el contenedor Docker esté corriendo (la API activa en el puerto **5001**)  

## Contacto
Omar Alberto Torres  
Tel: 304 344 0112  
Correo: omar.torresm@udea.edu.co

**Nota:** Si requiere orientación adicional sobre la ejecución o detalles técnicos, puede escribir al correo institucional o revisar los comentarios en el código fuente.






