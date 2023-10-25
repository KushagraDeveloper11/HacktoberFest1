from random import * #imports everything from that module
win=0
lose=0 
choice= int(input("You want to play 1 match or Best of 3 or Best of 5?\n"))
for i in range(0, choice):
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)
    '''

    #Write your code below this line 👇
    user= input("What you want to choose? Type R for Rock, P for Paper or S for Scissors.\n")
    if user=="R":
        print(rock)
    elif user=="P":
        print(paper)
    elif user=="S":
        print(scissors)
    else:
        print("Inalid Choice")
        
    print("Computer Chose:\n")
    comp= random.randint(0,2)
    if comp==0:
        print(rock)
    elif comp==1:
        print(paper)
    else:
        print(scissors)
      
    if (comp==0 and user=="R") or (comp==1 and user=="P") or (comp==2 and user=="S"):
        print("Match Drawn!\n")
    if (comp==0 and user=="P") or (comp==1 and user=="S") or (comp==2 and user=="R"):
        print("You Win!!\n")
        win+=1
        print(f"Your score is {win} - {lose}.\n")
    if (comp==0 and user=="S") or (comp==1 and user=="R") or (comp==2 and user=="P"):
        print("You Lose!\n")
        lose+=1
        print(f"Your score is {win} - {lose}.\n")
if win>lose:
    print(f"Your final score is {win} - {lose}. You Won!\n")
elif win<lose:
    print(f"Your final score is {win} - {lose}. You Lost!\n")
else:
    print(f"Your final score is {win} - {lose}. Match Drawn!\n")
