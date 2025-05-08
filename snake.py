import pygame
import random
import sys

# Oyun penceresi boyutu
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Renkler
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)

# Yönler
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def draw_segment(screen, x, y, is_head=False):
    color = DARK_GREEN if is_head else GREEN
    pygame.draw.circle(screen, color, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 2)

def draw_food(screen, x, y):
    pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))

def random_food():
    return (
        random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
        random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
    )

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Solucan Oyunu (Snake - Nokia 3310 Style)")
    clock = pygame.time.Clock()

    # Başlangıç durumu
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = RIGHT
    food = random_food()

    while True:
        screen.fill(BLACK)

        # Olaylar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        # Yılanın başı
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0] * CELL_SIZE, head_y + direction[1] * CELL_SIZE)

        # Duvara veya kendine çarpma kontrolü
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake
        ):
            print("Oyun Bitti!")
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)

        # Yem yedi mi?
        if new_head == food:
            food = random_food()
        else:
            snake.pop()

        # Çizim
        for i, segment in enumerate(snake):
            draw_segment(screen, segment[0], segment[1], is_head=(i == 0))

        draw_food(screen, food[0], food[1])
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
