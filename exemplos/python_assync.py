import datetime
import math
import asyncio


async def main():
    print("Realizando o processamento matemático de forma assíncrona.")
    inicio = datetime.datetime.now()
    # asyncio.run(computar(inicio=1, fim=50_000_000))

    tarefa1 = asyncio.create_task(computar(inicio=1, fim=10_000_000))
    tarefa2 = asyncio.create_task(computar(inicio=1, fim=20_000_000))
    tarefa3 = asyncio.create_task(computar(inicio=1, fim=30_000_000))
    tarefa4 = asyncio.create_task(computar(inicio=1, fim=40_000_000))
    tarefa5 = asyncio.create_task(computar(inicio=1, fim=50_000_000))
    await asyncio.gather(tarefa1, tarefa2, tarefa3, tarefa4, tarefa5)

    fim = datetime.datetime.now()
    tempo = fim - inicio

    print(f"Terminou em  {tempo.total_seconds():.2f} segundos.")


async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":
    asyncio.run(main())
