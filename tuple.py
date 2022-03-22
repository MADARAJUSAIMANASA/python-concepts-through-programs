#Tuple
t=()# Empty Tuple
td=("hello",1,2,3.3)
print("index =",td[0])# index
td=(1,1,2,3.3)
print("count =",td.count(1))# count
print("minimum =",min(td))# minimum of the tuple
print("maximum =",max(td))# maximum of the tuple
print("sum =",sum(td))# sum of The bulit-in functions
print("len =",len(td))#length of the tuple
#  Example
tuple=(1,2,3,4,5)
ty=(1,2,3,4,5)
l=[]
for i in tuple:
    for j in ty:
        if i == j:
            c =i+j
            print(c)
            l.append(c)
print(l)

