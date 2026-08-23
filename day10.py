list = [4, 3, 2, 5, 6]
n = len(list)
#print elements in list with for each loop
for num in list:
    print(num)
#print elements in list with index based for loop
for i in range(n):
    print(i, list[i])

#skip printing even numbers in list
for num in list:
    if num % 2 == 0:
        continue
    print(num, end= " ")
print()

#skip printing odd numbers in list
for num in list:
    if num % 2 == 1:
        continue
    print(num, end= " ")
print()

#when number 2 comes stop printing  
for num in list:
    if num == 2:
        break
    print(num, end= " ")
print()

#when first odd number comes stop printing
for num in list:
    if num % 2 == 1:
        break
    print(num, end= " ")
print()

#print numbers from 1 to 10, when all numbers are printed, print 'All numbers printed'
for i in range(1, 11):
    print(i)
print("All numbers printed")

#print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All
#  numbers printed'
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
print("All numbers printed")
#print numbers from 10 to 1, when 5 comes stop printing, when all numbers are print, print 'All numbers printed'
for i in range(10, 0, -1):
    if i == 5:
        break
    print(i)
print("All numbers printed")
