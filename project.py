import gameclasses as gc
import gametasks as gt

try:
    #declare variables
    mathInstructions='In this game, you will be given a simple arithmetic question.\
        \nEach correct answer gives you one mark.\
        \nNo mark is deducted for wrong answers.'
    
    binaryInstructions='In this game, you will be given a number in base 10.\
        \nYour task is to convert this number to base 2.\
        \nEach correct answer gives you one mark.\
        \nNo mark is deducted for wrong answers.'

    userName=input('Name: ')

    gt.updateUS(userName, 0)
    gt.getUS()
    totalScore=0
    
    #use a while loop to run the program until the user choose to exit
    while True:
        try:
            sGame = input('Would you like to play the (B)inary Game or the (M)ath Game? ')
            sGame=sGame.upper()
        
            if sGame!='B' and sGame!='M':
                print('Not a valid choice.')
            else:
                break

        except Exception as e:
            print(e)
  
    while True:
        try:
            if sGame=='M':
                mg=gc.MathGame(2)
                score = mg.generateQuestions()
            else:
                bg=gc.BinaryGame(2)
                score = bg.generateQuestions()

            totalScore+=score
            
            if input('Play again? ').upper()!='Y':
                print('Thanks for playing!')
                #print('Score:', str(score))
                print('Total Score this session:', str(totalScore))
                break
            
        except Exception as e:
            print(e)
    
    #update the user's score after zhe exits the program
    gt.updateUS(userName, totalScore)
    gt.getUS()
            
    #gt.updateUS(userName, gt.score)
    
except Exception as e:
    #inform the users that an error has occured and the program will exit
    print(e)
    quit

