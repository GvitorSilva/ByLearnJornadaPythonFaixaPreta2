from random import sample
low = 'abcdefghijklmnopqrstuvwxyz'
upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = '0123456789'
sym = '!@#$^&*'

todos = low + upp + num + sym
comprimento = 10
senha = ''. join (sample(todos, comprimento))
imprimir = (senha)

print(f'Sua senha é {imprimir}')
