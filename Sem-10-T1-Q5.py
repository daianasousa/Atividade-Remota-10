def dados_alunos():
    a = dict()

    while True:
        matricula = input('Matricula: ').strip()
        
        if matricula == '':
            break

        nome = input('Digite seu nome: ').strip()
        nota_1 = float(input('Primeira nota: '))
        nota_2 = float(input('Segunda nota: '))

        media = (nota_1 + nota_2) / 2

        a[matricula] = nome, nota_1, nota_2, media

    return a


def matriculas():
    m = []
    while True:
        matricula_entrada = input('Digite sua matricula: ').strip()
        if matricula_entrada == '':
            break

        m.append(matricula_entrada)
    
    return m


def main():
    a = dados_alunos()

    m = matriculas()

    i = 0
    while i < len(m):
        for k, v in a.items():
            if k == m[i]:
                print('{}: {:.1f}'.format(v[0], v[3]))

        i += 1


if __name__ == "__main__":
    main()