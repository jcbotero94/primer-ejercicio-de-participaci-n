x=int(input("ingrese un numero: "))
factorial=x
if x>1:
  for i in range (x-1,1, -1):
    factorial= factorial* i
    print(i)
    print(factorial)