# accessing string's cgharacters

f = 'abcdef'
# a index 0, b index 1 and so on
# f index -1, e index -2 and so on
index = 0
while index < len(f):
    letter = f[index]
    print(letter)
    index = index + 1

for char in f:
    print(char, end = '')

fruit = 'banana'
length = len(fruit)
index = length - 1
while index in range (0, len(fruit)):
    letter = fruit[index]
    print('\n',letter)
    index = index - 1

# For example you wanna use ' in string quotes'', so you have to use \ before ' to excape, similarly for "

# print ('O'Bhaiya') # gives error
print ('O\'Bhaiya') # fine now
print ('"Isn\'t," they said.')
print('First line.\nSecond line.')  # with print(), \n produces a new line
# in case you want to print \n then use r before quotes
print(r'C:\some\name') # without r (raw) break at n occurs


# string mutation

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:] # number before colon included, after colon excluded
print(new_greeting)
#gt = greeting[43] # Invalid
gt = greeting[:43] # valid
print (gt)

# count function for letter search in string using while

s = input ('Enter String: ')
string = str(s)

se = input ('Enter Search: ')
search = str(se)

def count(string,search):
    c = 0
    n = 0
    while n < len(string):
        if search == string[n]:
            c = c + 1
            n = n + 1
        else:
            n = n + 1
    return c

p = count(string,search)
print (p)

# count function for letter search in string using for

s = input ('Enter String: ')
string = str(s)

se = input ('Enter Search: ')
search = str(se)

def count(string,search):
    c = 0
    n = 0
    for num in string:
        n = str(num)
        if search == n:
            c = c + 1
    return c
p = count(string,search)
print (p)

# String comparison

w = input('Enter for Comparison: ')
word = str(w)

if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# String methods

stuff = 'Karakarakara   '
print (stuff.upper())
print (stuff.find('a')) # index which is 'a'
print (stuff.count('a')) # look for 'o'
print (stuff.count('a ')) # look for 'o '
print (stuff.count('ar',5)) # look for 'o ' from 5th letter
print (stuff.count('ra',5,9)) # look for 'o ' from 5th to 9th letter
print (stuff.strip()) # removes spaces before and after String
print (stuff.startswith('H')) # checks wether starts with H
print (stuff.lower().startswith('k')) # combining the two methods

# Parsing strings
# refer document - New Learnings for reference

print ('In %d years I have spotted %g %s.' % (1, 0.1, 'camels'))
print ('In %d years I have spotted %g %s.' % (12, 0.1, 'camels'))
print ('In %5d years I have spotted %g %s.' % (12, 0.1, 'camels'))
print ('In %+5d years I have spotted %-5g %s.' % (12, 0.1, 'camels'))
print ('In %-5d years I have spotted %g %s.' % (12, 0.1, 'camels'))
print ('In %05d years I have spotted %f %s.' % (12, 0.1, 'camels'))
print ('In %05d years I have spotted %5.2f %s.' % (12, 0.1, 'camels'))
print ('In %u years I have spotted %5.2f %s.' % (12, 0.1, 'camels'))
print ('In %e years I have spotted %g %c.' % (12, 0.1, 'a'))

while True:
    line = input('> ')
    if line.startswith('#'):  # cant use line[0] == '#' because if empty string then line[0] not exist
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# String in multiple lines (use three ''')

s = (r"""
Usage: thingy [OPTIONS]
     -h             Display this usage message
     -H hostname    Hostname to connect to
""")

print (s)
print(repr(s)) # helps while debugging

# String Concatenation
print (3 * 'un' + 'ium')

# Exercise

str = 'X-CoDSCoPAM-Confidence:0.8475'

fin = str.find(':')
print(fin)
nstr = str[fin+1:]
fnstr = float(nstr)
print (fnstr)

rstr = '##'

nrstr = str.replace('Co',rstr,4) # replaces 'Co' in str with '##' 4 times
print (nrstr)
