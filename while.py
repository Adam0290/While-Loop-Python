#while loop

num = 0

while num < 10:
    num += 1
    print (num)

import random
rand_num = random.randint(0,50)
my_num = 50

while rand_num != my_num: #The not-equal-to operator ( != ) 
    print(rand_num)
    rand_num = random.randint(0,50)

print("You've found{}!".format(my_num))