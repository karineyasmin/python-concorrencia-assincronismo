import datetime
import math
import cProfile
import pstats
import io
from pstats import SortKey


def main():
    inicio = datetime.datetime.now()
    computar(fim=50_000_000)
    tempo = datetime.datetime.now() - inicio

    print(f"Terminou em {tempo.total_seconds():.2f} segundos")


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()

    profiler.disable()
    profiler.dump_stats("python_padrao2.stats")

    sec = io.StringIO()
    sort_by = SortKey.TIME
    ps = pstats.Stats(profiler, stream=sec).sort_stats(sort_by)
    ps.print_stats()
    print(sec.getvalue())
