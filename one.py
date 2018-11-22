#Prints the words "Hello World"
'''
print ("Hello World")
x=5
y=10
y=x
print ("x = ", x)
print ("y = ", y)

brand = 'Apple'
exchangeRate = 1.235235245
message = 'The price of this %s laptop is %d USD and the exchange \
rate is %4.2f USD to 1 EUR' % (brand, 1299, exchangeRate)
print (message)
 
message = 'The price of this \'{0:s}\' laptop is {1:d} USD and the exchange \
rate is {2:4.2f} USD to 1 EUR'.format(brand, 1299, exchangeRate)
print (message)

message = 'The price of this {} laptop is {} USD and the exchange \
rate is {} USD to 1 EUR'.format(brand, 1299, exchangeRate)
print (message)

print ('this is %s' % ('cool'))
msg='this is %s' % ('warm')
print (msg)

print (int(5.712987))
print (float("2.123"))
print (str(123))
print (int("1"))

userAge = [0,1,2,3,4]
print (userAge)

#user2 = []
#print (user2)

print (userAge[1])
print (userAge[-2])

userAge2 = userAge[0:5]
print (userAge2)
userAge2 = userAge[0:5:2]
print (userAge2)
userAge2 = userAge[:5:2]
print (userAge2)
userAge2 = userAge[1::2]
print (userAge2)
userAge2 = userAge[0::2]
print (userAge2)


userAge = [0,1,2,3,4]
print (userAge)

userAge[1]=1.1
print (userAge)

userAge.append('99')
print (userAge)

del userAge[1]
print (userAge)

myList = [0,1,2,3,4,'Hello']
print (myList)
myList2=myList[1:3]
print (myList2)

months=('', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', \
        'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
print (months)

print (months[3])

userNameAge = {"Andy":30, "Bob":31, "Chuck":32, "Doug":33, "andy":34}
print (userNameAge["Andy"])

userNameAge2=dict(Andy=130, Bob=131, Chuck=132, Doug=133, andy=134)
userNameAge2["Bob"]=222
print (userNameAge2)

userAdd={}
userAdd["Alice"]=3
del userAdd["Alice"]
print (userAdd)

myName = input('Please enter your name: ')
myAge = input('Hi, %s, what about your age: ' % (myName.upper()))
myAge = input('Hi, {0:12}, what about your age: '.format(myName.upper()))

print ('Hello World, my name is', myName, 'and I am', myAge, 'years old.')

print ('Hello World, my name is %s and I am %d years old.' \
       % (myName, int(myAge)))

print ('Hello World, my name is {0:s} and I am {1:d} years oldd.'.format(myName, int(myAge)))


print ('one\ntwo')
print ('I said, \'Go away!\'')
'''

#print (2==5 and 2==2)
'''
if 1==2:
    print ('1')
elif 2==3:
    print ('2')
    print ('2a')
elif 3==4:
    print ('3')
else:
    print ('end')

userInput = input('Enter 1 or 2: ')
if userInput=='1':
    print ('You entered %s' % (userInput))
elif userInput=='2':
    print ('You entered %s' % (userInput))
else:
    print ('You entered neither.')

'''

'''
num1 = 1 if 1==2 else 2
print ('%d' % (num1))
print ('{0:3}'.format(num1))
'''
'''
userAge = [0,1,2,3,4]
for a in userAge:
    print (a)

for i, a in enumerate(userAge): print (i, a)
'''

userNameAge = {"Andy":30, "Bob":31, "Chuck":32, "Doug":33, "andy":34}
'''
print ('\n')
for a in enumerate(userNameAge):
    print (a)
'''
'''
for a, b in enumerate(userNameAge):
    #print (b, a)
    #print ('Member %d is %s and zhey are %d years old.' % (a, b, userNameAge[b]))
    print ('Member {0:d} is {1:s} and {1:s} is {2:d} years old.'.format(a, b, userNameAge[b]))


for i, j in userNameAge.items():
    print ('Name = %s, Age = %d' % (i, j))

for i in 'hello':
    print (str(i) + '\n')

for i in range(12, 13):
    print (i)
'''
'''
i=0
while i<13:
    print ('counter =', i)
    if i==5:
        i+=1
        continue
    print ('hi', i)
    i+=1
'''
'''
try:
    answer=int(12/5)
    print (answer)
except:
    print ('error')
'''
'''
try:
    userInput1=int(input('Please enter a number: '))
    userInput2=int(input('Please enter another number: '))
    answer=userInput1/userInput2
    print ('The answer is ', answer)
    myFile=open('missing.txt', 'r')
except ValueError as e:
    print ('Value Error')
    print (e)
except ZeroDivisionError:
    print ('Zero Div Error')
except Exception as e:
    print ('Unknown error: ', e)
           

newString = "Hello World".replace("World", "Universe")
print (newString)
'''
'''
def Func1(a, b):
    return a/b

response=Func1(6,2)
print (response)
'''
'''
def CheckIfPrime(a):
    for i in range(2, a):
        if (a%i==0):
            return False
    return True

a=8
print ('Yes, %d is prime' % (a) if CheckIfPrime(a) else 'No, %d is not Prime' % (a))
'''
'''
msg1='Global var'
def fxn1():
    print ('\nINSIDE FXN1')
    #Global vars are accessible inside a function
    #print (msg1)
    #declaring a local var
    msg1='Local var'
    print (msg1)

fxn1()
print (msg1)
'''
'''
def fSteve(a, b, c=2):
    print (a+b+c)

fSteve(1,2)
'''
'''
def addNums(*num):
    sum = 0
    for i in num:
        sum+=i
    print (sum)

addNums(1,2,3,1,1,1,1,1,1)
'''
'''
def printMembers(**age):
    for i,j in age.items():
        print(i, j)
        print('Name %s. Age %d' % (i,j))
        print('Name {0}! Age {1}!'.format(i,j))
         
printMembers(John=10, Mike=20)

def all3(a, *b, **c):
    print (a)
    sum=0
    for i in b:
        sum+=i
    print(sum)
    for i,j in c.items():
        print(i, j)

all3('i am a', 1,2,13,z=3,y=2,x=1)
'''
'''
import random as r

a=r.randrange(1,10)
print(a)
'''
'''
from random import randrange as rr, randint as rint

a=rr(10,15)
print(a)
a=rint(2,22)
print(a)

import sys
if '/Users/Steve/Documents/python learning/sub' not in sys.path:
    sys.path.append('/Users/Steve/Documents/python learning/sub')

import prime as p
print(p.CheckIfPrime(23))

from prime import CheckIfPrime as chkprime
a=43
print(a, chkprime(a))

import sys
print(sys.path)

import sys
sys.path.remove('/Users/Steve/Documents/python learning/sub')

print(sys.path)
'''


