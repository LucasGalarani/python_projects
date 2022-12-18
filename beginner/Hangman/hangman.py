import random

palavras = ['brasil', 'jogo', 'kate perry', 'Jeniffer', 'Elefante', 'Pudim', 'Brigadeiro', 'Beans', 'Coconut', 'Rice', 'Jelly', 'Microsoft', 'Adobe', 'Javascript', 'Pararelepipedo', 'Nozes', 'Cake', 'Sugar', 'Python', 'Lucas', 'Anthony']

palavra = random.choice(palavras)

tentativas = 0

chances = 4

letras_escolhidas = []

estado_atual = ['_'] * len(palavra)

print('Bem Vindo ao Jogo da Forca!')
print('Seu objetivo é acertar a palavra secreta')
print('Regras: ')
print('1- Você terá', chances,'tentativas para descobrir a palavra;')
print('2- Você só pode digitar uma palavra por vez;')
print('Ao acertar a letra ela irá ser colocada na palavra oculta')

while tentativas <= chances:
    letra = input('Qual letra você gostaria de colocar na palavra? ')
    if letra in palavra:
        print('Parabéns,você acertou!')
    else:
        print('Você errou,tente outra vez.')
        tentativas += 1