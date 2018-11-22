class Game:

    def __init__(self, noOfQuestions=0):
        self.checkNoOfQuestions(noOfQuestions)

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        self.checkNoOfQuestions(noOfQuestions)

    def checkNoOfQuestions(self, value):
        if value<1:
            print('Minimum Number of Questions = 1. Hence, number of questions will be set to 1.')
            self._noOfQuestions = 1
        elif value>10:
            print('Maximum Number of Questions = 10. Hence, number of questions will be set to 10.')
            self._noOfQuestions = 10
        else:
            print('Number of questions will be set to', str(value) + '.')
            self._noOfQuestions = value


class BinaryGame(Game):
    def generateQuestions(self):
        #import randint
        #declare local variable called score
        #use for loop to generate questions and evaluate answers
        #return the value of score

        from random import randint
        #return randint(0,20)

        score=0

        for i in range(self.noOfQuestions):
            base10 = randint(1,100)
            userResult = input('Convert ' + str(base10) + ' to binary: ')
            
            while True:
                try:
                    #cast user's answer to an integer and evaluate the answer
                    #update user score based on the answer
                    #break out from the while True loop using the break stmt

                    iResult = int(userResult, base = 2)
                    if iResult==base10:
                        print ('Good! Correct!')
                        score+=1
                        break
                    else:
                        #print ('Sorry, wrong! The answer is:', str(bin(base10)))
                        print ('Sorry, wrong! The answer is: {:b}'.format(base10))
                        break
                        
                except:
                    #print error msg if casting fails
                    #prompt user to key in the answer again
                    userResult = input('Answer not a valid binary number.\nPlease convert ' + str(base10) + ' to binary: ')

        print('Final score:', str(score))
        return score

class MathGame(Game):
    def generateQuestions(self):
        #import randint
        from random import randint

        #declare four local vars called score, numberList, symbolList, and operatorDict
        score=0
        numberList = [0,0,0,0,0]
        symbolList = ['','','','']
        operatorDict = {1:'+', 2:'-', 3:'*', 4:'**'}

        #use for loop to generate questions and evaluate the answers
        for i in range(self.noOfQuestions):
            for j in range(0,5):
                numberList[j] = randint(1,4)    

            for j in range(0,4):
                while True:
                    symbolList[j] = operatorDict[randint(1,4)]
                    if not (j>0 and symbolList[j]=="**" and symbolList[j]==symbolList[j-1]):
                        break
                    #else:
                        #print('Repeat **')
                        #print(symbolList)

            #print(numberList)
            #print(symbolList)

            questionString=''

            for i in range(len(numberList)-1):
                questionString+=str(numberList[i])+symbolList[i]
                
            questionString+=str(numberList[i])

            result = eval(questionString)
            
            questionString=questionString.replace('**', '^')

            #print(questionString)
            #print(result)

            while True:
                try:
                    userResult = int(input(questionString + ' = '))
                    if userResult==result:
                        print ('Good! Correct!')
                        score+=1
                    else:
                        #print ('Sorry, wrong! The answer is:', str(bin(base10)))
                        print ('Sorry, wrong! The answer is:', str(result))
                    break
                except:
                    userResult = input('Please enter an integer.\n' + questionString + ' = ')

        #return the value of score
        print('Final score:', str(score))
        return score
























    
            

        

        
