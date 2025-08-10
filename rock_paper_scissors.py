import random #library
print('To win 🙂‍↔️ the game you must know the rules:\n'
     +'1.Rock 2.Paper 3.Scissors/n'
     +'Rock vs Paper -> Paper wins\n'
     +'Paper vs Scissors -> Scissors wins\n'
     +'Rock vs Scissors -> Rock wins\n') #rules
while True:
    print('Enter u r choice 🫡 \n 1-Rock\n 2-Paper\n 3-Scissors\n') #choices
    choice=int(input("Enter your choice🤗: ")) #user choice
    while choice>3 or choice<1:
        choice = int(input("Enter a valid choice please ☺ : "))#if the user enters the wrong choice 
    #initialization of the choices
    if choice==1:
        choice_name='Rock'
    elif choice==2:
        choice_name='Paper'
    else:
        choice_name='Scissors'
    #printing the user choices
    print('User choice is😇: ',choice_name)
    print("Now It's for the computer choice...🤖🤖")
    #computer choice randomly any from the 1,2 and 3
    comp_choice = random.randint(1, 3) #random library
    #initialzation of computer choice
    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is: ",comp_choice_name)
    print("You VS Computer",choice_name,"vs",comp_choice_name)
    #chosing the winner
    if choice ==comp_choice:
        print("🫡Draw🫡")
    elif (choice == 1 and comp_choice == 3) or (choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice == 2):
        print("You win!🙂‍↔️🤗")
    else:
        print("Computer wins!😕")
    print("Do u want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing 🥳")
