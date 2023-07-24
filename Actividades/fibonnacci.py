

num1 = 1
num2 = 1
num3 = 0
for i in range(20):
    num3 = num1 + num2
    if num2 == 1:
        print("1")
        print("1")
    
    print(num3)
    if num3 >= 2000:
        break
      
    num1 =num2
    num2 = num3