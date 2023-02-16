#def sum_of_data():
#    print ("Mother Fucker")
#sum_of_data()

#def sum_of_data(a):
#    print(a)
#sum_of_data("CEO")

#def sum_of_data(a : int,b : str):
#    print(a)
#    print(b)
#sum_of_data(49,"Roll Number")

#def sum_of_digits(number : int) -> int:
#    sum = 0
#    for i in str(number):
#        sum += int(i)
#    print(sum)
#sum_of_digits(9804396868)

#def sum_of_digits(number : int) -> int:
#    sum = 0
#    for i in str(number):
#        sum += int(i)
#    return sum
#print(sum_of_digits(9804396868))

#def sum_of_elements(my_list:list) -> int:
#    sum = 0
#    for i in my_list:
#        sum += int (i)
#    return sum
#print(sum_of_elements(my_list=[7,8]))

#def sum_of_elem(number : int, my_list : list) -> tuple:
#    sum,sum_list = 0,0
#    for i in str(number):
#        sum += int(i)
#    for j in my_list:
#        sum_list += int(j)
#    return sum,sum_list
#print(sum_of_elem(8948,[4,84,6,6]))

#def armstrong_number(number : int) -> int:
#    sum = 0
#    for i in str(number):
#        sum = sum + (int(i)**len(str(number)))
#    if sum == number:
#        return "Armstrong"
#    else:
#        return "Not Armstrong"
#print(armstrong_number(153))

#def prime_number(number : int) -> int:
#    for i in range (2,number):
#        if number%i==0:
#            return "Not Prime"
#    else:
#        return "Prime"
#print(prime_number(9))

#def number_type(number:int)->int:
#    if number%2==0:
#        return "Even"
#    else:
#        return "Odd"
#print(number_type(5))

#reverse a number and a string using function
#def revers(number : int, string:str) -> tuple:
#    revers_number,revers_string = 0,""
#    for i in string:
#        revers_string = i + revers_string
#    while number>0:
#        last_digit = number%10
#        revers_number = revers_number*10 + last_digit
#        number = number//10
#    return revers_number, revers_string
#print(revers(123,"LIFE"))

#make a random password generator using function

#import random, string
##coin = ("heads", "tails")
##toss = random.choice(coin)
##print(toss)
#x = string.ascii_letters
#y = string.digits
#z = string.punctuation
#all_together = x+y+z
#toss = random.choices(all_together,k=8)
#print(toss)

#def dictionary(my_dict:dict)->dict:
#    for i in range (1,15):
#        my_dict[i]=i**2
#    return my_dict
#print(dictionary(my_dict={}))

#def name(string : str)-> dict:
#    my_dict = {}
#    for i in string:
#        if i in my_dict:
#            my_dict[i] +=1
#        else:
#            my_dict[i] = 1
#    return my_dict
#print(name("subrata saha"))
   