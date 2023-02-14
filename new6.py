#Armstrong
Number = int(input ("Enter the number: "))
Sum = 0
#for i in str(Number):
    #Sum = Sum * int(i)
#print (Sum)
#    ABC = (A*A*A)+(B*B*B)+(C*C*C)= ABC --Armstrong Number

for i in str(Number):
    Sum = Sum + (int(i)**len(str(Number)))
if Sum == Number:
    print(f"Armstrong {Number}")
else:
    print("Not Armstrong")