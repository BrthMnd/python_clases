import random as rd

lista = []
def ingresarDatos():
    for i in range(20):
        lista.append(int(input("Coloque el numero: ")))
     
def datosAutomaricos():
    for i in range(20):
        lista.append(rd.randint(15,100))
    
def variosElemento():
    cantidad = int(input("ingrese cantidad de numeros a cambiar: "))
    encotrado = False
    count = 0
    
    while  cantidad >= count:
        elemento = int(input("ingrese elemento: "))
        numerodecambio = int(input("numero de cambio:"))
        x = 0
        for i in lista:
            if i == elemento:
                lista[x] = numerodecambio 
            x+= 1
        print(lista)  
            
        count+=1;
        if (encotrado):
            print("elemento no encontrado")

def unElemento():
    elemento = int (input("Coloque el que va a remplazar"))
    nuevonumero = int(input("nuevo numero"))
    count = 0
    for i in lista:
        if i == elemento:
            lista[count] = nuevonumero 
        count += 1
    print(lista)      
           
    
# while True:
    # 1
    
desicion = int(input("Opcion 1: Ingresar datos / Opcion 2: datos automaticos ->"))

if desicion == 1:
    ingresarDatos()
elif desicion == 2:
    datosAutomaricos()
else: 
    pass


# 2
print(lista)
cantidad = len(lista)
elemento = int(input("colocar elemento a buscar en la lista: "))
count = 1
encotrado = False
for i in lista:
    if i == elemento:
        print (f"Elemento {i} encontrado en la posicion de la lista: {count}")
        encotrado = False
        break
    count+=1;
    encotrado = True
    
if (encotrado):
    print("elemento no encontrado")

print(lista)
# 3

desicion = int(input("Opcion 1: un elemento / Opcion 2: varios elementos ->"))

if desicion == 1:
    unElemento()
elif desicion == 2:
    variosElemento()
else: 
    pass

# 4
count = 1
suma = 0
for i in lista:
    suma += i 
    
    
    count += 1
print (f"el promedio es: {suma/count}")

mayorq = 0
menorq = 50
for i in lista:
    if i > menorq:
        pass
    if i < menorq: 
        menorq = i
    if i == menorq: 
        pass
print(f"el menor es: {menorq}" )
    
                    