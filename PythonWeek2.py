#Question 1
my_list = list()
# print(type(my_list))

#Question 2
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# print(my_list)

#Question 3
my_list.insert(1, 15)
# print(my_list)

#Question 4
extended_list = [50,60,70]
my_list.extend(extended_list)
# print(my_list)

#Question 5 
my_list.pop(len(my_list) -1 )

# my_list.pop(7)
# print(my_list)

#Question 6
my_list.sort()
print(my_list)

#Question 7
print(my_list.index(30))
 