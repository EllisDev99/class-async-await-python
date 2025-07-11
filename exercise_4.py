"""
Objetivo: Comparar concurrencia real.

🧠 Descripción:

    Función proceso_lento(i: int) que espera 2 segundos y retorna i**2.

    Primero: hacelo en un for con await proceso_lento(...) uno por uno.

    Segundo: hacelo con create_task() y gather() en paralelo.

    Medí el tiempo total de cada uno (usá time.perf_counter()).

    Imprimí cuánto tiempo te ahorraste al usar concurrencia.
"""
import asyncio, time

async def proceso_lento(i: int) -> int:
    await asyncio.sleep(2)
    return i**2

async def main():
    # PRIMER MARCADOR -SERIAL-
    serial_start = time.perf_counter()
    for n in range(1, 6):
        await proceso_lento(n)
    serial_end = time.perf_counter()
    serial_time = serial_end - serial_start
    print(f'Primer marcador: {serial_time:.3f}seg')

    # SEGUNDO MARCADOR -CONCURRENTE-
    concurrent_start = time.perf_counter()
    procesos = [asyncio.create_task(proceso_lento(n)) for n in range(1, 6)]
    result = await asyncio.gather(*procesos)
    concurrent_end = time.perf_counter()
    concurrent_time = concurrent_end - concurrent_start
    print(f'Segundo marcador: {concurrent_time:.3f}seg')
    #FINAL

    # DIFERENCIA DE MARCADORES
    print(f'Al usar la corrutina me ahorre:')
    print(f'{serial_time - concurrent_time:.3f}seg')

asyncio.run(main())