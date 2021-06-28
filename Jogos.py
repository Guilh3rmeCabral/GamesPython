import Forca
import Adivinhacao

def escolha_jogo():
    print('################################')
    print('=======Escolha o seu Jogo!=======')
    print('################################')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Digite o jogo que queira jogar:'))

    if jogo == 1:
        print('Jogo da Forca')
        Forca.jogar()
    elif jogo == 2:
        print('Jogo da Advinhação')
        Adivinhacao.jogar()
    else:
        print('Escolha um jogo')

if (__name__ == '__main__'):
    escolha_jogo()