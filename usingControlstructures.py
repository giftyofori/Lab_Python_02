#ex5

theInput=raw_input("Enter an integer then press 'enter': ")
i=int(theInput)
if i%2==0:
     print"this is an even number"
else:
    print"this is odd"

#ex6
school_age=5
voting_age=18
retiring_age=60
presidential_age=40
personsAge=input('enter your age and press enter')
j=personsAge
if j< school_age and j>0:
        print"you are too young"
    
if j>=voting_age:
        print"remember to vote on 7th december"
if j>=presidential_age and j>= voting_age and j>0:
        print"vote for me"

elif j< presidential_age and j>0:
        print'you cant be president'
if j>= retiring_age:
        print'you are too old'
elif j<0:
    print"i dont know where you fit"

#ex7
for i in range(40,-1,-1):
    if i%3==0:
        print i
        
#ex8
for k in range(6,31,1):
    if (k%2!=0) and (k%3!=0) and (k%5!=0):
        print k

#ex9
n=0
for n in range(0,100,1):
    while (n*79)%97==1:
        print n
        n= n+1

