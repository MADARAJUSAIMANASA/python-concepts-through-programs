# list functions
list=[] #empty list
list=[1,2,2,3,"python",3,True]
list.append("manasa")# add element into list
print(list)
list.extend(["hello","2"])#add multiple items into list
print(list)
print(list.count(3))#repation of the element in the list
print(list.index("python")) #item based get index value
list.insert(0,"sai")#index based on add element into list
print(list)
list.pop(2)#index based delete item
list.remove("hello")#element based delete item
print(list)
list.reverse()#reverse of the list
print(list)
list.clear()
print(list)
