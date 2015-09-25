"""
distribution.py
Author: Sarah Dunbar
Credit: http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python

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

string = input ("Please enter a string of text (the bigger the better): ")
s = string.lower()
a = s.count("a")
b = s.count("b")
c = s.count("c")
d = s.count("d")
e = s.count("e")
f = s.count("f")
g = s.count("g")
h = s.count("h")
i = s.count("i")
j = s.count("j")
k = s.count("k")
l = s.count("l")
m = s.count("m")
n = s.count("n")
o = s.count("o")
p = s.count("p")
q = s.count("q")
r = s.count("r")
s = s.count("s")
t = s.count("t")
u = s.count("u")
v = s.count("v")
w = s.count("w")
x = s.count("x")
y = s.count("y")
z = s.count("z")
