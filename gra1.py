import requests

# Token de Graphhopper
TOKEN = "a5e6c345-c03a-4a7b-9fad-c08fc5692867"
API_URL = "https://graphhopper.com/api/1/route"


def obtener_ruta(origen, destino):
    params = {
        "point": [origen, destino],
        "locale": "es",  # idioma español
        "vehicle": "car",
        "key": TOKEN,
        "instructions": True
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la ruta: {e}")
        return None

    return response.json()


def mostrar_ruta(ruta):
    print("\n--- Resumen de la ruta ---")
    distancia_km = ruta['paths'][0]['distance'] / 1000
    tiempo_min = ruta['paths'][0]['time'] / 60000
    print(f"Distancia total: {distancia_km:.2f} km")
    print(f"Tiempo estimado: {tiempo_min:.2f} minutos")

    print("\n--- Instrucciones paso a paso ---")
    for idx, instr in enumerate(ruta['paths'][0]['instructions'], start=1):
        texto = instr['text']
        distancia = instr['distance'] / 1000
        tiempo = instr['time'] / 60000
        print(f"{idx}. {texto} - {distancia:.2f} km, {tiempo:.2f} min")


def main():
    print("=== Programa de Geolocalización con Graphhopper ===")
    while True:
        origen = input("Ingrese la ubicación de origen (ej.: '-33.4489,-70.6693') o 's' para salir: ").strip()
        if origen.lower() in ['s', 'salir']:
            print("Saliendo del programa...")
            break

        destino = input("Ingrese la ubicación de destino (ej.: '-33.4561,-70.6483') o 's' para salir: ").strip()
        if destino.lower() in ['s', 'salir']:
            print("Saliendo del programa...")
            break

        ruta = obtener_ruta(origen, destino)
        if ruta:
            mostrar_ruta(ruta)
        else:
            print("No se pudo obtener la ruta. Intente nuevamente.")


if __name__ == "__main__":
    main()
