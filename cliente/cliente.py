import requests

# Dirección de tu API REST (puede cambiar si corres en otro host/puerto)
API_URL = "http://localhost:5001"

def entrenar_modelo():
    url = f"{API_URL}/train"
    response = requests.post(url)
    if response.status_code == 200:
        print(" Entrenamiento completado")
        print(response.json())
    else:
        print(" Error en el entrenamiento:", response.text)

def predecir_archivo():
    url = f"{API_URL}/predict_file"
    response = requests.get(url)
    if response.status_code == 200:
        print(" Predicción por archivo lista")
        print(response.json())
    else:
        print(" Error en predicción:", response.text)

def predecir_uno(json_registro):
    url = f"{API_URL}/predict_one"
    response = requests.post(url, json=json_registro)
    if response.status_code == 200:
        print(" Predicción de un registro:")
        print(response.json())
    else:
        print(" Error en predicción:", response.text)


if __name__ == "__main__":
    # 1. Entrenar el modelo
    entrenar_modelo()

    # 2. Predecir por archivo
    predecir_archivo()

    # 3. Predecir un registro manual
    registro = {
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
    predecir_uno(registro)
