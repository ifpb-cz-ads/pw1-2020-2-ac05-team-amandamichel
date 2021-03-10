

'''4) Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta. Exemplo:

(()) OK
()()(()()) OK
()) Erro
'''

expressao = input('Informe a expressão com parênteses: ')

pilha = []

for ch in expressao:
  pilha.append(ch)

qtEsquerdo = 0
qtDireito = 0

while len(pilha) > 0 :
  pop = pilha.pop()
  
  if pop == '(':
    qtEsquerdo += 1
  
  elif pop == ')':
    qtDireito += 1

if (qtEsquerdo != qtDireito):
  print('Erro')
else:
  print('Ok')