import openpyxl 
import numpy as np

num = np.array([1,2,3,4,1,2,3,4,4,3,3,2,2,4,2,2,3,3])

print(num)
for i in num:
    print(i)

print(len(num))
print(np.median(num))
print(num[0:4:2])
print("la dimencion es",num.shape)
print("la cantidad de dimenciones es",num.ndim)
print("el tipo de dato es",num.dtype)
print("la cantidad de elementos de la matriz:", num.size)
print("la cantidad de elementos de la matriz:", num.data)
print("valor maximo", max(num))
print("valor minimo", min(num))
print("valor sumado", sum(num))
print("valor media", num.mean())
print("valor std", num.std())
print("valor std", num.dot())

