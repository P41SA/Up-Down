import requests

# Función para verificar si una URL está en línea o caída
def verificar_estado_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"{url} está en línea (estado {response.status_code})."
        else:
            return f"{url} está caída (estado {response.status_code})."
    except requests.ConnectionError:
        return f"{url} está caída (No se pudo conectar)."

# Leer las URL desde un archivo de texto
def leer_urls_desde_archivo(archivo):
    try:
        with open(archivo, "r") as file:
            urls = file.read().splitlines()
        return urls
    except FileNotFoundError:
        return None

# Archivo de entrada
archivo_urls = "urls.txt"

# Leer las URLs desde el archivo
urls = leer_urls_desde_archivo(archivo_urls)

if urls:
    for url in urls:
        estado = verificar_estado_url(url)
        print(estado)
else:
    print(f"No se pudo encontrar el archivo '{archivo_urls}' o está vacío.")
