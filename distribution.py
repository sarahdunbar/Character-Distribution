"""
distribution.py
Author: Sarah Dunbar
Credit: http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python, Geoff Dunbar, https://wiki.python.org/moin/HowTo/Sorting/

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""

import copy
string = input ("Please enter a string of text (the bigger the better): ")
s = string.lower()
list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letterpos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
for x in letterpos:
    b = letters[x]
    r = s.count(b)
    list1[x] = r
    
def letternums (letterpos):
    for x in letterpos:
        b = letters[x]
    
print ("The distribution of characters in '" + string + "' is: ")
tuplelist = zip(list1, letters)
tuplist = sorted(tuplelist, key=lambda 1000*lise[0] + (26 - letternums(letterpos)), reverse=True)
print(tuplist)











#list2 = copy.deepcopy(list1)
#list2.sort()
#print ("The distribution of characters in "' + string + '" is: ")
#letterpos2 = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#for x in letterpos2:
#    biggie = list2[x]
#    z = list1.index(biggie)
#    letter = letters[z]
#    while biggie > 0:
 #       print(letter, end="")
 #       biggie = biggie -1
  #  print("", end="\n")


    

    