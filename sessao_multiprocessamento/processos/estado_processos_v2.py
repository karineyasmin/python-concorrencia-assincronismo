import multiprocessing
import time
import ctypes

# Compartilhando estados entre processos


def funcao1(val, stat):
    if stat.value:
        res = val.value + 10
        stat.value = False
    else:
        res = val.value + 20

        # aqui altera o valor da variavel
        val.value = 200
        stat.value = True

    print(f"Resultado da função 1 é {res}")
    time.sleep(0.001)


def funcao2(val, stat):
    if stat.value:
        res = val.value + 30
        stat.value = False
    else:
        res = val.value + 40

        val.value = 400
        stat.value = True

    print(f"O resultado da função 2 é {res}")
    time.sleep(0.001)


def main():
    valor = multiprocessing.Value("i", 100)  # "i" - Tipo Inteiro
    status = multiprocessing.Value(ctypes.c_bool, False)

    p1 = multiprocessing.Process(target=funcao1, args=(valor, status))
    p2 = multiprocessing.Process(target=funcao2, args=(valor, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
