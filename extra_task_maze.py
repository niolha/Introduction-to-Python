"""
1) Лабиринт
Дан лабиринт (Матрица NxN) дана точка входа в лабиринт. Стеной является символ - # коридор - . Например

##########
.........#
######.###
#......###
#.####.###
#........#
##.#######
##.##.####
##......##
#######.##

enter = [1, 0]
exit = ???
Найти выход из лабиринта.
Учтите что лабиринты могут быть самыми разными, разного размера, без выхода и т/д/
"""

maze = [
    '##########',
    '.........#',
    '######.###',
    '#......###',
    '#.####.###',
    '#........#',
    '##.#######',
    '##.##.####',
    '##......##',
    '#######.##'
]

maze2 = [
    '###########',
    '........##',
    '######.####',
    '.......####',
    '#......####',
    '#.####.####',
    '#.####.####',
    '#.........#',
    '##.########',
    '##.##.#####',
    '##......###',
    '###.#######'
]

maze3 = [
    '###########',
    '.........##',
    '######.####',
    '.......####',
    '#......####',
    '#.####.####',
    '#.####.####',
    '#........##',
    '##.########',
    '##.##.#####',
    '##......###',
    '###########'
]



def is_wall(maze, row, col):
    wall = '#'
    if maze[row][col] == wall:
        return True
    else:
        return False


def get_neighbors1(row, col):    # для конкретного лабиринта "maze"
    neighbors = []
    if row - 1 >= 0:
        neighbors.append([row - 1, col])
    if row + 1 <= 9:
        neighbors.append([row + 1, col])
    if col - 1 >= 0:
        neighbors.append([row, col - 1])
    if col + 1 <= 9:
        neighbors.append([row, col + 1])
    return neighbors


print(get_neighbors1(1, 8))


def get_neighbors(maze, row, col):     ##для разных лабиринтов (не для всех)
    neighbors = []
    max_row = len(maze)
    max_col = len(maze[row])
    if row - 1 >= 0:
        neighbors.append([row - 1, col])
    if row + 1 <= max_row - 1:
        neighbors.append([row + 1, col])
    if col - 1 >= 0:
        neighbors.append([row, col - 1])
    if col + 1 <= max_col - 1:
        neighbors.append([row, col + 1])
    return neighbors


print(get_neighbors(maze2, 0, 9))


def replace_str(str_name, index, symbol):
    new_str = list(str_name)
    new_str[index] = symbol
    new_str = "".join(new_str)
    return new_str


def find_exit(maze, row, col):
    start = is_wall(maze, row, col)
    if start:
        print('It is NOT an entrance')
        return False
    list_of_neighbors = get_neighbors(maze, row, col)
    dots = []
    for elements in list_of_neighbors:
        dot = is_wall(maze, elements[0], elements[1])
        if dot == False:
            dots.append(elements)
    my_str = maze[row]
    maze[row] = replace_str(my_str, 0, '#')
    for dot in dots:
        row_dot = dot[0]
        list_of_neighbors_2 = get_neighbors(maze, dot[0], dot[1])
        if len(list_of_neighbors_2) < 4:
            print(f"{dot} is exit")
            return dot
        my_str2 = maze[row_dot]
        maze[row_dot] = replace_str(my_str2, dot[1], '#')
        for elements in list_of_neighbors_2:
            if not is_wall(maze, elements[0], elements[1]):
                dots.append(elements)
    if "." not in maze:
        print('No Exit')
    return True


find_exit(maze, 1, 0)
find_exit(maze2, 7, 10)
find_exit(maze3, 1, 0)
