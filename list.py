mylist1 =[1,2,3]
print(mylist1)
mylist2 = ['stringabcdefgh',1,2,3,4,True,'asfg',[1,2,3]]
print(mylist2)
print(len(mylist1))



mylist3 = ['a','b','c','d','e']
print(mylist3[0])
print(mylist3[-1])
print(mylist3[1:])
print(mylist3[:3])

print("before reassignment")
print(mylist3)
mylist3[0] = 'New Item'
print("after reassignment")
print(mylist3)


#mylist3.append(["x","y","z"])
print(mylist3)

listtwo = ["x","y","z"]
mylist3.extend(listtwo)
print(mylist3)


mylist = ['a','b','c','d','e']
item = mylist.pop()
print(mylist)
print(item)

mylist.reverse()
print(mylist)

mylist4 = [4,6,2,3,8,6,45]
mylist4.sort()
print(mylist4)



mylist5 = [1,2,['x','y','z']]
print(mylist5[2])
print(mylist5[2][1])

#List Comprehensive
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0]for row in matrix]
print(first_col)
