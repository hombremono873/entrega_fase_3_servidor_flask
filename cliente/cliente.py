
#import requests
#import json
#import os
#import threading, itertools, time, sys
import threading, itertools, time, sys, json, requests, os

#API_URL = "http://localhost:5001"

API_URL = os.getenv("API_URL", "http://host.docker.internal:5001")

def entrenar_modelo():
    print("\nIniciando entrenamiento del modelo...")
    print("Por favor sea paciente, este proceso puede tardar algunos minutos.\n")

    stop_spinner = False

    def spinner():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if stop_spinner:
                break
            sys.stdout.write(f'\rEntrenando el modelo... {c}')
            sys.stdout.flush()
            time.sleep(0.15)
        sys.stdout.write('\rEntrenamiento completado.    \n')

    # iniciar el hilo del spinner
    t = threading.Thread(target=spinner)
    t.start()

    try:
        r = requests.post(f"{API_URL}/train")
    except requests.exceptions.RequestException:
        stop_spinner = True
        t.join()
        print("\nError al conectar con el servidor.")
        return

    stop_spinner = True
    t.join()

    # mostrar resultado final
    if r.status_code == 200:
        print("Entrenamiento completado con éxito.\n")
    else:
        print("Error durante el entrenamiento.\n")

    print("Resultados del entrenamiento:")
    print(r.json())


def predecir_archivo():
    print("\nEl proceso puede tardar unos segundos por favor espere ")
    r = requests.get(f"{API_URL}/predict_file")
    print("\nPredicción por archivo lista" if r.status_code == 200 else "Error")
    print(r.json())

def predecir_uno():
    try: 
        print("\nEl proceso puede tardar unos segundos por favor espere ")
        with open("data.json", "r") as f:
            data = json.load(f)
        r = requests.post(f"{API_URL}/predict_one", json=data)
        print("\nPredicción individual" if r.status_code == 200 else "Error")
        print(r.json())
    except FileNotFoundError:
        print("\nNo se encontró el archivo data.json en el contenedor.")
        
def predecir_dinamico():
    print("\n--- PREDICCIÓN INDIVIDUAL ---\n")
    print("1. Usar archivo data.json existente\n")
    print("2. Ingresar los datos manualmente\n")
    opcion = input("\n Seleccione una opción: ")

    # Selección de entrada
    if opcion == "1":
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print(" No se encontró el archivo data.json en el contenedor.")
            return
    elif opcion == "2":
        print("\nIngrese los datos solicitados:")
        data = {
            "age": int(input("Edad: ")),
            "job": input("Profesión (ej: admin.): "),
            "marital": input("Estado civil (married/single/divorced): "),
            "education": input("Nivel educativo (primary/secondary/tertiary): "),
            "default": input("¿Tiene deuda por defecto? (yes/no): "),
            "balance": int(input("Balance en cuenta: ")),
            "housing": input("¿Tiene crédito hipotecario? (yes/no): "),
            "loan": input("¿Tiene préstamo personal? (yes/no): "),
            "contact": input("Medio de contacto (cellular/telephone): "),
            "campaign": int(input("Número de contactos durante la campaña: ")),
            "pdays": int(input("Días desde la última campaña (999 si nunca fue contactado): ")),
            "previous": int(input("Número de contactos previos: ")),
            "poutcome": input("Resultado anterior (success/failure/unknown): ")
        }
    else:
        print("Opción no válida.")
        return

    # Spinner
    stop_spinner = False
    def spinner():
        for c in itertools.cycle('|/-\\'):
            if stop_spinner:
                break
            sys.stdout.write(f'\r Enviando datos para predicción... {c}')
            sys.stdout.flush()
            time.sleep(0.15)
        sys.stdout.write('\r Predicción completada.              \n')

    t = threading.Thread(target=spinner)
    t.start()
    r = requests.post(f"{API_URL}/predict_one", json=data)

    stop_spinner = True
    t.join()

    if r.status_code == 200:
        result = r.json()
        print(f"\n Resultado de la predicción:\nPredicción: {result['pred']} | Probabilidad: {result['proba']:.3f}")
    else:
        print(" Error al realizar la predicción.")
        print(r.json())

def menu():
    while True:
        print("\n--- CLIENTE ML ---")
        print("1. Entrenar modelo")
        print("2. Predecir archivo")
        print("3. Predecir registro individual")
        print("4. Predecir registro entrada dinámica")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            entrenar_modelo()
        elif opcion == "2":
            predecir_archivo()
        elif opcion == "3":
            predecir_uno()
        elif opcion == "4":
            predecir_dinamico()
        elif opcion == "5":
            print("Saliendo del cliente...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
    