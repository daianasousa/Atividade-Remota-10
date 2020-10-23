def dados_iniciais():
    lista = []
    dicionario = {}

    i = 0
    for c in range(6):
        dicionario.clear()

        dicionario['nome'] = input('nome: ').strip()

        tempo_total = 0
        melhor_volta = 100000
        for i in range(10):
            tempo = float(input())
            
            tempo_total += tempo
            if tempo < melhor_volta:
                melhor_volta = tempo

        tempo_medio = tempo_total / 10

        dicionario['tempo_total'] = tempo_total
        dicionario['tempo_medio'] = tempo_medio
        dicionario['melhor_volta'] = melhor_volta

        lista.append(dicionario.copy())

    return lista


def organizar():
    lista = dados_iniciais()

    lista_ordenada = sorted(lista, key=lambda k:k['tempo_total'])

    return lista_ordenada


def main():
    lista_ordenada = organizar()

    print('-------|----------------------|---------------|---------------|---------------')
    print(' Ordem |   Nome do Corredor   |  Tempo Total  |  Tempo Médio  | Melhor Volta  ')
    print('-------|----------------------|---------------|---------------|---------------')

    z = 1
    i = 0
    for d in lista_ordenada:
        t = len(d['nome'])
        if t % 2 == 0:
            t = len(d['nome'])
        else:
            t = len(d['nome']) + 1

        print('   {}   |'.format(z), end='')

        print(' ' * (11 - (len(d['nome']) // 2)), end='')
        print('{}'.format(d['nome']), end='')
        print(' ' * (11 - (t // 2)), end='')

        print('|     {:.1f}     '.format(d['tempo_total']), end='')

        print('|     {:.1f}      '.format(d['tempo_medio']), end='')

        print('|     {:.1f}     '.format(d['melhor_volta']))

        i += 1
        z += 1

    print('-------|----------------------|---------------|---------------|---------------')


if __name__ == "__main__":
    main()