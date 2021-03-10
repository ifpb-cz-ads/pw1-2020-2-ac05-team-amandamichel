'''

Modifique o programa anterior de forma a pesquisar p e v em toda a lista e informando o usuário a posição
onde p e a posição onde v foram encontrados.

'''

L=[15,7,27,39,39]
p=int(input("Digite o valor a procurar:"))
v=int(input("Digite o valor a procurar:"))
x=0
while x < len(L):
    if L[x] == p:
        print(p, " achado na posicao ", x)
    if L[x] == v:
        print(v, " achado na posicao ", x)
    x+=1

if p not in L:
    print("\n%d não encontrado" %p)

if v not in L:
    print("\n%d não encontrado" %v)
