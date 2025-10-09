from predict import hacer_prediccion  #Importo la función
# ------------------------------------------------------------------------------
# 4. Simulación: entrada como vendría desde producción
# ------------------------------------------------------------------------------
entrada = {
    "age": 45,
    "job": "admin.",
    "marital": "married",
    "education": "secondary",
    "default": "no",
    "balance": 600,
    "housing": "yes",
    "loan": "no",
    "contact": "cellular",
    "campaign": 3,
    "pdays": -1,
    "previous": 0,
    "poutcome": "unknown"
}

def main():
    prediccion = hacer_prediccion(entrada)
    print("Predicción:", prediccion)
    
if __name__ == "__main__":
    main()  
