# Estrutura

nome = input('Digite o seu nome: ')
print(f'\nOlá {nome},seja bem-vindo ao Conversor de Medidas.')
print('Aqui você poera converter diversar medidas,basta digitar uma medida e depois a que você quer transformar e pronto!')
print('Digite apenas a abreviação da medida.')

# Medidas
medida_1 = input('Digite a medida inicial: ')

if medida_1 == 'km':
    print('Medida selecionada é quilômetro')
    resposta = input('Tem certeza? ')
    if resposta == 'sim':
        print('Ok,slecione a proxima medida.')
    else:
        print('Tente novamente.')
        quit()
        
elif medida_1 == 'hm':
    print('Medida selecionada é hectômetro')
    resposta = input('Tem certeza? ')
    if resposta == 'sim':
        print('Ok,slecione a proxima medida.')
    else:
        print('Tente novamente')
        quit()
        
elif medida_1 == 'dam':
    print('Medida selecionada é decâmetro')
    resposta = input('Tem certeza? ')
    if resposta == 'sim':
        print('Ok,slecione a proxima medida.')
        quit()
        
    else:
        print()
elif medida_1 == 'm':
    print('Medida selecionada é metro')
    resposta = input('Tem certeza? ')
    if resposta == 'sim':
        print('Ok,slecione a proxima medida.')
        
elif medida_1 == 'dm':
    print('Medida selecionada é decímetro')
    resposta = input('Tem certeza? ')
    if resposta == 'sim':
        print('Ok,slecione a proxima medida.')
    
elif medida_1 == 'cm':
    print('Medida selecionada é centímetro')
    resposta = input('Tem certeza? ')
    if resposta == 'sim':
        print('Ok,slecione a proxima medida.')
        
elif medida_1 == 'mm':
    print('Medida selecionada é milímetro')
    resposta = input('Tem certeza? ')
    if resposta == 'sim':
        print('Ok,slecione a proxima medida.')
    
medida_2 = input('Digite a medida para fazer a transformação: ')
# Conversor

# Calculos