"""
Objetivo: Ver cómo se intercalan las corrutinas.

🧠 Descripción:

    Escribí tres funciones: tic(), tac(), y tuc(), cada una con asyncio.sleep() distintos.

    Que cada una imprima su nombre cada cierto tiempo, en un loop de 5 iteraciones.

    Lanzalas con create_task() y usá un await asyncio.sleep() más largo para que el programa no termine antes.

Ideal para ver cómo se intercalan las salidas de consola. Bien musical 😏
"""
import asyncio
from random import randint

async def tic():
    for i in range(1, 6):
        await asyncio.sleep(randint(0, 5))
        print('TIC')
    return 'TIC FINISHED'

async def tac():
    for i in range(1, 6):
        await asyncio.sleep(randint(0, 5))
        print('TAC')
    return 'TAC FINISHED'

async def toc():
    for i in range(1, 6):
        await asyncio.sleep(randint(0, 5))
        print('TOC')
    return 'TOC FINISHED'

async def main():
    task_tic = asyncio.create_task(tic())
    task_tac = asyncio.create_task(tac())
    task_toc = asyncio.create_task(toc())

    result = await asyncio.gather(task_tic, task_tac, task_toc)



asyncio.run(main())