import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand Gesture Snake Game")

clock = pygame.time.Clock()
BLOCK = 20  # size of snake segment and food


class Snake:
    def __init__(self):
        self.body = [(300, 300)]   # initial head
        self.length = 1
        self.speed = 6             # smooth movement

    def move_to(self, target_x, target_y):
        head_x, head_y = self.body[0]

        dx = target_x - head_x
        dy = target_y - head_y
        dist = max((dx ** 2 + dy ** 2) ** 0.5, 1)

        new_x = head_x + (dx / dist) * self.speed
        new_y = head_y + (dy / dist) * self.speed

        # Keep snake inside window
        new_x = max(0, min(new_x, WIDTH - BLOCK))
        new_y = max(0, min(new_y, HEIGHT - BLOCK))

        self.body.insert(0, (new_x, new_y))

        if len(self.body) > self.length:
            self.body.pop()

    def grow(self):
        self.length += 1

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (int(segment[0]), int(segment[1]), BLOCK, BLOCK)
            )


class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (WIDTH - BLOCK) // BLOCK) * BLOCK
        y = random.randint(0, (HEIGHT - BLOCK) // BLOCK) * BLOCK
        return (x, y)

    def draw(self):
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (*self.position, BLOCK, BLOCK)
        )


def check_collision(snake, food):
    head_x, head_y = snake.body[0]

    head_x = round(head_x / BLOCK) * BLOCK
    head_y = round(head_y / BLOCK) * BLOCK

    return (head_x, head_y) == food.position
