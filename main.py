import asyncio# permite ejecutar funciones que pueden "esperar" sin bloquear el resto del programa.

async def say_hello():# definimos la función asíncrona.
    """Función asíncrona que imprime 'Hola...\n' seguido de una pausa (await) de 1s para despueé imprimir 'Ellis'."""
    print('Hola...\n')
    await asyncio.sleep(1)# pausa de 1 segundo, pero puede continuar con otra tarea si la hay
    print('Ellis')

async def task1():
    """Función asíncrona que espera 2s con 'await asyncio.sleep(2)' luego imprime un mensaje."""
    await asyncio.sleep(2)
    print('Tarea 1 terminada.')

async def task2():
    """Función asíncrona que espera 1s con 'await asyncio.sleep(1)' luego imprime un mensaje."""
    await asyncio.sleep(1)
    print('Tarea 2 terminada.')

async def main():
    """Función que crea dos tareas asíncronas que se ejecutan al mismo tiempo (concurrencia)"""
    taskA = asyncio.create_task(task1())
    taskB = asyncio.create_task(task2())

    await taskA
    await taskB







# MAIN
if __name__ == '__main__': # esta línea se asegura de que lo que está abajo sólo se ejecute si corrés este archivo directamente, y no si lo importás como módulo.
    """Esto imprime '¡Hola mundo!' inmediatamente al arrancar el programa"""
    print('¡Hola mundo!')
    asyncio.run(say_hello()) # acá se corre la función say_hello() dentro de un bucle de eventos de asyncio. 

    asyncio.run(main())