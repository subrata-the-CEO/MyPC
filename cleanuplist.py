# takes a list. This list will contain numbers represented as strings.
# Your function should split this list into two new lists.
# The first list should contain only even numbers.
# The second only odd. Then, wrap these two lists in one main list and return it.
# Return an empty list if there are no even numbers, or odd.
# clean_up_list(["8"]) ➞ [[8], []]
# clean_up_list(["11"]) ➞ [[], [11]]
# clean_up_list(["7", "4", "8"]) ➞ [[4, 8], [7]]
# clean_up_list(["9", "4", "5", "8"]) ➞ [[4, 8], [9,5]

#list = ["15","42","36","79","58","33","52"]
#even_list = []
#odd_list = []
#blank_list = []
#for i in list:
#    if int(i)%2==0:
#        even_list.append(int(i))
#    else:
#        odd_list.append(int(i))
#print([even_list], ",", [odd_list])

#number = 6549814881847 #---- count even and odd number using while loop
#count_even = 0
#count_odd = 0
#while number>0:
#    if number%2==0:
#        count_even+=1
#    else:
#        count_odd+=1
#    number=number//10
#print("Even Number Present:",count_even,",","Odd Number Present:", count_odd)

