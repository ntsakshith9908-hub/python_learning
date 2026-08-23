#important problems
#1. print numbers from 1 to 10
for i in range(1, 11):
    print(i, end = " ")
print('\n\n')

#2. print even numbers from 5 to 30 and above list 
list = [4, 3, 5, 2, 5, 2, 9, 1, 7, 4, 6, 8]
for i in range(5, 31):
    if i % 2 == 0:
        print(i, end = " ")
print()

# using for each and iterating through list
for x in list:
    if x % 2 == 0:
        print(x, end = " ")
print()

#3. print odd numbers from 5 to 30 and above list
list = [4, 3, 5, 2, 5, 2, 9, 1, 7, 4, 6, 8]
# using range
for i in range(1, 31):
    if i % 2 == 1:
        print(i, end = " ")
print()
# using for each and iterating through list
for x in list:
    if x % 2 == 1:
        print(x, end = " ")
print()

#4. print numbers divisible by 5 from 1 to 30 and above list
for i in range(1, 31):
    if i % 5 == 0:
        print(i, end = " ")
print('\n')
list = [4, 3, 5, 2, 5, 2, 9, 1, 7, 4, 6, 8]
for x in list:
    if x % 5 == 0:
        print(i, end = " ")
print()

#5. print numbers divisible by both 5 and 7 from 1 to 100 and above list
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end = " ")
print()
list = [4, 3, 5, 2, 5, 2, 9, 1, 7, 4, 6, 8]
for x in list:
    if x % 5 == 0 and x % 7 == 0:
        print(i, end = " ")
print('\n')


#6. sum of numbers from 10 to 25 and above list
total = 0
for i in range(10, 26):
    total += i
print(total)

total = 0
list = [4, 3, 5, 2, 5, 2, 9, 1, 7, 4, 6, 8]
for x in list:
    total += x 
print(total)

#7. multiplication table of a number 
n = int(input())
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

#8. factorial of a number
n = int(input())
fact = 1
if n == 0 or n == 1:
    fact = 1
else:
    for i in range(1, n + 1):
        fact = fact * i
print(f'Factorial of {n} is {fact}')


#9. fibonacci of numbers
n = int(input("Enter number of Fibonacci "))
a = 0
b = 1
for i in range(n):
    print(a, end = " ")
    a, b = b, a + b 
print()

#10. reverse a string
#method1
word = "Akshith"
res = word[::-1]
print(res)
#method2
word = "Akshith"
rev = ""
for char in word:
    rev = char + rev
print(rev)
print()
#method3
word = "Akshith"
rev = ""
n = len(word)
for i in range(n - 1, -1, -1):
    rev = rev + word[i]
print(rev)
print()

#11. count vowels in a string 
#method1
str = "Akshith"
for char in str.lower():
    if char in 'aeiou':
        print(char, end= " ")
print()
#method2
str = "Akshith"
vowels = ['a', 'e', 'i', 'o', 'u']
for char in str.lower():
    if char in vowels:
        print(char, end= " ")
print()


#12. count z's and y's in a string
#method1
word = "fuzzy"
z_count = word.count('z')
y_count = word.count('y')
print("z count: ", z_count)
print("y_count: ", y_count)

#method2
word = "fuzzy"
z_count = 0
y_count = 0
for char in word:
    if char == 'z':
        z_count += 1
    elif char == 'y':
        y_count += 1
print("z count: ", z_count)
print("y_count: ", y_count)

#13. check whether a number is prime number or not
n = int(input('Enter the Number: '))
is_prime = True
if n < 2:
    print("Not a Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False 
            break
if is_prime:
    print("Prime")
else:
    print("Not a Prime")