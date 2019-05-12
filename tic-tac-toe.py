
# coding: utf-8

# In[ ]:

                             #**************** Created by Sushen Patidar  *****************

import random
def print_matrix(arr,arr1):                                                  #printing the matrix in formated way
    k=1
    o=1
    for j in range(0,3):
        print("                                          ",end=' ')
        for i in range(1,4) :                      
            print(f'| {arr[k]}',end=' ')
            k+=1
            
        print("|",end="                ")
        for i in range(1,4) :                      
            print(f'| {arr1[o]}',end=' ')
            o+=1
            
        print("|")




def check_winner(arr):                                                         ##checking if there is any winner or not
    if (arr[3]=='X' and arr[5]=='X' and arr[7]=='X')  or (arr[1]=='X' and arr[5]=='X' and arr[9]=='X' ) or (arr[1]=='X' and arr[2]=='X' and arr[3]=='X' ) or (arr[4]=='X' and arr[5]=='X' and arr[6]=='X') or (arr[7]=='X' and arr[8]=='X' and arr[9]=='X') or (arr[1]=='X' and arr[4]=='X' and arr[7]=='X') or (arr[2]=='X' and arr[5]=='X' and arr[8]=='X') or (arr[3]=='X'and arr[6]=='X' and arr[9]=='X') :
        return 1                                                               ## for won the match
    if (arr[3]== O' and arr[5]=='O' and arr[7]=='O')  or (arr[1]=='O' and arr[5]=='O' and arr[9]=='O' ) or (arr[1]=='O' and arr[2]=='O' and arr[3]=='O' ) or (arr[4]=='O' and arr[5]=='O' and arr[6]=='O') or (arr[7]=='O' and arr[8]=='O' and arr[9]=='O') or (arr[1]=='O' and arr[4]=='O' and arr[7]=='O') or (arr[2]=='O' and arr[5]=='O' and arr[8]=='O') or (arr[3]=='O'and arr[6]=='O' and arr[9]=='O') :
        return 1
    return 0
def check_draw(arr):                                                           ##checking if match is draw or not
    if arr[1]!=' ' and arr[2]!=' ' and arr[3]!=' ' and arr[4]!=' ' and arr[5]!=' ' and arr[6]!=' ' and arr[7]!=' ' and arr[8]!=' ' and arr[9]!=' ' :
        return 1                                                               ## match is draw
    else:
        return 0
def random_turn(mo=1) :                                                        ##return that which player has first chance to play 
    return random.randint(1,2)


def check_valid_input(arr,position):                                           ##checking that input given  by player is valid or not
    if  position<=0 or position>=10 or arr[position]=='X' or arr[position]=='O' :
        print('plz enter right input')
        return 0                                                               ##  0  wrong input
    return 1                                                                   ## 1 for right input        




def input_of_user(arr,position,X_or_O):                                       #placing the right symbol of current player "X" or "O".
    if X_or_O =='X':
        arr[position]='X' 
    else:
        arr[position]='O'
def start_game(user1,user2):                                                  ##logic of game
    arr=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    arr1=['0','1','2','3','4','5','6','7','8','9']
    print_matrix(arr,arr1)
    q=''
    turn=random_turn(1)
    if turn ==1:
        q=1
    else:
        q=2
    print(f'First turn is play by User{q}\n')
       
    a=9
    while a:
        b=0                                                                 ## deciding the symbole of players and turn
        if q==1:
            w=user1
        else:
            w=user2
        p=''
        if a%2==0:
            p='X'
        else :
            p='O'
        while b==0:
            position=int(input(f'enter your position({p}) {w} = '))         ##taking input of place from player
            b=check_valid_input(arr,position)                               ## checking valid input or not
            if b==1:
                break
        if a%2==0:
            X_or_O='X'
        else:
            X_or_O='O'
        input_of_user(arr,position,X_or_O)                                  ##placing the right symbol of current player "X" or "O"
        a=a-1
        
        print_matrix(arr,arr1)                                              ##printing the matrix
        if check_winner(arr)==1:                                           ##checking the winner
            print(f'.          Winner is     @ {w}')
            return q
        if check_draw(arr)==1:                                             ## match is draw or not
            print("Match is draw")
            break
        
        q+=1
        q=q%3                                                             ## decide the turn of which user
        if q== 0:
            q=1
        
    
def main(ram=1):                                    # main function
    print("""  ************          Welcome to tic toe game             ****************
                       
                       
                        Please enter the choise
                        # Press 1 : play with computer
                        # Press 2 : Play with another user""")
    user_choice=int(input())
    
    if user_choice==1 or user_choice==2 :
        user1=input("Enter user 1 Name=")
        user2=input("Enter user 2 Name=")                                           # taking the name of users
    user1_score=0
    user2_score=0
    while True:
        a=start_game(user1,user2)                                                   # start game(calling function)
        if a==1:
            user1_score+=1                                                          #adding the score
        elif a==2:
            user2_score+=1
        else: 
            pass
        a=input('.          press Q for exit\n or any other key to play again')         # input for play again or quit the game
        if a=='q' or a=='Q':
            break
    print("                      **** Score card  ****                ")              # final score card of user
    print(f"           {user1}         {user2}    ") 
    print(f"           {user2_score}                 {user2_score}")
    
    
    if user1_score>user2_score:                                                       ###   Final winner of game
        print(f".                            Winnner is {user1} !!!")
    elif user1_score==user2_score:                                    
        print('.                              Match is draw!!!')                           
    else :
        print(f".                             Winner is {user2} !!!")
     
main()                                                                                # calling main function



