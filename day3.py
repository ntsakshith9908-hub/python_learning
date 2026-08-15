#1.int 
num_int = 6
print(num_int, type(num_int))

#2.float
num_float = 12.2
print(num_float, type(num_float))

#3.complex
num_complex = 2 + 4j
print(num_complex, type(num_complex))

#4.bool
is_python_simple = True
print(is_python_simple, type(is_python_simple))

#5.NoneType
value = None
print(value, type(value))

#6.string
name = "Akshith"
print(name, type(name))

#7.range
num_range = range(2, 8)
print(num_range, type(num_range))

#8.List
nums_list = [2, 4, 6, 8, 10, 12]
print(nums_list, type(nums_list))

#9.tuple
nums_tuple = (1, 2, 3, 4, 5)
print(nums_tuple, type(nums_tuple))

#10.set
num_set = {1, 3, 5, 7, 9}
print(num_set, type(num_set))

#11.dictionary
my_dict = {"name": "Akshith", "age": 22}
print(my_dict, type(my_dict))


#Type Conversionj

#int to float
a = 5
print("int to float: ", float(a))

#float to int
b = 9.3
print("float to int: ", int(b))

c = 123
print("int to str: ", str(c))

#str to int
d = "121"
print("str to int: ", int(d))

#list to tuple
num_list = [1, 4, 2, 5]
print("list to tuple: ", tuple(num_list))

#tuple to list
num_tuple = (3, 2, 1, 0)
print("tuple to list: ", list(num_tuple))

#list to set
num_list2 = [5, 6, 7, 8]
print("list to set: ", set(num_list2))

#range to list
range_nums = range(3, 7)
print("range to list: ", list(range_nums))