# Integrantes do grupo (ordem alfabética):
# André Vinícius Zicka Schmidt - GitHub: andrevzs
# Gabriel Fischer Domakoski - GitHub: fochu3013
#
# Grupo no Canvas:
# RA1 19

import sys
from lexer import parseExpressao


def lerArquivoTeste(nome_arquivo):
    linhas = []

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                conteudo = linha.strip()
                if conteudo != "":
                    linhas.append((numero_linha, conteudo))
    except FileNotFoundError:
        print(f"Erro: arquivo '{nome_arquivo}' não encontrado.")
        sys.exit(1)
    except OSError as erro:
        print(f"Erro ao abrir o arquivo '{nome_arquivo}': {erro}")
        sys.exit(1)

    return linhas


def processarLinhas(linhas):
    for numero_linha, conteudo in linhas:
        try:
            tokens = parseExpressao(conteudo)
            print(f"Linha {numero_linha}: {tokens}")
        except ValueError as erro:
            print(f"Linha {numero_linha}: {erro}")


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo_teste.txt>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    linhas = lerArquivoTeste(nome_arquivo)
    processarLinhas(linhas)


if __name__ == "__main__":
    main()