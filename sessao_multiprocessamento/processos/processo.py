import multiprocessing


print(f"Iniciando o processo com nome: {multiprocessing.current_process().name}")


def faz_algo(valor):
    print(f"Fazendo algo com {valor}")


def main():
    pc = multiprocessing.Process(
        target=faz_algo, args=("Pássaro",), name="Processo Geek"
    )
    print(f"Iniciando o processo com o nome {pc.name}")
    pc.start()
    pc.join()


if __name__ == "__main__":
    main()
