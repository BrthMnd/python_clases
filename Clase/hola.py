# import numpy as np
import random as rd
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# list = [1,2,3,4,5,6,7,8,9,10]
list = []
for i in range(20):
    num = rd.randint(0,99)
    list.append(num)
list.sort()
listanueva = [str(i)for i in list]
cadena = "-".join(listanueva)


# print(listanueva)
print(cadena)