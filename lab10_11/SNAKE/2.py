#импорт библиотек
import pygame
import random,time
import sys
import pygame_menu
#инициализация
pygame.init()

#параметры
bg_image = pygame.image.load("snake3.png")
SIZE_BLOCK = 20
FRAME_COLOR = (0,255,202)
WHITE= (255,255,255)
BLUE = (180,255,255)
BLUE_APPLE = (0,0,255)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 104 , 0)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1 
size = [SIZE_BLOCK*COUNT_BLOCKS + 2*SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * SIZE_BLOCK + HEADER_MARGIN]
print(size)

#экран , загаловок , шрифт

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Жылан")
timer = pygame.time.Clock()
courier = pygame.font.SysFont("courier",36)

#клас и функции для определения и создание блоков в игре змейка
class SnakeBlock:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def is_insite(self):
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK
    
    def __eq__(self,other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


#поле игры
def draw_block(color,row,column):
    pygame.draw.rect(screen,color,(SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                           HEADER_MARGIN + row * SIZE_BLOCK + MARGIN * (row + 1),
                                           SIZE_BLOCK,
                                           SIZE_BLOCK))



def start_the_game():

    #генератор рандомных  блоков
    def get_random_empty_block():
        x = random.randint(0,COUNT_BLOCKS - 1)
        y = random.randint(0, COUNT_BLOCKS -1)
        empty_block = SnakeBlock(x,y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0,COUNT_BLOCKS - 1)
            empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
        return empty_block
    
        #рестарт игры

    snake_blocks = [SnakeBlock(9,8),SnakeBlock(9,9),SnakeBlock(9,10)]
    apple = get_random_empty_block()
    d_row = buf_row = 0
    d_col  = buf_col = 1
    total = 0
    speed = 1

    done = False



    #главный цикл
    while not done:
        #чтобы выйти
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN and buf_col != 0:
                    buf_row = 1 
                    buf_col = 0
                elif event.key == pygame.K_LEFT and buf_row != 0:
                    buf_row = 0
                    buf_col = -1
                elif event.key == pygame.K_RIGHT and buf_row != 0:
                    buf_row = 0
                    buf_col = 1

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, (0,0, size[0], HEADER_MARGIN))
        #счетчик очков и скорости
        text_total = courier.render (f"total: {total}", 0 , WHITE)
        text_speed = courier.render (f"speed: {speed}", 0 , WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))
        #рисование игрового поля
        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (row + column) % 2 == 0:
                    color = BLUE
                else:
                    color = WHITE
                draw_block(color,row,column)

        #проверяет границы 
        head = snake_blocks[-1]
        if not head.is_insite():
            print('crash')
            break

        draw_block(BLUE_APPLE,apple.x,apple.y)
        for block in snake_blocks:
            draw_block(SNAKE_COLOR,block.x,block.y)

        pygame.display.flip
        
        if apple == head:
            total += 1
            if total % 5 == 0:
                speed += 2
            snake_blocks.append(apple)
            apple = get_random_empty_block()

        
        d_row = buf_row
        d_col = buf_col
        new_head = SnakeBlock(head.x + d_row, head.y + d_col )
        
        if new_head in snake_blocks:
            print('crash yourself')
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        
        pygame.display.flip()
        timer.tick(5 + speed)


main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.2)
menu = pygame_menu.Menu('', 400, 300,
                       theme=main_theme)

menu.add.text_input('Name :', default='John Doe')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:

    screen.blit(bg_image,(0,0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()