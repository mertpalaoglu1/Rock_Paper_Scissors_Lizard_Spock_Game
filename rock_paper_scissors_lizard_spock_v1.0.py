import random as rnd
import time 

''' 
    Final Project for Aygaz Python Bootcamp lead by Global AI Hub.
    Code is written by Mert Palaoğlu, the game is inspired by The Big Bang Theory show.
    Gameplay explained : https://www.youtube.com/watch?v=pIpmITBocfM
    
'''

def rock_paper_scissors_lizard_Spock_MERT_PALAOGLU():
    roundsPlayed=0
    playerScore=0
    computerScore=0
    moves=['rock','paper','scissors','lizard','spock']

    time.sleep(2) #Little delay for beginning:
    print("**************************************************************************************")
    print('Hello my dear rival, welcome to the game!')
    print("You know It's so boring to play regular rock paper scissors for great minds like Us.")
    print('So I have made the game little bit more complicated for Us. ENJOY!')
    print("--------------------------------------------------------------------------------------")
    time.sleep(2)
    print('Rules:')
    print('There are 5 characters that a player can choose, each character has win and lose chance to other characters. So if I choose the character that beats yours,')
    print('I win. So choose wisely. We will play until one of us has 2 wins.')
    print("You can always type 'Exit' to leave the game.")
    print("--------------------------------------------------------------------------------------")
    time.sleep(2)
    print('Characters:')
    print('Scissors: Cuts Paper, decapitates Lizard, but is smashed by Spock and crushed by Rock.')
    print('Paper: Covers Rock, disproves Spock, but is cut by Scissors and eaten by Lizard.')
    print('Rock: Crushes Scissors and Lizard, but is covered by Paper and vaporized by Spock.')
    print('Lizard: Poisons Spock, eats Paper, but is crushed by Rock and decapitated by Scissors.')
    print('Spock: Smashes Scissors, vaporizes Rock, but is poisoned by Lizard and disproved by Paper.')
    print("--------------------------------------------------------------------------------------")
    time.sleep(2)
   
    print("Are you confused already? Let's get started then!")
    print("--------------------------------------------------------------------------------------")

    #Game stars:
    while True: 
        playerScore=0
        computerScore=0
        roundsPlayed=0

        while playerScore<2 and computerScore<2:
            print('Round:',roundsPlayed+1)

            #valid input test and exit komutları

            while True:
                choice=input('Choose your Character(rock, paper, scissors, lizard, spock):').lower()
                if choice in moves:
                    break
                elif (choice.lower()=='exit' and roundsPlayed==0): 
                    print('Why did you wanna play then you fool!')
                    return 0
                elif(choice.lower()=='exit'and roundsPlayed!=0):
                    print('You may leave now, Go!')
                    return 
                else:
                    print("You couldn't even choose a valid character, could you?")
                    
            computerChoice=rnd.choice(moves)
            print('I pick the',computerChoice)

            #choosing and error komutları
            if choice==computerChoice:   
                print("It's a tie, great mind think alike!")

            elif (choice.lower()=='rock' and (computerChoice=='scissors' or computerChoice=='lizard')) or \
                 (choice.lower()=='paper' and (computerChoice=='rock' or computerChoice=='spock')) or \
                 (choice.lower()=='scissors' and (computerChoice=='paper' or computerChoice=='lizard')) or \
                 (choice.lower()=='lizard' and (computerChoice=='paper' or computerChoice=='spock')) or \
                 (choice.lower()=='spock' and (computerChoice=='scissors'or computerChoice=='rock')):
                print('You got lucky this round!')
                playerScore+=1
            else:
                print('Haha, I win this round!')
                computerScore+=1

            roundsPlayed+=1
            time.sleep(2)
            print('--------------------------------------------------------------------------------------')
            print(f'ScoreBoard: Player= {playerScore}, Computer={computerScore} \n')   

            #result komutları

        if playerScore==2:
            time.sleep(1.5)
            print('--------------------------------------------------------------------------------------')
            print("You win the Game, I'm actually impressed! ")
        elif computerScore==2:
            time.sleep(1.5)
            print('--------------------------------------------------------------------------------------')
            print("I win the Game, It was so easy!")  

           #play again komutları    

        print('--------------------------------------------------------------------------------------')
        newGame=input('Wanna play one more ? (yes/no): ').lower()
        computernewGame=rnd.choice(['no','yes'])

        if (newGame=='yes' and computernewGame=='yes'):
            continue
        elif(newGame=='yes' and computernewGame=='no'):
            print("Well I don't wanna play no more! Leave!")
            break
        else:
            print("It was a good game, come again sometime!")
            break

rock_paper_scissors_lizard_Spock_MERT_PALAOGLU()