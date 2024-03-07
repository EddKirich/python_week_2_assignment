#create an empty list
my_list = []
#appending elements [10, 20, 30, 40] into the list
my_list.extend([10, 20, 30, 40])
#insert value 15 at the second position. The second position is "1"
my_list.insert(1, 15)
#extend the list with another list
my_list.extend([50, 60, 70])
#removing the last element from the list
my_list.pop()
#sorting the list in ascending order
my_list.sort()
#find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
#print the final state of the list
print("Final my_list:", my_list)
