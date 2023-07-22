#Armstrong Number using While Loop
Number = int(input("Enter The Number: "))
Wokring_Digit = Number
Sum = 0
Length = len(str(Wokring_Digit))
#Armstrong = (A*A*A)+(B*B*B)+(C*C*C) = ABC 
while Wokring_Digit>0:
    Last_Digit = (Wokring_Digit%10)
    Sum = Sum + (Last_Digit**Length)
    Wokring_Digit = Wokring_Digit//10
    print(Sum)
if Sum==Number:
    print("This is an Armstrong Number")
else:
    print("This is Not an Armstrong Number")
