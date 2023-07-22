#Sum of the Number and Multiply of the Number
Number = int(input("Enter The Number: ")) #ABC
Sum = 0 #A+B+C
Multiply = 1 #A*B*C
while Number>0:
    Last_Digit = (Number%10)
    Multiply = Multiply * Last_Digit #--->
    Number = Number//10
    print(Multiply)
