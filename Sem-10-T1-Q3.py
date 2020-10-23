cadastro1 = {}
cadastro2 = {}
def e_cad():
    for i in range(0, 2):
        nome = input('Nome: ').strip()
        idade = int(input('Idade: '))
        cpf = input('CPF: ').strip()
        if idade >= 18:
            dados = nome, idade, cpf
            cadastro1[cpf] = dados
        if idade < 18:
            dados2 = nome, idade, cpf
            cadastro2[cpf] = dados2

def desempacotar(cadastro1, cadastro2):
    if len(cadastro1) != 0 :
        print(f'========== MAIORES DE 18 ANOS ==========')
    for i in cadastro1:
        nome, idade, cpf = cadastro1[i]
        print(f'{nome};{idade};{cpf}')
    if len(cadastro2) != 0:
        print(f'========== MENORES DE 18 ANOS ==========')
    for c in cadastro2:
        nome, idade, cpf = cadastro2[c]
        print(f'{nome};{idade};{cpf}')


def main():
    e_cad()
    desempacotar(cadastro1, cadastro2)

if __name__ == '__main__':
    main()
