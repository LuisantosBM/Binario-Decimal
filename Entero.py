n = 1010
num = 0

lista = [int(i) for i in str(n)]

for i in range(len(lista)):
  num = num + (lista[len(lista)-i-1]*2**i)

print(num)
