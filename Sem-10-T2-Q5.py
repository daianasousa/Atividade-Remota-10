agenda = {
    'João': '86988102987',
}


# (C)RUD
def criar():
    # ler o nome
    nome = input('Nome: ')
    # ler o telefone e adiciona em uma lista telefonica
    telefone = [input("Número de telefone: ")]
    # empacota nome e telefone com uma variável
    lista = (nome, telefone)
    # adiciona o aluno ao dicioário
    codigo = nome
    agenda[codigo] = lista
    input('Registro Incluído. Pressione qualquer tecla para contunuar...')


# C(R)UD
def ler(codigo):
    # carrega os dados do dicionário e desempacota nas variáveis
    nome, telefone = agenda[codigo]
    # retorna as variáveis desempacotadas
    return nome, telefone


# CR(U)D
def atualizar(codigo):
    # carrega dados do aluno definido pelo código
    nome, telefone = ler(codigo)
    # ler um novo nome para variável auxiliar
    aux = input(f'Novo Nome: ')
    # se o valor lido para o nome for vazio, ignora e mantém o mesmo valor
    if aux != '':
        # se for lido um valor válido, adiciona o campo nome
        nome = aux

    # usa a mesma variável auxiliar para ler telefone
    aux = input(f'Novo Telefone: ')
    # se o valor lido para o telefone for vazio, ignora e mantém o mesmo valor
    if aux != '':
        # se for um telefone válido, adiciona um telefone o mais
        nova = input(f'Incluir Telefone? (S, N): ')[0].upper() == 'S'
        if nova:
            
            agenda[codigo][1].append(str(aux))
            print('telefone incluída com sucesso.')
        else: 
            print('Erro!!!!!!!!!!!!1')
    # atualiza os dados no dicionário agenda
    agenda[codigo] = (nome, telefone)
    input('Registro Atualizado. Pressione qualquer tecla para contunuar...')


# CRU(D)
def apagar(codigo):
    # ler o código para apagar.
    nome, telefone = ler(codigo)
    # pegue uma confirmação do usuário para excluir
    confirma = input(f'Deseja realmente apagar {nome}? (S, N): ')[0].upper() == 'S'
    if confirma:
        # se confirmado, apaga o registro
        del agenda[codigo]


        input('Registro Apagado. Pressione qualquer tecla para contunuar...')


def Agenda_telefonica():
    # imprime uma listagem da agenda
    print('=' * 10, 'Listando Toda agenda', '=' * 10)
    qtd = 0
    # código recebe todas as chaves do dicionário agenda
    for codigo in agenda:
        # ler os dados da agenda
        nome, telefone = ler(codigo)
        print('-' * 30)
        print(f'Nome: {codigo}')
        # imprime os dados
        print(f'Telefone: {telefone}')

        qtd += 1
    if qtd == 0:
        print('<<< Nada para mostrar >>>')
    else:
        print(f'{qtd} nomes exibidos no relatório.')
    print('=' * 10, 'Fim da Listagem da agenda', '=' * 10)
    input('Pressione qualquer tecla para continuar....')



def menu():
    # mostra um menu de opções e faz a leitura da opção desejada
    while True:
        print('1 - (C) Incluir Novo Nome')
        print('2 - (R) Incluir Telefone')
        print('3 - (U) Excluir Telefone')
        print('4 - (D) Excluir Nome')
        print('5 - Mostra Agenda')
        print('0 - Fim do Programa')
        print('=' * 30)
        opcao = int(input('Digite sua opção: '))
        if opcao in (1, 2, 3, 4, 5, 0):
            return opcao
        else:
            print('Opção Inválida')


def main():
    while True:
        op = menu()
        if op == 1 or op == 2:  # create
            criar()
        
        elif op == 3 or op == 4:  # delete
            codigo = int(input('nome para Remover: '))
            if codigo in agenda:
                apagar(codigo)
            else:
                print(f'nome não existe na agenda com código {codigo}.')
        elif op == 5:  # listar todos
            Agenda_telefonica()
        elif op == 0:  # fim do programa
            print('Fim do programa.')
            break
        else:
            pass


if __name__ == '__main__':
    main()
