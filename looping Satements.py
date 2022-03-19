# task-7 looping Statements while loop,for loop
a=4
b=1
# Using while loop
while a > b:
    if b == 3 :
       print("while loop ",b)
       break
    b+=1

#using for loop
for i in range(0,10,2):
    if i==6:
       print("for loop ",i)
    continue
