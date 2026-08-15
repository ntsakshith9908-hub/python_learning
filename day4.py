#Day 4
#Arithmetic Operators
print(10 + 5 * 2) #20
print(2 ** 3 ** 2) # 512
print(10 // 3) #3
print(10 % 3) #1 
print(5 / 2) # 2.5
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
print((1, 2, 3) + (4, 5, 6)) # (1, 2, 3, 4, 5, 6)
# print({1, 2, 3} + {4, 5, 6}) # TypeError
print([1, 2, 3] * 4) # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(*[1, 2, 43]) #1 2 43
print([1, 2, 3] + [1, 2, 3]) # [1, 2, 3, 1, 2, 3]
# print([1, 2, 3] + 'dog') #TypeError only concatenate list to list

#Relational and Logical Operators
print(10 > 5 and 20 < 30) # True
print(10 > 20 and 5 < 10) # False
print(not 1 == 1) # False
print(1 < 2 < 3) # True
print(1 > 2 > 3) # False
print('abc' > 'def') # False
print([1, 2, 3] > [1, 3, 4]) # False

# Assignment and walrus operator
# print(a = 10)  #TypeError
print(a := 10) # 10
if (n := 34) > 10:
    print(n)    # 34

# Identity and equality operators
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) #True
print(a is b) #False

a = 'abc'
b = 'abc'
print(a == b) #True
print(a is b) #True

a = (1, 2, 3)
b = (1, 2, 3)
print(a == b) #True
print(a is b) #True

#Membership operator
a = [1, 2, 3, 4, 5]
print(6 in a) #False
print(6 not in a) #True
print('abc' in 'abcde') #True