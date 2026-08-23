#SET METHODS
#create a empty dict and print its type
my_dict = {}
print(type(my_dict))
#create a empty set and print its type
unique = set()
#add 5 non-sequences and 5 sequences to that set with add method
#5 non-sequences
unique.add(5)
unique.add(6.5)
unique.add(5 + 7j)
unique.add(True)
unique.add(None)
print(unique)
# 5 sequences
unique.add('python')
unique.add([1, 3]) # TypeError unhashable list
unique.add((2, 4))
unique.add({5, 6}) # TypeError unhashable set
unique.add({'b': 1, 'd': 3})  # TypeError unhashable dict
print(unique)
#add 5 non-sequences and 5 sequences with update method
unique = set()
# 5 non-sequences
unique.update(5) # TypeError 
unique.update(6.5) # TypeError 
unique.update(6 + 7j) # TypeError 
unique.update(True) # TypeError 
unique.update(None) # TypeError
# 5 sequences
unique.update("Python")
unique.update([2, 4])
unique.update((5, 6))
unique.update({7, 8})
unique.update({"g", 7})
print(unique)
#print a set and remove first element from that set
print(unique)
unique.pop()
print(unique)
#remove one existing and one non-existing element from that set
unique.remove(7)
unique.remove(100) # KeyError 100 doesn't exist
#discard one existing and one non-existing element from that set
unique.discard(8)
unique.discard(100) # no Key Error even the 100 doesn't exist
#remove all elements from the set
unique.clear()
print(unique)

#create a set {1,2,3,4}, a list [3,4,5,6]. 
set = {1,2,3,4}
lst = [3,4,5,6]
#write union of set and list
print(set.union(lst))
#write intersection of set and list
print(set.intersection(lst))
#write difference of set and list
print(set.difference(lst))
#write symmetric difference of set and list
print(set.symmetric_difference(lst))
#use union, intersection, difference, symmetric difference operators on set and another set. try to change second type of list and see outputs
set1 = {1, 3, 5, 4}
set2 = {2, 3, 6, 4}
# union
print(set1 | set2)
#intersection
print(set1 & set2)
#difference
print(set1 - set2)
#symmetric difference
print(set1 ^ set2)
#DICT METHODS
#create a empty dict
my_dict = {}
print(my_dict)

#extend dict with another dict
my_dict.update({'a': 1, 'b': 2})
print(my_dict)
#extend dict with another list
my_dict.update([('c', 3), ('d', 4)])
print(my_dict)
#extend dict with another tuple
my_dict.update((('e', 5), ('f', 6)))
print(my_dict)
#extend dict with another set
my_dict.update({('g', 7), ('h', 8)})
print(my_dict)

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
freq = {1:'a', 2:'b', 3:'c', 4:'d'}
print(freq)
#remove the pair with key 4
freq.pop(4)
print(freq)
#remove the pair with key 100
freq.pop(100) # KeyError 100 doesn't exist
print(freq)
#remove the pair with key 100 if not there return 'z'
print(freq.pop(100, 'z'))

#remove the last pair
freq.popitem()
print(freq)
#remove all elements from the dict
freq.clear()
print(freq)

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
dict1 = {1:'a', 2:'b', 3:'c', 4:'d'}
print(dict1)
#get the value of key 4
print(dict1.get(4)) # d
#get the value of key 100
print(dict1.get(100)) # None
#get the value of key 100, if key is not present get 'z'
print(dict1.get(100, 'z')) # z

#get the value of key 4 with setdefault
print(dict1.setdefault(4)) # d
#get the value of key 100 with setdefault
print(dict1.setdefault(100)) # None
#get the value of key 100 with setdefault, if key is not there add 100 with 'z'
print(dict1.setdefault(100, 'z')) 
#get all keys of dict and print its type
print(dict1.keys())
print(type(dict1.keys()))
#get all values in dict and print its type
print(dict1.values())
print(type(dict1.values()))
#get all items in dict and print its type
print(dict1.items())
print(type(dict1.items))


