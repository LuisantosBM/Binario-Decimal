n = 1010.101
num = 0

def entero(lista):
  num = 0

  for i in range(len(lista)):
    num = num + (int(lista[len(lista)-i-1])*2**i)
  
  return num

def fraccion(lista):
  num = 0

  for i in range(len(lista)):
    if i>1:
      num = num + (int(lista[i])*2**(-(i-1)))

  return num

lista = [i for i in str(n)]
ListaEntero = []
ListaFraccion = []

bandera = False

for i in range(len(lista)):
  if '.'==lista[i]:
    bandera= True
    ListaFraccion.append('0')  
    
  if bandera == False:
    ListaEntero.append(lista[i])
  else:
    ListaFraccion.append(lista[i])


print(entero(ListaEntero)+fraccion(ListaFraccion))
