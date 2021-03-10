'''8) A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4].
Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.'''

import statistics

T = [ -10, -8, 0, 1, 2, 5, -2, -4]

'''Alternativa usando for

total = 0
for temp in T:
  total += temp

print(total/len(T))'''

print(f'Maior temperatura: {max(T)}\nMenor temperatura: {min(T)}\nMédia: {statistics.mean(T)}')
