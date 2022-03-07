n = 0.101
num = 0

lista = [i for i in str(n)]

for i in range(len(lista)):
  if i>1:
    num = num + (int(lista[i])*2**(-(i-1)))

#Segunda forma.
#for i in range(len(lista)):
#  if '.'==lista[len(lista)-i-1]:
#    break
#  else:
#    num = num + (int(lista[len(lista)-i-1])*2**(-(len(lista)-2-i)))

print(num)
