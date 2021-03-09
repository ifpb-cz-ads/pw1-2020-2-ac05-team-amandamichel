'''

Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

'''

lista1 = [5,1,4,7,8]
lista2 = [4,5,9,3,6]
lista3 = []


lista3.extend([i for i in lista1 if i not in lista2])
lista3.extend([j for j in lista2 if j not in lista1])

print(lista3)