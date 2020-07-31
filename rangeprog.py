for item in range(10):
    print(item)


#List Comprehension

x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
    print(out)



    #-------------


y = [1,2,3,4]
out = [num**2 for num in y]
print(out)
