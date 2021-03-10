'''

Escreva um programa que lê uma string com uma palavra ou frase, e que gera um dicionário onde cada chave
seja um caractere, e seu valor seja a quantidade de vezes que o caractere aparece na frase. Você deve
ignorar os espaços em branco.

Exemplo: "programacao" -> {"p": 1, "r": 2, "o": 2, "g": 1, "a": 2, "m": 1, "c": 1}

'''

palavra = input("Informe uma palavra ou uma frase: ")

dicionario = {}
i = 0
pos = 0

while i < len(palavra):
    if palavra[i] != " ":
        dicionario[pos] = palavra[i]
        pos = pos + 1
    i = i + 1

print(dicionario)
