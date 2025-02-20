import random
l=["rock","paper","scissor"]
while True:
    choose=int(input('''
Want to play the game...?
1.Yes
2.No
                     '''))
    if(choose==1):
        my_count=0
        computer_count=0
        for a in range(0,5):
            userInput=int(input('''
1.rock
2.paper
3.scissor
                     '''))
            if userInput==1:
                myans="rock"
            elif userInput==2:
                myans="paper"
            elif userInput==3:
                myans="scissor"
            computer_ans=random.choice(l)
            
            if myans==computer_ans:  
                print("Your Answer",myans)
                print("Computer Answer",computer_ans)
                print("Draw")
                my_count=my_count+1
                computer_count=computer_count+1
            elif (myans=="rock" and computer_ans=="scissor") or (myans=="paper" and computer_ans=="rock") or (myans=="scissor" and computer_ans=="paper"):
                print("Your Answer",myans)
                print("Computer Answer",computer_ans)
                print("You Win")
                my_count=my_count+1
            else:
                print("Your Answer",myans)
                print("Computer Answer",computer_ans)
                print("Computer Win")
                computer_count=computer_count+1
        print()
        print()
        if(my_count==computer_count):
            print("Final Result :")
            print("Your Count",my_count)
            print("Computer Answer",computer_count)
            print("Game Draw")
            
        elif my_count>computer_count:
            print("Final Result :")
            print("Your Count",my_count)
            print("Computer Answer",computer_count)
            print("You Win The Game")
        else:
            print("Final Result :")
            print("Your Count",my_count)
            print("Computer Answer",computer_count)
            print("You lose the game")
            
    else:
        break
        
