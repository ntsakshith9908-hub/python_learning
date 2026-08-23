#1.print numbers from 1 to 10
for i in range(1, 11):
    print(i, end = " ")
print('\n\n')

#2.print even numbers from 1 to 30 
list = [4, 3, 5, 2, 5, 2, 9, 1, 7, 4, 6, 8]
# using range
for i in range(1, 31):
    if i % 2 == 0:
        print(i, end = " ")
print()
# using for each and iterating through list
for x in list:
    if x % 2 == 0:
        print(x, end = " ")
print()

#3. print odd numbers from 1 to 30
for i in range(1, 31):
    if i % 2 == 1:
        print(i, end = " ")
print('\n')

#4. print numbers divisible by 5 from 1 to 30
for i in range(1, 31):
    if i % 5 == 0:
        print(i)
print()

#5. print numbers divisible by 5 and 7 from 1 to 30
for i in range(1, 31):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
print()

#6. sum of numbers from 10 to 25
total = 0
for i in range(10, 26):
    total += i 
print(total)

#7. multiplication table of a number
n = 7
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")
print()

#8. factorial of a number
n = 5
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(f'Factorial of {n} is {fact}')
print()

#9. fibonacci of numbers
n = int(input("Enter number of Fibonacci "))
a = 0
b = 1
for i in range(n):
    print(a, end = " ")
    a, b = b, a + b 
print()

#10. reverse a string
word = "Akshith"
res = word[::-1]
print(res)
# or 
word = "Akshith"
rev = ""
for char in word:
    rev = char + rev
print(rev)
print()
# or using range
rev = ""
for i in range(len(word) - 1, -1, -1):
    rev = rev + word[i]
print(rev)
print()

#11. count vowels in string 
str = "Akshith"
for char in str.lower():
    if char in 'aeiou':
        print(char, end= " ")
print()


#12. 
pass

#13. check whether a number a prime or not 
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