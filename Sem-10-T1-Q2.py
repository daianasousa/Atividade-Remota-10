def criando_agenda(n):
    agenda = []
    contato = {}

    a = 0
    while a < n:
        contato.clear()
        contato['nome'] = input('Nome: ').strip()
        contato['cidade'] = input('Cidade: ').strip()
        contato['estado'] = input('Estado: ').strip()
        contato['telefone'] = input('telefone: ').strip()

        agenda.append(contato.copy())
        
        a += 1

    return agenda


def main():
    n = int(input('Valor de n°: '))

    agenda = criando_agenda(n)

    for contato in agenda:
        print(contato['nome'], end='')

        print(' '*(25 - len(contato['nome'])), end='')
        
        print(contato['cidade'], end='')
        
        print('({})'.format(contato['estado']), end='')
        
        print(' ' * (24 - len(contato['cidade']) + len(contato['estado'])), end='')
        
        print(contato['telefone'])


if __name__ == "__main__":
    main()