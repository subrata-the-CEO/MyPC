#Palindrome using While Loop
INPUT = int(input("Please Enter the Number: "))
REVERS = 0
Working_Digit = INPUT
while Working_Digit>0:
    LAST_DIGIT = Working_Digit%10
    REVERS = REVERS*10 + LAST_DIGIT
    Working_Digit //= 10
    print(REVERS)
if REVERS== INPUT:
    print ("Palindrom")
else:
    print ("Not")
    