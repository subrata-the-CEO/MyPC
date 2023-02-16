#Palindrome
Name = "Subrata"
Age = 25
DOB = "14th May 1997"
Location = "Kolkata"
Company = "Intellipaat"
Designation = "BDA"
Revers = ""
for i in str(Name):
    #print(i)
    Revers = i + Revers
print(Revers)
if Revers==Name:
    print("Palindrome")
else:
    print("It Is Not Plindrome")
    