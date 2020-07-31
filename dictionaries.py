#Dictionaries
my_stuff = {'key1':"value",'key2':"value2"}
print(my_stuff['key2'])

my_stuff2 = {"key1":"value",'key2':"value2",'key3':{'123':[1,2,'grabMe']}}

print(my_stuff2['key3']['123'][2])

print(my_stuff2['key3']['123'][2].upper())

my_stuff3 = {'lunch':'pizza','bfast':'eggs'}
print(my_stuff3['lunch'])
my_stuff3['lunch'] = 'burger'
my_stuff3['dinner'] = 'pasta'

print(my_stuff3)
