import pygame

pygame.init()

SCR_WIDTH = 500
SCR_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption("SNAKE AI")

CLOCK = pygame.time.Clock()

CELL_LEN = 25
CELL_X_MAX = SCR_WIDTH // CELL_LEN
CELL_Y_MAX = SCR_HEIGHT // CELL_LEN


class Snake:
    def __init__(self, pos, color):
        self.color = color
        self.dir = (1, 0)
        self.grow_flag = False
        self.body = [pos, (pos[0]-1, pos[1]), (pos[0]-2, pos[1]), (pos[0]-3, pos[1])]

    def set_dir(self, dir):
        self.dir = dir

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.dir[0], head_y + self.dir[1])
        self.body.insert(0, new_head)
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False
        return new_head

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(SCREEN, self.color, pygame.Rect(x * CELL_LEN, y * CELL_LEN, CELL_LEN, CELL_LEN))

    def check_collision_with_walls(self, x, y):
        if x < 0 or y < 0 or x >= CELL_X_MAX or y >= CELL_Y_MAX:
            return True
        return False

    
    def check_collision_with_self(self, x, y):
        return (x, y) in self.body[1:]
    

class Food:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def draw(self):
        x, y = self.pos
        pygame.draw.rect(SCREEN, self.color, pygame.Rect(x * CELL_LEN, y * CELL_LEN, CELL_LEN, CELL_LEN))