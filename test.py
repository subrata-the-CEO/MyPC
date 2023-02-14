#find the sum and multiplication of a number
number = int(input("Enter the Number: "))
sum = 0
multi = 1

#for i in str(number):
#    sum =sum +int(i)
#    multi=multi*int(i)
#print(sum)
#print(multi)
#while number!=0:
#    working_digit = number%10
#    sum = sum+working_digit
#    number=number//10
#print(sum)

#prime number
for i in range(2,number):
    if number%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
    