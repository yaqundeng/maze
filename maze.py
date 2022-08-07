from pygame.locals import *
import pygame


def grid(m, n):
    '''
        define a grid function to constuct the framework of a maze
        the function takes two positive integer parameters: m, n
        grid() returns a nested list which contains each line of 
        it prints out the lines
    '''
    if not isinstance(m, int) or not isinstance(n, int):
        raise TypeError
    if m <= 0 or n <= 0:
        raise ValueError
    i = 0
    j = 0
    maze_list = []
    while i <= m:
        j = 0
        nest = []
        while j <= n:
            if i == 0 or i == m or j == 0 or j == n:
                nest.append(1)
            else:
                nest.append(0)
            j += 1
        maze_list.append(nest)
        i+=1
    for b in range(1, n - 1):
        maze_list[5][b] = 1
    
    print( maze_list)
    return maze_list

##def maze(lst, i, j):
##    if not isinstance(lst, list):
##        raise TypeError
##    if not isinstance(i, int) or not isinstance(j, int):
##        raise TypeError
##    if len(lst) <= 0:
##        raise ValueError
##
##    if lst[7][7] == 2:
##        return True
##    else:
##        if lst[i][j] == 0:
##            lst[i][j] = 2
##            if maze(lst, i+1, j):
##                return True
##            elif maze(lst, i, j+1):
##                return True
##            elif maze(lst, i - 1, j):
##                return True
##            elif maze(lst, i, j - 1):
##                return True
##            else:
##                lst[i][j] = 3
##                return False
##        else:
##            return False


def is_valid_position(lst, i, j):
    if i < 0 or j < 0:
        return False
    if lst[i][j] == 1:
        return False
    if lst[i][j] == 0 or lst[i][j] == 2:
        return True
    return False


def maze(lst, i, j):
    stack = list()
    stack.append((i, j))
    while len(stack) > 0:
        i, j = stack.pop()

        if lst[7][7] == 2:
            print("GOAL")
            return True
        if lst[i][j] == 2:
            # Already visited
            continue
        # Mark position as visited
        lst[i][j] = 2
        # Check for all possible positions and add if possible
        if is_valid_position(lst, i+1, j):
            stack.append((i+1, j))

        if is_valid_position(lst, i, j+1):
            stack.append((i, j+1))

        if is_valid_position(lst, i, j-1):
            stack.append((i, j-1))

        if is_valid_position(lst, i-1, j):
            stack.append((i-1, j))

    # We didn't find a path, hence we do not need to return the path
    return False

def main():
    m = 8
    n = 8
    lst = grid(m, n)
    print(maze(lst, 1, 1))
    for i in range(m+1):
        for j in range(n+1):
            print(lst[i][j], end = "")
        print()


main()
