
#codinggrad task-2

#principle
p=10
#time
t=20
#rate
r=2

#find out the simple interest -- (p*t*r)/100
simpleInterest=(p*t*r)/100
print(simpleInterest)
#find out the compound interest --p*((1+r/100)**t-1)
compound_interest= p*((1+r/100)**t -1)
print(compound_interest)