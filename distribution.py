"""
distribution.py
Author: Sarah Dunbar
Credit: http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python, Geoff Dunbar, https://wiki.python.org/moin/HowTo/Sorting/, Anoushka Alavilli, Mr. Dennison

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
letterdictionary = {"a":25, "b":24, "c":23, "d":22, "e":21, "f":20, "g":19, "h":18, "i":17, "j":16, "k":15, "l":14, "m":13, "n":12, "o":11, "p":10, "q":9, "r":8, "s":7, "t":6, "u":5, "v":4, "w":3, "x":2, "y":1, "z":0}
letterpos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
for x in letterpos:
    b = letters[x]
    r = s.count(b)
    list1[x] = r

def letternums (letter):
    i = letterdictionary[letter]
    return i
    
print ('The distribution of characters in "' +  string  + '" is: ')
tuplelist = zip(list1, letters)
tuplist = sorted(tuplelist, key=lambda lise: 1000*lise[0] + letternums(lise[1]), reverse=True)
for x in tuplist:
    if x[0] > 0:
        i = x[0]
        while i > 0:
            print(x[1], end = "")
            i = i - 1
        print("", end="\n")


    

    