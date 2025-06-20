import asyncio# permite ejecutar funciones que pueden "esperar" sin bloquear el resto del programa.

async def say_hello():# definimos la función asíncrona.
    """función asíncrona que imprime 'Hola...\n' seguido de una pausa (await) de 1s para despueé imprimir 'Ellis'."""
    print('Hola...\n')
    await asyncio.sleep(1)# pausa de 1 segundo, pero puede continuar con otra tarea si la hay
    print('Ellis')



# MAIN
if __name__ == '__main__': # esta línea se asegura de que lo que está abajo sólo se ejecute si corrés este archivo directamente, y no si lo importás como módulo.
    """Esto imprime '¡Hola mundo!' inmediatamente al arrancar el programa"""
    print('¡Hola mundo!')
    asyncio.run(say_hello()) # acá se corre la función say_hello() dentro de un bucle de eventos de asyncio. 