import asyncio# permite ejecutar funciones que pueden "esperar" sin bloquear el resto del programa.

async def say_hello():# definimos la función asíncrona.
    """Función asíncrona que imprime 'Hola...\n' seguido de una pausa (await) de 1s para despueé imprimir 'Ellis'."""
    print('Hola...\n')
    await asyncio.sleep(1)# pausa de 1 segundo, pero puede continuar con otra tarea si la hay
    print('Ellis')

# ----- CREACIÓN DE TAREAS ASÍNCRONAS
async def task1():
    """Función asíncrona que espera 2s con 'await asyncio.sleep(2)' luego imprime un mensaje."""
    await asyncio.sleep(2)
    print('Tarea 1 terminada.')

async def task2():
    """Función asíncrona que espera 1s con 'await asyncio.sleep(1)' luego imprime un mensaje."""
    await asyncio.sleep(1)
    print('Tarea 2 terminada.')

async def compute_square(x: int = 0, t: int = 1):
    """
    Calcula el cuadrado de un número de forma asíncrona tras una espera no bloqueante.

    Esta función espera `t` segundos utilizando `await asyncio.sleep(t)` y luego retorna `x` elevado al cuadrado.

    Args:
        x (int): Número a elevar al cuadrado. Por defecto es 0.
        t (int): Tiempo de espera en segundos antes de calcular. Por defecto es 1.

    Returns:
        int: El resultado de x ** 2.
    """
    await asyncio.sleep(t)
    return x**2

async def download_data(url: str) -> str:
    print(f'Start downloading from {url}')
    await asyncio.sleep(2) # simulamos el tiempo de espera
    print(f'Finished downloading from {url}')
    return f'Data from {url}'


async def main():
    """Función que crea dos tareas asíncronas que se ejecutan al mismo tiempo (concurrencia)"""
    taskA = asyncio.create_task(task1())
    taskB = asyncio.create_task(task2())

    await taskA
    await taskB

    # ----- EJECUTAR TAREAS CONCURRENTES
    results = await asyncio.gather( # lanza todas las tareas al mismo tiempo
        compute_square(3),
        compute_square(2, t=2),
        compute_square(8, t=3),
        compute_square(1, t=4),
        compute_square(4, t=5)
        )
    print(results)
    
    # ------ EJEMPLO DE DESCARGA DE DATOS
    urls = [
        'http://example.com/1',
        'http://example.com/2',
        'http://example.com/3',
        'http://example.com/4'
        ]
    task = [asyncio.create_task(download_data(url)) for url in urls]
    results2 = await asyncio.gather(*task)
    print('All downloads finished')
    for result in results2:
        print(result)    
    
    
    



# MAIN
if __name__ == '__main__': # esta línea se asegura de que lo que está abajo sólo se ejecute si corrés este archivo directamente, y no si lo importás como módulo.
    """Esto imprime '¡Hola mundo!' inmediatamente al arrancar el programa"""
    print('¡Hola mundo!')
    asyncio.run(say_hello()) # acá se corre la función say_hello() dentro de un bucle de eventos de asyncio. 

    asyncio.run(main())