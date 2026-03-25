def eh_digito(c):
    return "0" <= c <= "9"


def eh_maiuscula(c):
    return "A" <= c <= "Z"


def parseExpressao(linha):
    tokens = []
    i = 0

    # percorre a linha chamando estados
    while i < len(linha):
        i = estado_inicial(linha, i, tokens)

    return tokens


def estado_inicial(linha, i, tokens):
    # ignora espaços
    while i < len(linha) and linha[i].isspace():
        i += 1

    if i >= len(linha):
        return i

    c = linha[i]

    # parênteses
    if c == "(":
        tokens.append("(")
        return i + 1

    if c == ")":
        tokens.append(")")
        return i + 1

    # número
    if eh_digito(c):
        return estado_numero(linha, i, tokens)

    # identificador (RES, MEM, etc.)
    if eh_maiuscula(c):
        return estado_identificador(linha, i, tokens)

    # operadores simples
    if c == "+":
        tokens.append("+")
        return i + 1

    if c == "-":
        tokens.append("-")
        return i + 1

    if c == "*":
        tokens.append("*")
        return i + 1

    if c == "%":
        tokens.append("%")
        return i + 1

    if c == "^":
        tokens.append("^")
        return i + 1

    # / ou //
    if c == "/":
        return estado_barra(linha, i, tokens)

    raise ValueError(f"Erro léxico: '{c}'")


def estado_numero(linha, i, tokens):
    inicio = i
    tem_ponto = False

    # lê número com possível ponto
    while i < len(linha):
        c = linha[i]

        if eh_digito(c):
            i += 1
            continue

        if c == ".":
            if tem_ponto:
                raise ValueError("Erro léxico: número inválido")
            tem_ponto = True
            i += 1
            if i >= len(linha) or not eh_digito(linha[i]):
                raise ValueError("Erro léxico: número inválido")
            continue

        break

    tokens.append(linha[inicio:i])
    return i


def estado_identificador(linha, i, tokens):
    inicio = i

    # lê sequência de letras maiúsculas
    while i < len(linha) and eh_maiuscula(linha[i]):
        i += 1

    tokens.append(linha[inicio:i])
    return i


def estado_barra(linha, i, tokens):
    # distingue / de //
    if i + 1 < len(linha) and linha[i + 1] == "/":
        tokens.append("//")
        return i + 2

    tokens.append("/")
    return i + 1