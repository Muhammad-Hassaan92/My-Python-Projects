import random
list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def print_board():
    board = f'''
 _______________________________________________________________
|       |       |       |       |       |       |       |       |
|   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |
|_______|_______|_______|_______|_______|_______|_______|_______|
|       |       |       |       |       |       |       |       |
|   {list[56]}   |   {list[57]}   |   {list[58]}   |   {list[59]}   |   {list[60]}   |   {list[61]}   |   {list[62]}   |   {list[63]}   |
|_______|_______|_______|_______|_______|_______|_______|_______|
|       |       |       |       |       |       |       |       |
|   {list[48]}   |   {list[49]}   |   {list[50]}   |   {list[51]}   |   {list[52]}   |   {list[53]}   |   {list[54]}   |   {list[55]}   |
|_______|_______|_______|_______|_______|_______|_______|_______|
|       |       |       |       |       |       |       |       |
|   {list[40]}   |   {list[41]}   |   {list[42]}   |   {list[43]}   |   {list[44]}   |   {list[45]}   |   {list[46]}   |   {list[47]}   |
|_______|_______|_______|_______|_______|_______|_______|_______|
|       |       |       |       |       |       |       |       |
|   {list[32]}   |   {list[33]}   |   {list[34]}   |   {list[35]}   |   {list[36]}   |   {list[37]}   |   {list[38]}   |   {list[39]}   |
|_______|_______|_______|_______|_______|_______|_______|_______|
|       |       |       |       |       |       |       |       |
|   {list[24]}   |   {list[25]}   |   {list[26]}   |   {list[27]}   |   {list[28]}   |   {list[29]}   |   {list[30]}   |   {list[31]}   |
|_______|_______|_______|_______|_______|_______|_______|_______|
|       |       |       |       |       |       |       |       |
|   {list[16]}   |   {list[17]}   |   {list[18]}   |   {list[19]}   |   {list[20]}   |   {list[21]}   |   {list[22]}   |   {list[23]}   |
|_______|_______|_______|_______|_______|_______|_______|_______|
|       |       |       |       |       |       |       |       |
|   {list[8]}   |   {list[9]}   |   {list[10]}   |   {list[11]}   |   {list[12]}   |   {list[13]}   |   {list[14]}   |   {list[15]}   |
|_______|_______|_______|_______|_______|_______|_______|_______|
|       |       |       |       |       |       |       |       |
|   {list[0]}   |   {list[1]}   |   {list[2]}   |   {list[3]}   |   {list[4]}   |   {list[5]}   |   {list[6]}   |   {list[7]}   |
|_______|_______|_______|_______|_______|_______|_______|_______|
'''
    print(board)

def enter_choice(player_choice,  alternative):
        if list[int(player_choice) - 1] in [" "]:
            list[int(player_choice) - 1] = alternative   
        elif list[int(player_choice) - 1] in ["X", "O"] and list[int(player_choice) + 7] in [" "]:
            list[int(player_choice) + 7] = alternative
        elif list[int(player_choice) + 7] in ["X", "O"] and list[int(player_choice) + 15] in [" "]:
            list[int(player_choice) + 15] = alternative
        elif list[int(player_choice) + 15] in ["X", "O"] and list[int(player_choice) + 23] in [" "]:
            list[int(player_choice) + 23] = alternative
        elif list[int(player_choice) + 23] in ["X", "O"] and list[int(player_choice) + 31] in [" "]:
            list[int(player_choice) + 31] = alternative
        elif list[int(player_choice) + 31] in ["X", "O"] and list[int(player_choice) + 39] in [" "]:
            list[int(player_choice) + 39] = alternative
        elif list[int(player_choice) + 39] in ["X", "O"] and list[int(player_choice) + 47] in [" "]:
            list[int(player_choice) + 47] = alternative
        elif list[int(player_choice) + 47] in ["X", "O"] and list[int(player_choice) + 55] in [" "]:
            list[int(player_choice) + 55] = alternative

def game():
    print("----------------------Welcome to the game.----------------------")
    players = input("Enter 'a' to play with computer and 'b' to play with a friend: ").lower()
    while players not in ["a", "b"]:
        players = input("Invalid Input. Enter 'a' to play with computer and 'b' to play with a friend: ").lower()

    if players == "a":
        player_one = input("Enter your name, player one: ")
        while player_one in [""]:
            player_one = input("Invalid Input, Enter your name, player one: ")
        player_two = "Computer"

    elif players == "b":
        player_one = input("Enter your name, player one: ")
        while player_one in [""]:
            player_one = input("Invalid Input, Enter your name, player one: ")
        player_two = input("Enter your name, player two: ")
        while player_two in ["", "Computer"]:
            player_two = input("Invalid Input, Enter your name, player two: ")
    tie = ""
    print("\n",f"{player_one}, your sign is 'X'")    
    print(f" {player_two}, your sign is 'O'")    
    print_board()

    attempts = 0
    while attempts >= 0:
        attempts += 1

        if attempts % 2 != 0:
            player_choice = choice(player_one)
            enter_choice(player_choice, "X")
            winner = determine_winner(player_one, player_two, tie)
        
        elif attempts % 2 == 0:
            if player_two in ["Computer"]:
                player_two_choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
                print(f"Computer chose {player_two_choice}")
                enter_choice(player_two_choice,  "O")
            elif player_two not in ["Computer"]:
                player_choice = choice(player_two)
                enter_choice(player_choice, "O")
        print_board()
        winner = determine_winner(player_one, player_two, tie)
        
        if winner == player_one:
            print(f"-----------------------------You win, {player_one}-----------------------------")
            break
        if winner == player_two:
            if player_two in ["Computer"]:
                print(f"-----------------------------The computer wins.-----------------------------")
                break            
            if player_two not in ["Computer"]:
                print(f"-----------------------------You win, {player_two}-----------------------------")
                break
        if winner == tie:
            print("-----------------------------Its a draw.-----------------------------")
            break
  
def determine_winner(player_one, player_two, tie):
#   winner condition for horizontal rows
    for i in [1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 25, 26, 27, 28, 29, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45]:
        if   list[i-1:i+3] == ['X', 'X', 'X', 'X']:
            return player_one
        elif list[i-1:i+3] == ['O', 'O', 'O', 'O']:
            return player_two
#   winner condition for vertical rows
    for i in [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]:
        if   [list[i], list[i+8], list[i+16], list[i+24]] == ['X', 'X', 'X', 'X']:
            return player_one
        elif [list[i], list[i+8], list[i+16], list[i+24]] == ['O', 'O', 'O', 'O']:
            return player_two
#   winner condition for right diagonal
    for i in [0, 1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 25, 26, 27, 28, 29, 33, 34, 35, 36]:
        if   [list[i], list[i+9], list[i+18], list[i+27]] == ['X', 'X', 'X', 'X']:
            return player_one
        elif [list[i], list[i+9], list[i+18], list[i+27]] == ['O', 'O', 'O', 'O']:
            return player_two
#   winner condition for left diagonal
    for i in [3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 19, 20, 21, 22, 23, 27, 28, 29, 30, 31, 35, 36, 37, 38, 39]:
        if   [list[i], list[i+7], list[i+14], list[i+21]] == ['X', 'X', 'X', 'X']:
            return player_one
        elif [list[i], list[i+7], list[i+14], list[i+21]] == ['O', 'O', 'O', 'O']:
            return player_two
#   tie condition
    while " " not in list:
        return tie

def choice(player):
    player_choice = input(f"Enter the column, {player}: ")
    while player_choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            player_choice = input(f"Invalid choice. Enter the column, {player}: ")
    if list[int(player_choice) - 1] in [" "] or list[int(player_choice) + 7] in [" "] or list[int(player_choice) + 15] in [" "] or list[int(player_choice) + 23] in [" "] or list[int(player_choice) + 31] in [" "] or list[int(player_choice) + 39] in [" "] or list[int(player_choice) + 47] in [" "] or list[int(player_choice) + 55] in [" "]:
        pass
    elif list[int(player_choice) - 1] in ["X", "O"] and list[int(player_choice) + 7] in ["X", "O"] and list[int(player_choice) + 15] in ["X", "O"] and list[int(player_choice) + 23] in ["X", "O"] and list[int(player_choice) + 31] in ["X", "O"] and list[int(player_choice) + 39] in ["X", "O"] and list[int(player_choice) + 47] in ["X", "O"] and list[int(player_choice) + 55] in ["X", "O"]:
        print(f"This column is full, {player}. Choose another column.")
        choice(player)   
    return player_choice

game()