#STRING


mystring = 'abcdefg'
print(mystring[0])
print(mystring[-1])
print(mystring[4])


#Basics
'hello'
"hello"
"I'm a dog"

#Indexing
myline = 'abcdefg'
print(myline[3])

#Slicing
mystring = 'abcdefgh'
print(mystring[2:])
print(mystring[4:])
print(mystring[:3])
print(mystring[2:5])
print(mystring[:])
print(mystring[::1])
print(mystring[::2])

#String is immutable
#mystring[0] = 'X';


#Basic Methods

mystring = 'Hello World'
x = mystring.capitalize();
x = mystring.split('o');
print(x)


#Print Formatting
x = "Insert another string here: {}".format("INSERT ME!")
y = "Item One: {} Item Two: {}".format("dog","cat")
z = "Item One: {x} Item Two: {y}".format(x= "dog",y = "cat")
print(x)
print(y)
print(z)
