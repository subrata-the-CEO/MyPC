#countdown program using while loop
n = int(input("Enter the number: "))
while n>0:
    print("Countdown = ",n)
    n-=1
    print("Countdown = ",n)
    if n==0:
        print("BLASTOFF")
#countdown program using for loop
for i in range(n,0,-1):
    print(i)


