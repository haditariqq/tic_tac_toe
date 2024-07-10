import random

tic_tac_toe = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

num=random.randint(1,10)
if num % 2 == 0:
    print("Player 1 starts (X)")
    print("Player 2 is O")
else:
    print("Player 2 starts (X)")
    print("Player 1 is O")

for row in tic_tac_toe:
    for index , i in enumerate(row):
        if index==2:
            print(i, end=" ")
        else:
            print(i + " |", end=" ")
    print('\n__________')
for turn in range(5):
    player_1_row=int(input("Enter your row number(0/1/2): "))
    player_1_column=int(input("Enter your column number(0/1/2): "))
    while tic_tac_toe[player_1_row][player_1_column]=="O" or tic_tac_toe[player_1_row][player_1_column]=="X":
        print("This space is already taken, enter a different space")
        player_1_row=int(input("Enter your row number(0/1/2): "))
        player_1_column=int(input("Enter your column number(0/1/2): "))
    tic_tac_toe[player_1_row][player_1_column]="X"
    for row in tic_tac_toe:
        for index , i in enumerate(row):
            if index==2:
                print(i, end=" ")
            else:
                print(i + " |", end=" ")
        print('\n__________')
    if turn >=2:
        if (tic_tac_toe[0][0] == tic_tac_toe[0][1]==tic_tac_toe[0][2]=="X") or (tic_tac_toe[1][0] == tic_tac_toe[1][1]==tic_tac_toe[1][2]=="X") or (tic_tac_toe[2][0] == tic_tac_toe[2][1]==tic_tac_toe[2][2]=="X") or (tic_tac_toe[0][0] == tic_tac_toe[1][0]==tic_tac_toe[2][0]=="X") or (tic_tac_toe[0][1] == tic_tac_toe[1][1]==tic_tac_toe[2][1]=="X") or (tic_tac_toe[0][2] == tic_tac_toe[1][2]==tic_tac_toe[2][2]=="X") or (tic_tac_toe[0][0] == tic_tac_toe[1][1]==tic_tac_toe[2][2]=="X") or (tic_tac_toe[0][2] == tic_tac_toe[1][1]==tic_tac_toe[2][0]=="X"):
            print("Player X wins")
            break

    player_2_row=int(input("Enter your row number(0/1/2): "))
    player_2_column=int(input("Enter your column number(0/1/2): "))
    while tic_tac_toe[player_2_row][player_2_column]=="O" or tic_tac_toe[player_2_row][player_2_column]=="X":
        print("This space is already taken, enter a different space")
        player_2_row=int(input("Enter your row number(0/1/2): "))
        player_2_column=int(input("Enter your column number(0/1/2): "))
    tic_tac_toe[player_2_row][player_2_column]="O"
    for row in tic_tac_toe:
        for index , i in enumerate(row):
            if index==2:
                print(i, end=" ")
            else:
                print(i + " |", end=" ")
        print('\n__________')
    if turn >=2:
        if (tic_tac_toe[0][0] == tic_tac_toe[0][1]==tic_tac_toe[0][2]=="O") or (tic_tac_toe[1][0] == tic_tac_toe[1][1]==tic_tac_toe[1][2]=="O") or (tic_tac_toe[2][0] == tic_tac_toe[2][1]==tic_tac_toe[2][2]=="O") or (tic_tac_toe[0][0] == tic_tac_toe[1][0]==tic_tac_toe[2][0]=="O") or (tic_tac_toe[0][1] == tic_tac_toe[1][1]==tic_tac_toe[2][1]=="O") or (tic_tac_toe[0][2] == tic_tac_toe[1][2]==tic_tac_toe[2][2]=="O") or (tic_tac_toe[0][0] == tic_tac_toe[1][1]==tic_tac_toe[2][2]=="O") or (tic_tac_toe[0][2] == tic_tac_toe[1][1]==tic_tac_toe[2][0]=="O"):

            print("Player O wins")
            break

