# Hacker rank Program On Conditional Stmts
# Task 1
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Code

n = int(input().strip())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# Task 2

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True,
# otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to theis_leap 
# function. It is only necessary to complete the is_leap function.
# Input:
# 1990
# Sample Output:
# False

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))