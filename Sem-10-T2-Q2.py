def ano_nascimento(lista):
    d = dict()
    for c in lista:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d


def main():
    lista = []
    for c in range(1000):
        ano = int(input())
        lista.append(ano)

    lista.sort()

    h = ano_nascimento(lista)
    for k, v in h.items():
        print('{}: {}'.format(k, v))


if __name__ == "__main__":
    main()