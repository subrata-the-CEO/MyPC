# find the armstrong number in the list

my_list = ["153","151","9374","7354"]
n = 0
#using for loop:
#for i in my_list:
#    sum = 0
#    for j in i:
#        sum = sum + (int(j)**len(str(i))) # 0
#        print("Number = ", i,"Sum = ", sum)
#    if sum == int(i):
#        print(f"Armstrong {i}")
#    else:
#        print("Not Armstrong")

#using while loop:
#while n<len(my_list):
#    temp_var = int(my_list[n])
#    sum=0
#    length = int(my_list[n])
#    while temp_var>0:
#        last_digit = temp_var%10
#        sum = sum + (last_digit**len(str(my_list[n])))
#        temp_var//=10
#    print(length)
#    if sum == length:
#        print("Armstrong")
#    else:
#        print("Not Armstrong")
#    n+=1

#using both for & while loop:
#my_list = ["153","151","2597","784591"]
#for i in my_list:
#    sum = 0
#    temp_ver = int(i)
#    while temp_ver>0:
#        last_digit=(temp_ver%10)
#        sum=sum+(last_digit**len(str(i)))
#        temp_ver//=10
#    print(sum)
#    if sum==int(i):
#        print("Armstrong")
#    else:
#        print("Not")