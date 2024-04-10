import pygame
import random, time
import sys

pygame.init()


SIZE_BLOCK = 20
FRAME_COLOR = (0,255,202)
WHITE= (255,255,255)
BLUE = (180,255,255)
RED = (224,0,0)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 104 , 0)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1 
size = [SIZE_BLOCK*COUNT_BLOCKS + 2*SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * SIZE_BLOCK + HEADER_MARGIN]
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Жылан")
timer = pygame.time.Clock()
courier = pygame.font.SysFont("courier",36)

class SnakeBlock:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def is_insite(self):
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK

    def __eq__(self,other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

def get_random_empty_block():
    x = random.randint(0,COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS -1)
    empty_block = SnakeBlock(x,y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0,COUNT_BLOCKS - 1)
        empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
    return empty_block

def draw_block(color,row,column):
    pygame.draw.rect(screen,color,(SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                           HEADER_MARGIN + row * SIZE_BLOCK + MARGIN * (row + 1),
                                           SIZE_BLOCK,
                                           SIZE_BLOCK))


def restart_game():
    global snake_blocks, apple, d_row, d_col, total, speed
    snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = get_random_empty_block()
    d_row = 0
    d_col = 1
    total = 0
    speed = 1

snake_blocks = [SnakeBlock(9,8),SnakeBlock(9,9),SnakeBlock(9,10)]
apple = get_random_empty_block()
d_row = 0
d_col  = 1
total = 0
speed = 1

done = False



while not done:

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            head = snake_blocks[-1]
            for block in snake_blocks[:-1]:
                if head.x == block.x and head.y == block.y:
                    screen.fill(FRAME_COLOR)
                    game_over_text = courier.render("Game Over", True, WHITE)
                    screen.blit(game_over_text, (size[0] / 2 - game_over_text.get_width() / 2, size[1] / 2 - game_over_text.get_height() / 2))
                    pygame.display.flip()
                    waiting_for_restart = True
                    while waiting_for_restart:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                waiting_for_restart = False
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    waiting_for_restart = False
                                    restart_game()
                    break
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1 
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, (0,0, size[0], HEADER_MARGIN))
    
    text_total = courier.render (f"total: {total}", 0 , WHITE)
    text_speed = courier.render (f"speed: {speed}", 0 , WHITE)
    screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            draw_block(color,row,column)


    head = snake_blocks[-1]
    if not head.is_insite():
        screen.fill(FRAME_COLOR)
        game_over_text = courier.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (size[0] / 2 - game_over_text.get_width() / 2, size[1] / 2 - game_over_text.get_height() / 2))
        pygame.display.flip()
        waiting_for_restart = True
        while waiting_for_restart:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     waiting_for_restart = False
                     pygame.quit()
                     sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting_for_restart = False
                        restart_game()
        continue
    draw_block(RED,apple.x,apple.y)
    for block in snake_blocks:
        draw_block(SNAKE_COLOR,block.x,block.y)
    
    if apple == head:
        total += 1
        if total % 5 == 0:
            speed += 1
        snake_blocks.append(apple)
        apple = get_random_empty_block()

    new_head = SnakeBlock(head.x + d_row, head.y + d_col )
    snake_blocks.append(new_head)
    snake_blocks.pop(0)
      
    pygame.display.flip()
    timer.tick(5 + speed)
