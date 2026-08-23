#create a list with 3 elements
my_list = [1, 2, 3]
#INSERT OPERATIONS
#appending
#add 5 types of non-sequence elements to it with append
my_list.append(6) #int
my_list.append(5.5) #float
my_list.append(True) #Boolean
my_list.append(3 + 4j) #complex
my_list.append(None) #None Type
print(my_list)
#add 5 types of sequences to it with append
my_list.append('Hi') #string
my_list.append([2, 3]) #list
my_list.append((3, 4)) #tuple
my_list.append(range(3)) #range
my_list.append(b"abc") #bytes
print(my_list)
#extending
#add 5 types of non-sequence elements to it with extend
my_list = [2, 4, 6]
# my_list.extend(10) #TypeError
# my_list.extend(3.14)  #TypeError
# my_list.extend(2+5j) #TypeError
# my_list.extend(True) #TypeError
# my_list.extend(None) #TypeError

#add 5 types of sequence elements to it with extend
#inserting
my_list = [1, 2, 3]
#insert an element at index 1 and print
my_list.insert(1, 50)
print(my_list)
#insert an element at index -1 and print
my_list = [1, 2, 3]
my_list.insert(-1, 50)
print(my_list)
#insert an element at index 10000 and print
my_list = [1, 2, 3]
my_list.insert(10000, 50)
print(my_list)
#insert an element at index -10000 and print
my_list = [1, 2, 3]
my_list.insert(-10000, 50)
print(my_list)

#DELETE OPERATIONS
#create a list with 1,2,1,3,4,1
my_list = [1, 2, 1, 3, 4, 1]
#pop element at index 3 and print element and list
my_list = [1, 2, 1, 3, 4, 1]
element = my_list.pop(3)
print(element)
print(my_list)
#pop last element and print element and list
my_list = [1, 2, 1, 3, 4, 1]
element = my_list.pop()
print(element)
print(my_list)
#remove first 1 from list and print element and list
my_list = [1, 2, 1, 3, 4, 1]
my_list.remove(1)
print(my_list)

#clear all elements in the list
my_list = [1, 2, 1, 3, 4, 1]
my_list.clear()
print(my_list)

#UPDATE OPERATIONS
#create a list with 3,2,1,5,4 
my_list = [3, 2, 1, 5, 4]
#sort the list in ascending and print
my_list.sort()
print(my_list)
#create a list with 3,2,1,5,4 
my_list = [3, 2, 1, 5, 4]
#sort the list in descending and print
my_list.sort(reverse = True)
print(my_list)
#create a list with 3,2,1,5,4 
my_list = [3, 2, 1, 5, 4]
#reverse the list and print
my_list.reverse()
print(my_list)

#READ OPERATIONS
#create a list with 1,2,1,3,1,2
my_list = [1, 2, 1, 3, 1, 2]
#find count of 1 and 2 in list
print(my_list.count(1))
print(my_list.count(2))
#find index of 1 from start
print(my_list.index(1))
#find index of 1 from 2nd index
print(my_list.index(1, 2))
#find index of 1 from 5th index
# print(my_list.index(1, 5)) # Value error


#TUPLE
#create a tuple with 1,2,1,3,1,2
my_tuple = (1, 2, 1, 3, 1, 2)
#find count of 1 and 2 in tuple
print(my_tuple.count(1))
print(my_tuple.count(2))
#find index of 1 from start
print(my_tuple.index(1))
#find index of 1 from 2nd index
print(my_tuple.index(1, 3))
#find index of 1 from 5th index
# print(my_tuple.index(1, 5)) # ValueError 







