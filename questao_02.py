'''2) Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.'''

tamanho = int(input('Informe o tamanho das listas: '))

lista1 = []
lista2 = []

cont = 1
while cont <= tamanho:
  lista1.append(input(f'\nInforme o {cont}º elemento da lista 1: '))
  cont += 1

cont = 1
while cont <= tamanho:
  lista1.append(input(f'\nInforme o {cont}º elemento da lista 2: '))
  cont += 1

print(f'\nUnião das listas: {lista1 + lista2}') 
