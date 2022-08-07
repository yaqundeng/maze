"""
    CS5001
    Final Project, 12/13/2021
    Fall 2021
    Yaqun Deng
    Filename: maze-1.py

    This project mainly contains two parts: a maze framework,
    an moving object. It is designed to direct the moving
    object to find a proper way to exit the maze.

    The project was based on the skills and knowledge learned from CS 5001.
    Data structures like strings, tuples, and nested lists are applied to this
    project. Another focus is recursion. Recursion was used to find the way
    from the entrance to the exit. Implemented classes by defining attributes
    and methods including constructors and string methods.

    Other features like if-else statements, nested loops, multiway conditionals,
    logical operators, boolean expressions, and error handling are also
    included in this project.
"""


import pygame


class Maze:
    """
        define a Maze class to construct the framework of a maze
        the grid() function takes two positive integer parameters: m, n
        grid() returns a nested list which contains each line
    """

    # defensive coding

    def __init__(self, m, n):
        if not isinstance(m, int) or not isinstance(n, int):
            raise TypeError
        if m <= 0 or n <= 0:
            raise ValueError
        self.m = m
        self.n = n

    # define a grid function to construct the framework of a maze
    # takes no parameters
    # return a nested list

    def grid(self):
        i = 0
        maze_list = []
        while i <= self.m:
            j = 0
            nest = []
            while j <= self.n:
                if i == 0 or i == self.m or j == 0 or j == self.n:
                    nest.append(1)
                else:
                    nest.append(0)
                j += 1
            maze_list.append(nest)
            i += 1
        maze_list[0][1] = 0
        maze_list[11][17] = 0

        # set up blocks in the maze

        for b in range(self.n - 8, self.n - 2):
            maze_list[8][b] = 1
        for a in range(1, self.n - 6):
            maze_list[2][a] = 1
        for c in range(11, self.n + 1):
            maze_list[10][c] = 1
        for d in range(9, 12):
            maze_list[d][9] = 1
        for e in range(2, 9):
            maze_list[e][14] = 1
        for f in range(1, 7):
            maze_list[f][12] = 1
        for g in range(6, 12):
            maze_list[6][g] = 1
        for h in range(6, 11):
            maze_list[h][6] = 1
        for j in range(2, 7):
            maze_list[4][j] = 1
        for k in range(5, 11):
            maze_list[k][2] = 1
        for p in range(3, 6):
            maze_list[10][p] = 1
        for o in range(5, 9):
            maze_list[o][4] = 1
        for q in range(1, 10):
            maze_list[q][16] = 1
        maze_list[4][9] = 1
        maze_list[5][9] = 1
        maze_list[4][10] = 1
        maze_list[4][7] = 1

        return maze_list

    # define a draw function to draw the grid

    def draw(self, display_surf, image_surf):
        maze = self.grid()
        for i in range(self.m + 1):
            for j in range(self.n + 1):
                if maze[i][j] == 1:
                    display_surf.blit(image_surf, (j * 44, i * 44))

    def __str__(self):
        return self.grid()


class Paint:
    """
        define a Paint class to draw the way of movement
        from the entrance to the exit
    """

    windowWidth = 800
    windowHeight = 600
    pygame.display.set_caption("Maze")
    maze = Maze(12, 17)
    grid = maze.grid()

    def __init__(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((self.windowWidth,
                                                     self.windowHeight))
        self.image_surf = pygame.image.load("player-2.png").convert_alpha()
        self.block_surf = pygame.image.load("block-1.png").convert_alpha()

    # define a move function to draw the movement
    # move() takes two parameters i, j,
    # i, j stand for the position of the nested list

    def move(self, i, j):
        self.rect = self.image_surf.get_rect()
        self.rect.move_ip([j * 44, i * 44])
        pygame.time.delay(100)
        self.display_surf.fill((252, 184, 38))
        self.maze.draw(self.display_surf, self.block_surf)
        self.display_surf.blit(self.image_surf, self.rect)
        pygame.display.update()

    # define an on_loop function to find the way out
    # takes two element, i, j
    # i, j stand for the starting position of the maze
    # returns a boolean

    def on_loop(self, lst, i, j):
        if lst[11][17] == 2:
            return True
        else:
            if lst[i][j] == 0:
                lst[i][j] = 2
                if self.on_loop(lst, i + 1, j):
                    self.move(i, j)
                    return True
                elif self.on_loop(lst, i, j + 1):
                    self.move(i, j)
                    return True
                elif self.on_loop(lst, i - 1, j):
                    self.move(i, j)
                    return True
                elif self.on_loop(lst, i, j - 1):
                    self.move(i, j)
                    return True
                else:
                    lst[i][j] = 3
                    return False
            else:
                return False

    # define an on_execute function to execute all the functions in the class
    # on_execute() takes no parameters
    # it draws the gird and the movement

    def on_execute(self):
        self.display_surf.fill((252, 184, 38))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.maze.draw(self.display_surf, self.block_surf)
            self.display_surf.blit(self.image_surf, (11 * 44, 18 * 44))
            self.rect = self.image_surf.get_rect()
            self.on_loop(self.grid, 0, 1)
            pygame.display.update()

    def __str__(self):
        return self.display_surf


# define a main function to call all other functions

def main():
    paint = Paint()
    paint.on_execute()


if __name__ == "__main__":
    main()
