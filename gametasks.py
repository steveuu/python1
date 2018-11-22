

def printInstructions():
    instructions= 'These are the instructions.'
    print(instructions)

def getUS(userName=''):
    #print('inside getUS')
    try:
        userFile = open('userScores.txt', 'r')
    except:
        userFile = open('userScores.txt', 'w')
        print ('File not found')
        userFile.close
        return -2
        
    lineF = userFile.readline()
    #print('lineF2:', lineF2)
    #print('i am 1')
    while len(lineF):
        #print('i am 1a')
        content = lineF.split(',')
        for i, s in enumerate(content):
            content[i] = s.strip()
            
        if len(content) >= 2:
            if content[0]==userName or userName=='':
                print(content[0] + ' --> ' + content[1])
                
        lineF = userFile.readline()
    #print('i am 2')
    userFile.close
    return 1


def updateUS(userName, userScore):
    import os
    bFound=False
    userFile = open('userScores.txt', 'r')
    userTemp = open('userScores.tmp', 'w')
    lineF = userFile.readline()
    while len(lineF): 
        content = lineF.split(',')
        for i, s in enumerate(content):
            content[i] = s.strip()
        if len(content)>=2:                               
            if content[0]==userName:
                lineT=content[0]+','+str(userScore)
                userTemp.write(lineT + '\n')
                print(content[0] + '\'s score updated from', content[1], 'to', str(userScore))
                bFound=True
            else:
                lineT=content[0]+','+ str(content[1])
                userTemp.write(lineT + '\n')
        lineF = userFile.readline()

    if not bFound:
        lineT=userName + ',' + str(userScore)
        userTemp.write(lineT + '\n')
        print(userName, 'added!')
        
    userTemp.close
    userFile.close

    #now transfer
    os.remove('userScores.txt')
    os.rename('userScores.tmp', 'userScores.txt')
 
    getUS()
                
        
        

        
                       
        
    
    


        
