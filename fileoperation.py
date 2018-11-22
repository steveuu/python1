'''
f=open('myfile.txt', 'r')

firstline=f.readline()
secondline=f.readline()
print(firstline, end='')
print(secondline)
'''
'''
for line in f:
    print(line, end='')
'''

'''
f=open('myfile.txt', 'a')

f.write('\nThis sentence will be appended.')
f.write('\nPython is fun!')

f.close
'''
'''
f=open('myfile.txt', 'r')

for line in f:
    print(line, end='')

f.close
'''
'''
i = open('myfile.txt', 'r')
o = open('myoutputfile.txt', 'w')

msg = i.read(10)

while len(msg):
    print (msg, '=', len(msg))
    o.write(msg)
    o.flush() #why do i need this? if buffering.
    msg=i.read(10)

i.close
o.close
'''
'''
inputF = open('ref.png', 'rb')
outputF = open('ref4.png', 'wb')

msg=inputF.read(10)
#msg=inputF.read()
#outputF.write(msg)

while len(msg):
    outputF.write(msg)
    outputF.flush() #when buffering, need this
    msg=inputF.read(10) 

inputF.close
outputF.close
'''
'''
import os
#os.rename('ref copy.png', 'a.png')
os.remove('a.png')
'''

