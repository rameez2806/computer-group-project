'''
This project is made by the following students:
1) Rameez khan
2) Sugam Agarwal
3) Aditya Jain

Class: XI C 
Session - 2022-23

'''


import random

def winner (c ,p):  #Rules of the game
    if c == p :
       return None
    elif c == 's' :
        if p == 'p' :
           return True
        elif p == 'x' :
            return False
    elif c == 'p' :
        if p == 's' :
            return False
        elif p == 'x' :
            return True
    elif c == "x" :
        if p == "s" :
           return True
        elif p == 'p' :
           return False

rounds = int(input('How much rounds you wanna play \n')) #asking user for how many rounds to be played
cs = 0 #computer initial score
ps = 0 #player initial score
p = ("Chose 's' for stone / 'p' for paper / 'x' for scizzor \n") #choice for user
c = random.randint(1,3) #computer choice
if c == 1 : 
    c = "s"
elif c == 2 :
    c = 'p'
elif c == 3:
    c = 'x'

for i in range(1 , rounds + 1) : #game begins!

    print('ROUND : ' , i)
    p = input("Chose 's' for stone / 'p' for paper / 'x' for scizzor \n")
    c = random.randint(1, 3)
    if c == 1:
        c = "s"
    elif c == 2:
        c = 'p'
    elif c == 3:
        c = 'x'

        
    a = winner(c,p) #calling function to chose the winner of round
    print('You choosed : ', p)
    print('Computer choosed : ', c)
    if a == None:
        print('The round was a tie :|')
    elif a == True:
        print("You won this round :)")
        ps += 1
    elif a == False:
        print('You loosed this round :(')
        cs += 1
    print('*' * 105)


print('Your score is : ' , str(ps)) #display user score
print("Computer Score is : " , str(cs)) #display computer's score

if cs > ps : #display the final result
    print('You losed the match')
elif cs < ps :
    print('You won the match')
elif cs == ps :
    print('The match is a tie')
