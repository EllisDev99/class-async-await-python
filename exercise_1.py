# --- SIMULADOR DE PEDIDIOS DE COMIDA
"""
✅ 1. Simulador de pedidos de comida

📋 Objetivo: Practicar create_task() + gather() con tiempos diferentes.

🧠 Descripción:
Simulá que hay varios pedidos de comida. Cada uno tarda un tiempo distinto en prepararse. Escribí una función preparar_pedido(nombre: str, tiempo: int) que:

    Imprima cuándo empieza y termina.

    Devuelva el nombre del pedido y cuánto tardó.

Corré 5 pedidos al mismo tiempo y mostrá cuál salió primero y cuál último.
"""
import asyncio

# Función principal que será ejecutada por asyncio.run()
async def main():
    # Corrutina interna que simula la preparación de un pedido
    # Una corrutina es una función que puede pausar su ejecución y reanudarla más tarde.
    async def prepare_order(order: str = 'VASO CON AGUA', time: int = 1) -> str:
        print('Orden tomada, en un momento estará lista.')

        # Simula el tiempo que tarda en preparar el pedido (espera no bloqueante)
        await asyncio.sleep(time)
        print (f'Orden lista...')

        # Devuelve un string con la información del pedido
        return f'Pedido: {order}, tiempo de espera: {time}s'

    # Lista de pedidos que queremos preparar, cada uno es una corrutina que aún NO ha comenzado.
    orders = [
        prepare_order('HAMBURGUESA', 4),
        prepare_order(),
        prepare_order('PIZZA', 5),
        prepare_order('PERRO CALIENTE', 3),
        prepare_order('HELADO', 2)
    ]

    # Creamos tareas con asyncio.create_task para que empiecen a ejecutarse en segundo plano.
    # Esto no las espera, solo las lanza de una.
    list_orders = [asyncio.create_task(order) for order in orders]

    # Esperamos a que todas las tareas se completen al mismo tiempo usando asyncio.gather.
    # Esto devuelve una lista con los resultados de cada corrutina.
    ready_orders = await asyncio.gather(*list_orders)

    # Mostramos los resultados una vez que todas las órdenes estén listas.
    print('¡Saliendo las ordenes!:')
    for order in ready_orders:
        print(order)


# Lanza el event loop y ejecuta la función main()
# Esto es obligatorio en scripts para ejecutar código asincrónico
asyncio.run(main())

