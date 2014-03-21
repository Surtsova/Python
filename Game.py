from random import randint

board = []                        #Создание листа

for x in range(5):
    board.append(["O"] * 5)       #Создает игровое поле размером 5х5 и заполняет его символами "O"

def print_board(board):           #Функция, для вывода игрового поля на экран
    for row in board:
        print " ".join(row)      

print "Let's play Battleship!"
print_board(board)                #Вызов функции печати

def random_row(board):            #Функция генерирования случайной строки для корабля
    return randint(0, len(board) - 1)

def random_col(board):            #Функция генерирования случайного столбца для корабля
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)     #Присвоение переменной значение функции random_row
ship_col = random_col(board)     #Присвоение переменной значение функции random_col

for turn in range (9):          #Цикл повторяется до тех пор, пока колличество попыток не станет равным 10
    guess_row = int(raw_input("Guess Row:"))   #Ввод пользователем строки (от 1 до 5)
    guess_col = int(raw_input("Guess Col:"))   #Ввод пользователем столбца (от 1 до 5)
    
    if guess_row-1 == ship_row and guess_col-1 == ship_col:  #Если введенная пользователем клетка совадает с местонахождением корабля, выводится сообщение и проиходит выход из цикла
        print "Congratulations! You sunk my battleship!"
        break
    else:   #Если введенная клетка не является нужной
        if (guess_row-1 < 0 or guess_row-1 > 4) or (guess_col-1 < 0 or guess_col-1 > 4): #Если введенная клетка находится вне поля
            print "Oops, that's not even in the ocean."
        elif(board[guess_row-1][guess_col-1] == "X"): #Если пользователь уже вводил данную клетку
            print "You guessed that one already."
        else:  #Если введенная клетка свободна - вывод сообщения и замена значения клетки на "X"
            if turn==10: #Если кол-во попыток равно 10
                print "Game Over"
            print "You missed my battleship!"
            board[guess_row-1][guess_col-1] = "X"
    print "Turn", turn + 1 #Вывод кол-ва попыток
    print_board(board) #Вызов функции печати
