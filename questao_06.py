'''6) Modifique o programa anterior para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado. Na impressão, indique qual dos dois valores foi achado primeiro.'''

L=[15,7,27,39]

p = int(input("Digite o valor a procurar: "))
v = int(input("\nDigite outro valor a procurar: "))

x=0
while x < len(L):
    if L[x] == p:
        print(f"\n{p} achado primeiro na posicao {x}")
        break
    elif L[x] == v:
        print(f"\n{v} achado primeiro na posicao {x}")
        break
    x+=1

if x == len(L):
	print("%d não encontrado" %p)
