#Create an empty list
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert 15 at 
my_list.insert(1, 15)

#Extend list 
my_list.extend([50, 60, 70])

my_list.pop()

#Sort in ascending order
my_list.sort()

#print
index_30 = my_list.index(30)
print("List:", my_list)
print("Index of 30:", index_30)
