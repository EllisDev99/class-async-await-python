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

archivo_1 = "Can't Stop.mp4"
archivo_2 = "Aerials.mp4"
archivo_2 = "The Drug In Me Is You.mp4"