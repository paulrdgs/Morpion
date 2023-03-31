map = [
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . '],
]

player = 'Joueur 1'



def draw():
    for i in range(3):
        for j in range(3):
            print(map[i][j], end="")
        print()


def check_win():
    for i in range(3):
        if map[i][0] == map[i][1] == map[i][2] != ' . ':
            return True
        
    for i in range(3):
        if map[0][i] == map[1][i] == map[2][i] != ' . ':
            return True
    
    if map[0][0] == map[1][1] == map[2][2] != ' . ':
        return True
    elif map[0][2] == map[1][1] == map[2][0] != ' . ':
        return True
        
    return False


def check_draw():
    for i in range(3):
        for j in range(3):
            if map[i][j] == ' . ':
                return False
            
    return True



while True:
    choice = int(input(f'{ player } [1-9] ? > '))
    row = (choice - 1) // 3
    column = (choice - 1) % 3

    if map[row][column] == ' . ':
        map[row][column] = ' X ' if player == "Joueur 1" else ' O '

    draw()

    if check_win():
        print(f'{ player } a gagné !')
        break

    if check_draw():
        print(f'égalité !')
        break

    player = 'Joueur 1' if player == 'Joueur 2' else "Joueur 2"