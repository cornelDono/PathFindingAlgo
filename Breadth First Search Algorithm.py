import queue

def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", "O", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", "#", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", " ", "X", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", "#", " ", "#", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])

    return maze

def one_step_move(move, colPlace, rowPlace):
    if move == 'L':
        colPlace -=1

    elif move == 'R':
        colPlace += 1

    elif move == 'U':
        rowPlace -= 1
        
    elif move == 'D':
        rowPlace+= 1
    
    return colPlace, rowPlace


def printMaze(maze, path=''):
    for x, row in enumerate(maze):
        for y, col in enumerate(row):
            if col == "O":
                i = y
                i = x

    pos = set()

    for move in path:
        i, j = one_step_move(move, i, j)
        pos.add((j,i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j,i) in pos:
                print("+ ", end = "")
            else:
                print(col + " ", end = "")
        print()

def validMaze(maze, moves):
    for x, row in enumerate(maze):
        for y, col in enumerate(row):
            if col == "O":
                i = y
                j = x

    for move in moves:
        i, j = one_step_move(move, i, j)
        
        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#" or maze[j][i] == "0"):
            return False

    return True

def showStep(maze, moves, rowPlace, colPlace):
    for move in moves:
        colPlace, rowPlace = one_step_move(move, colPlace, rowPlace)

        for j, row in enumerate(maze):
                for i, col in enumerate(row):
                    if (j,i) == (rowPlace,colPlace):
                        print("* ", end = "")
                    else:
                        print(col + " ", end = "")
                print()

def findEnd(maze, moves):
    for x, row in enumerate(maze):
        for y, col in enumerate(row):
            if col == "O":
                i, startI = y, y
                j, startJ = x, x

    for move in moves:
        i, j = one_step_move(move, i, j)

    
    if maze[j][i] == "X":
        print('Found: ' + moves)
        printMaze(maze, moves)
        showStep(maze, moves, startJ, startI)

        return True

    return False


if __name__== '__main__':
    nums = queue.Queue()
    nums.put('')
    add = ''
    maze = createMaze2()

    while not findEnd(maze, add):
        add = nums.get()

        for j in ['L', 'R', 'U', 'D']:
            put = add + j
            if validMaze(maze, put):
                if len(put) < 3:
                    nums.put(put)
                else:
                    if put[-1] == "L" and put[-2] != "R" or put[-1] == "R" and put[-2] != "L" or put[-1] == "U" and put[-2] != "D" or put[-1] == "D" and put[-2] != "U":
                        nums.put(put)       


