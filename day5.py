# Day5
# 1. strip, lstrip, rstrip methods
a = "   python is simple   "
print(a.strip()) # python is simple
print(a.lstrip())# python is simple
print(a.rstrip())#    python is simple 

#2. replace
a = 'python is simple, python is easy, python is all-rounder'
b = a.replace('python', 'java')
print(a) # python is simple, python is easy, python is all-rounder
print(b) # java is simple, java is easy, java is all-rounder

#3. upper, lower, swapcase, title, capitalize
a = 'PYTHON is siMPLe'
print(a.lower()) # python is simple
print(a.upper()) # PYTHON IS SIMPLE 
print(a.swapcase()) # python IS SImplE
print(a.title()) # Python Is Simple
print(a.capitalize()) # Python is simple

#4. count, startswith, endswith
a = 'abacad'
b = a.startswith('a')
c = a.startswith('ad')
d = a.endswith('d')
e = a.endswith('de')
f = a.count('a')
g = a.count('ad')
print(b) # True
print(c) # False
print(d) # True
print(e) # False
print(f) # 3
print(g) # 1

# 5. find, rfind, index, rindex
s = 'abacada'
print(s.find('a')) # 0
print(s.find('a', 3)) # 4
print(s.find('a', 4, 8)) # 4
print(s.rfind('a')) # 6
print(s.rfind('a', 3)) # 6
print(s.rfind('a', 4, 8)) # 6
print(s.index('a')) # 0
print(s.index('a', 3)) # 4
print(s.index('a', 4, 8)) # 4
print(s.rindex('a')) # 6
print(s.rindex('a', 3)) # 6
print(s.rindex('a', 4, 8)) # 6
# print(s.index('z')) # Value Error
print(s.find('z')) # -1

# 6. is methods
#isspace
a = ''
b = 'a'
print(a.isspace()) # False
print(b.isspace()) # False

#isalpha
a = 'aBcD'
print(a.isalpha()) # True
b = 'aBcD1'
print(b.isalpha()) # False
c = 'aBc@D'
print(c.isalpha()) # False

#isdigit
a = '13'
print(a.isdigit()) # True
b = '12a'
print(b.isdigit()) # False

#isalnum
a = 'AbC123'
print(a.isalnum()) # True
b = 'Ab#C2' 
print(b.isalnum()) # False

#upper
a = '23$U'
print(a.isupper()) # True
b = '23%Ua'
print(b.isupper()) # False

# lower
a = '23$u'
print(a.islower()) # True
b = '23%uA'
print(b.islower()) # False

# split
a = 'badac'
print(a.split('a')) # ['b', 'd', 'c']
b = '   '
print(b.split('a')) # ['   ']
c = 'abaca'
print(c.split('a')) # ['', 'b', 'c', '']
d = 'iam a good person'
print(d.split()) # ['iam', 'a', 'good', 'person']

#join
a = '@'
l = [1, 2, 3]
t = (1, 2, 3)
s = {1, 2, 3}
d = {3: 1, 2: 3, 3: 1}
print(a.join(l)) # TypeError expected str, int found
print(a.join(t)) # TypeError expected str, int found
print(a.join(s)) # TypeError expected str, int found
print(a.join(d)) # TypeError expected str, int found

