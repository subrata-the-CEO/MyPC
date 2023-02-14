#testing python operators
n = int(input("Enter the number, n:"))
r = int(input("Enter the number, r:"))
s = (n-r)
#power = int(input("Enter the power:"))
#result = (n**power)
#print("Power value is: ", result)

factorial = 1 # = number*(number-1)*((number-1)-1)*...*1
factorial_r = 1
factorial_s = 1

while n>0  and r>0:
    factorial = factorial*n
    n-=1
    factorial_r = factorial_r*r
    r-=1
print("The Factoria of the Number (n) is: ", factorial) 
print("The Factoria of the Number (r) is: ", factorial_r)

while s>0:
    factorial_s = factorial_s*s
    s-=1

I = input("Enter the Either P or C: ")
if I=="P":
    p = (factorial/factorial_s)
    print("The Permutation is: ", p)
elif I=="C":
    c = (factorial/(factorial_r*factorial_s))
    print("The Combination is: ", c)
else:
    print("FU")