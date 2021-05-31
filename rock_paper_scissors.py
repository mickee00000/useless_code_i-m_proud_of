import random

computer = ['Rock', 'Paper', 'Scissors']

print('Enter your Choice:')
print("1.Rock\n2.Paper\n3.Scissors\n")

x = int(input())
y = ''

if x == 1:
    y = 'Rock'
elif x == 2:
    y= 'Paper'
elif x == 3:
    y = 'Scissors'

pc = random.choice(computer)

print("You       : "+y)
print("Computer  : "+pc)

if y == pc:
    print("Tie")
else:
    if         (y == "Rock" and pc == "Scissors") \
            or (y == "Scissors" and pc == "Paper")\
            or (y == "Paper" and pc == "Rock"):
        print("You Win..")
    else:
        print("You Lose..")