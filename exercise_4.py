"""
Objetivo: Comparar concurrencia real.

🧠 Descripción:

    Función proceso_lento(i: int) que espera 2 segundos y retorna i**2.

    Primero: hacelo en un for con await proceso_lento(...) uno por uno.

    Segundo: hacelo con create_task() y gather() en paralelo.

    Medí el tiempo total de cada uno (usá time.perf_counter()).

    Imprimí cuánto tiempo te ahorraste al usar concurrencia.
"""