from snake import *
from neural_network import forward_propagation
import random
import numpy as np


R = (1, 0)
L = (-1, 0)
D = (0, 1)
U = (0, -1)

def getRandomPos():
    return random.randint(0, CELL_X_MAX-1), random.randint(0, CELL_Y_MAX-1)

def check_direction(snake:Snake, food:Food, dir):
    self_collide = 0
    food_collide = 0
    distance_from_wall = 0
    head_x, head_y = snake.body[0]

    while not snake.check_collision_with_walls(head_x, head_y):
        if not self_collide and snake.check_collision_with_self(head_x, head_y):
            self_collide = 1
        if not food_collide and head_x == food.pos[0] and head_y == food.pos[1]:
            food_collide = 1
        distance_from_wall += 1
        head_x += dir[0]
        head_y += dir[1]

    return self_collide, food_collide, 1/distance_from_wall

def get_input(snake, food):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    inputs = []

    for dir in directions:
        self_collide, food_collide, norm_distance_from_wall = check_direction(snake, food, dir)
        inputs.extend([self_collide, food_collide, norm_distance_from_wall])

    return np.array(inputs)

def turn_left(dir):
    return {R:U, U:L, L:D, D:R}[dir]

def turn_right(dir):
    return {R:D, D:L, L:U, U:R}[dir]

def convert_to_dir(dir, index):
    if index == 0:
        return turn_left(dir)
    elif index == 1:
        return dir
    else:
        return turn_right(dir)

def simulate(individual):
    random.seed(0)
    snake = Snake((6, 5), (0, 0, 255))
    food = Food(getRandomPos(), (255, 0, 0))

    score = 0
    fitness = 0
    max_steps = 500
    steps = 0
    running = True
    steps_without_food = 0

    while running and steps < max_steps:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        input = get_input(snake, food)
        output = forward_propagation(input, individual)
        max_prob_ind = np.argmax(output)
        pred_dir = convert_to_dir(snake.dir, max_prob_ind)
        snake.set_dir(pred_dir)

        if snake.check_collision_with_self(snake.body[0][0] + snake.dir[0], snake.body[0][1] + snake.dir[1]):
            break

        snake.move()
        steps += 1

        head_x, head_y = snake.body[0]

        if snake.check_collision_with_walls(head_x, head_y):
            break

        if head_x == food.pos[0] and head_y == food.pos[1]:
            score += 1
            food = Food(getRandomPos(), (255, 0, 0))
            snake.grow_flag = True
            steps_without_food = 0
            max_steps += 200
        else:
            steps_without_food += 1
        
        if steps_without_food > 300:
            break
        
            
    if score < 10:
        fitness = steps * steps * pow(4, score)
    else:
        fitness = steps * steps * pow(4, 10) * (score - 9)
    
    return fitness, score


def visualize(individual):
    random.seed(0)
    snake = Snake((6, 5), (0, 0, 255))
    food = Food(getRandomPos(), (255, 0, 0))

    score = 0
    max_steps = 500
    steps = 0
    running = True
    steps_without_food = 0

    while running and steps < max_steps:
        CLOCK.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        input = get_input(snake, food)
        output = forward_propagation(input, individual)
        max_prob_ind = np.argmax(output)
        pred_dir = convert_to_dir(snake.dir, max_prob_ind)
        snake.set_dir(pred_dir)

        if snake.check_collision_with_self(snake.body[0][0] + snake.dir[0], snake.body[0][1] + snake.dir[1]):
            break
        snake.move()
        steps += 1

        head_x, head_y = snake.body[0]

        if snake.check_collision_with_walls(head_x, head_y):
            break

        if head_x == food.pos[0] and head_y == food.pos[1]:
            score += 1
            max_steps += 200
            food = Food(getRandomPos(), (255, 0, 0))
            snake.grow_flag = True
            steps_without_food = 0
        else:
            steps_without_food += 1

        if steps_without_food > 300:
            break
        
        SCREEN.fill((0, 0, 0))
        snake.draw()
        food.draw()
        pygame.display.flip()
    print(f"Final score : {score}")
