#Problem 1

s = 'django'
#Use indexing to print out the following

#'d'
print(s[0])

#'o'
print(s[5])

#'djan'
print(s[:4])

#'jan'
print(s[1:4])

#'go'
print(s[4:])

#Reverse the String
print(s[::-1])


#Problem 2
#nested list
l = [3,7,[1,4,'hello']]

#Reassigning "hello to be goodbye"
l[2][2] = 'goodbye'
print(l)


#Problem 3

#Using keys and index pairs

d1 = {'simple_key': 'hello'}

print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}

print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])


#Problem 5
age = 4
name = "Sammy"

#Using print formate
print("hello my dog's name is {a} and he is {b} years old.".format(a=name, b=age))
