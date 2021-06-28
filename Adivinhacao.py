import random


def jogar():
    print('\n################################')
    print('Bem vindo ao jogo de advinhação!')
    print('################################')

    numero_secreto = random.randint(1, 101)
    total = 0
    pontos = 1000

    print('Escolha um nível de dificuldade!')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))
    if nivel == 1:
        total = 20
    elif nivel == 2:
        total = 10
    elif nivel == 3:
        total = 5
    else:
        print('Escolha um nível!')

    for rodada in range(1, total + 1):
        print(f'tentatida {rodada} de {total}')
        chute = int(input('Digite o seu numero entre 1 e 100: '))
        print('Você digitou ', chute)

        if chute < 1 or chute > 100:
            print('Você deve digitar um numero entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'Você ACERTOU!\nVocê fez {pontos} pontos!')
            break
        else:
            if maior:
                print('Você errou!\nSeu chute foi maior que o número.')
            elif menor:
                print('Você errou!\nSeu chute foi menor que o número.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Fim de jogo')


if __name__ == "__main__":
    jogar()
