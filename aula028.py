
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
 

print('Olá!')
print(f'Seu nome é: {nome}')
print(f'Seu nome invertido é: {nome[::-1]}')

if ' ' in nome:
    print('Seu nome tem espaços.')
else:
    print('Seu nome não tem espasos.')

print(('Seu nome tem ', len(nome), ' letras'))
print('A primeira letra do seu nome é: ', nome[:1])
print('A última letra do seu nome é: ', nome[-1])