def main():
    dado = dict()
    lancado = cont1 = cont2 = cont3 = cont4 = cont5 = cont6 = 0
    
    while True:
        face = int(input('face: '))
        if face == 0:
            break

        else:
            jogada = face
            dado[face] = jogada
            lancado += 1
            
            if jogada == 1:
                cont1 += 1
            elif jogada == 2:
                cont2 += 1
            elif jogada == 3:
                cont3 += 1
            elif jogada == 4:
                cont4 += 1
            elif jogada == 5:
                cont5 += 1
            elif jogada == 6:
                cont6 += 1

    print(f'O dado foi lançado {lancado} vezes.')
    print(f'A face 1 saiu {cont1} vezes.\nA face 2 saiu {cont2} vezes.\nA face 3 saiu {cont3} vezes.\nA face 4 saiu {cont4} vezes.\nA face 5 saiu {cont5} vezes.\nA face 6 saiu {cont6} vezes.')


if __name__ == "__main__":
    main()