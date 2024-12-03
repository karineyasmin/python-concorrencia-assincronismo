import asyncio
import aiofiles


async def exemplo_arq1():
    async with aiofiles.open("texto.txt") as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)


async def exemplo_arq2():
    async with aiofiles.open("texto.txt") as arquivo:
        async for linha in arquivo:
            print(linha)


def main():
    asyncio.run(exemplo_arq2())


if __name__ == "__main__":
    main()
