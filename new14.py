#list
a = ['Subrata',2023,25.7,True]
string = []
integer = []
b = "Intellipaat"
#for i in a:
   # print(f"{i}:{type(i)}")
#a.reverse()
#a.append(b)
#a.extend(b)
#a.count(2023)
#print(a.count(2023))
#print(a.index(25.7))
#write a program to seperate every element and find the desired element
#for i in a:
 #   if i==25.7:
  #      print("Present")
   # else:
    #    print("Fuck_Off")
#for i in a:
 #   if type(i) == int:
  #      integer.append(i)
   # elif type(i) == str:
    #    string.append(i)
    #else:
      #  print('NULL')
#print(integer, string)
# int = 1; str = 2; float = 
#a.count(type(a))
#print(a.count)

#count each and every/ number of data types in the list

a = ["python","hello",69,69.69,True,False]
b = [i for i in a if type(i) == int]
c = [i for i in a if type(i) == str]
d = [i for i in a if type(i) == bool]
e = [i for i in a if type(i) == float]



count = 0
for i in a:
    if type(i) == int:
        count += 1

print("int",count)