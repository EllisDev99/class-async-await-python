"""
📋 Objetivo: Practicar asyncio.wait_for().

🧠 Descripción:

    Función consultar_api(nombre: str, tiempo_respuesta: int) que espera tiempo_respuesta segundos.

    Usá asyncio.wait_for() con un timeout menor a veces.

    Si excede el tiempo, capturá la excepción y decí “La API de {nombre} se tardó demasiado”.
"""
import asyncio

async def consultar_api(nombre: str, tiempo_respuesta: int) -> str:
    print('Consultando la API. . .')
    await asyncio.sleep(tiempo_respuesta)
    return 'OK'

async def main():
    try:
        api = 'PokeAPI'
        # usamos wait_for() para indicar un tiempo de respuesta
        await asyncio.wait_for(consultar_api(api, 3), 4) # tiempo de espera 4s
    except asyncio.TimeoutError: # en caso de excederce se lanza una excepción
        print(f'La API de {api} se tardó demasiado.')

asyncio.run(main())