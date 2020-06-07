import random
from colorama import Fore, Style


def disp():
    '''
    To display the board
    :return:
    '''
    for i in board:
        for j in i:
            print(Fore.BLUE + str(j), end=" | ")

        print("\n--+---+---+")


def gen_xy(player_input):
    '''
    Its to generate the x and y coordinates of each cell in the board based
    on the position entered by the user
    :param player_input:
    :return:
    '''
    x = int(player_input / 3)
    y = player_input % 3
    return x, y


def check(flag):
    '''
    to check whether player wins,computer wins or its draw
    its determined by the value of flag that's passed
    :param flag:
    :return:
    '''
    # global flag
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] == csymbol:
            flag = 1
        else:
            flag = 2
    if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][0] == csymbol:
            flag = 1
        else:
            flag = 2

    if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][0] == csymbol:
            flag = 1
        else:
            flag = 2

    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] == csymbol:

            flag = 1
        else:
            flag = 2
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[0][1] == csymbol:

            flag = 1
        else:
            flag = 2
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[0][2] == csymbol:
            flag = 1
        else:
            flag = 2

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == csymbol:
            flag = 1

        else:
            flag = 2

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == csymbol:
            flag = 1

        else:
            flag = 2

    return flag


def game(chances):
    '''
    game function is where the symbols needed and moves are read from user and board
    is updated accordingly
    :param chances:
    :return:
    '''
    while chances > 0:
        player_input = int(input(Fore.WHITE + 'Enter your move : '))
        x, y = gen_xy(player_input)
        board[x][y] = psymbol

        chances = chances - 1
        plist.append(player_input)
        for i in range(9):
            cplayer = random.randint(0, 8)
            if cplayer not in plist:
                break
        plist.append(cplayer)
        chances = chances - 1
        x, y = gen_xy(cplayer)
        board[x][y] = csymbol
        val = check(flag)
        if val == 1:
            print(Fore.GREEN + "Game Over")
            print(Fore.GREEN + Style.BRIGHT + "Computer Wins!")
            chances = 0

        elif val == 2:
            print(Fore.GREEN + "Game Over")
            print(Fore.GREEN + Style.BRIGHT + "Player Wins!")
            chances = 0

        disp()

    if val == 0 and chances == -1:
        print(Fore.GREEN + "Game Over")
        print(Fore.GREEN + Style.BRIGHT + "Its a Draw !")


choice = 'Y'
while (choice == 'Y'):
    board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    chances = 9
    flag = 0
    print(Fore.RED + Style.BRIGHT + "*********** Tic Tac Toe ***************\n")
    plist = []
    csymbol = '*'
    flag = 0
    psymbol = input(Fore.YELLOW + "Enter your Symbol  ")
    disp()
    game(chances)
    choice = input(Fore.MAGENTA + "Do you want to play again? (Y/N)  ").upper()
