"""
📋 Objetivo: Manejo de errores en corrutinas.

🧠 Descripción:
Creá una función descargar_archivo(nombre: str) que:

    Espera un tiempo aleatorio (usá random.randint).

    En un 25% de los casos, lance una excepción simulando un error de red.

    Usá gather() con return_exceptions=True para que ninguna tarea frene a las otras.

    Al final, imprimí cuáles descargas salieron bien y cuáles fallaron.
"""
import asyncio
from random import randint


# Definimos la corrutina para simular la descarga de un archivo
async def descargar_archivo(nombre: str) -> str:
    print(f'Iniciando la descarga de {nombre}')

    # Simulamos el tiempo de descarga
    await asyncio.sleep(randint(1, 5))

    # Generamos un número aleatorio que representa la falla del 25% (aprox)
    if randint(1, 4) == 1:
        raise Exception(f'Error de red {nombre}')
    
    print(f'{nombre} descargado correctamente.')
    return f'{nombre} OK'


# Corrutina principal
async def main():
    music = "Can't Stop.mp4"
    video = "The last of Us - cap 1.mkv"
    img = "Foto_de_perfil.png"

    # Ejecutamos todas las descargas en paralelo
    results = await asyncio.gather(
        descargar_archivo(music),
        descargar_archivo(video),
        descargar_archivo(img),
        return_exceptions=True # para que una excepción no frene a las demás
    )

    for result in results:
        if isinstance(result, Exception):
            print(f'Fallo al descargar {result}')
        else:
            print(f'Éxito al descargar {result}')


asyncio.run(main())