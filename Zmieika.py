import pygame
import time
import random

pygame.init()
white = (255, 255, 255)

# Определение цветов
black = (0, 0, 0)
red = (213, 50, 80)
blue = (0, 0, 255)

# Определение размеров окна
dis_width = 800
dis_height = 600

# Создание окна
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

# Определение размеров блока змейки и скорости змейки
snake_block = 10
snake_speed = 5

# Определение шрифта для отображения счёта
font_style = pygame.font.SysFont("Arial", 25)

# Функция для отображения текущего счёта
def your_score(score):
   value = font_style.render("Ваш счёт: " + str(score), True, white)
   dis.blit(value, [0, 0])

# Функция для рисования змейки
def snake(snake_block, snake_list):
   for x in snake_list:
       pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

# Функция для вывода сообщения на экран
def mess(msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Основной игровой цикл
def game_loop():
   game_over = False
   game_close = False
   x1 = dis_width / 2
   y1 = dis_height / 2
   x1_change = 0
   y1_change = 0
   snake_List = []
   Length_of_snake = 1
   foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
   foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

  # Основной цикл игры
   while not game_over:

      # Цикл для обработки событий в случае завершения игры
       while game_close == True:
           dis.fill(black)
           mess("Вы проиграли! Нажмите Q для выхода или C для повторной игры", white)
           your_score(Length_of_snake - 1)
           pygame.display.update()

         # Обработка событий для нажатия клавиш
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                       game_over = True
                       game_close = False
                   if event.key == pygame.K_c:
                     game_loop()

     # Обработка событий для выхода из игры
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game_over = True
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   x1_change = -snake_block
                   y1_change = 0
               elif event.key == pygame.K_RIGHT:
                   x1_change = snake_block
                   y1_change = 0
               elif event.key == pygame.K_UP:
                   y1_change = -snake_block
                   x1_change = 0
               elif event.key == pygame.K_DOWN:
                   y1_change = snake_block
                   x1_change = 0

      # Проверка на выход за границы экрана
       if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           game_close = True

      # Изменение координат змейки
       x1 += x1_change
       y1 += y1_change

     # Очистка экрана
       dis.fill(black)

      # Рисование еды
       pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

     # Обновление списка координат змейки
       snake_Head = []
       snake_Head.append(x1)
       snake_Head.append(y1)
       snake_List.append(snake_Head)

     # Удаление лишних координат змейки
       if len(snake_List) > Length_of_snake:
           del snake_List[0]

      # Проверка на столкновение с собственным хвостом
       for x in snake_List[:-1]:
           if x == snake_Head:
               game_close = True

     # Рисование змейки
       snake(snake_block, snake_List)

      # Отображение текущего счёта
       your_score(Length_of_snake - 1)
       pygame.display.update()

     # Проверка на съедание еды
       if x1 == foodx and y1 == foody:
           foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
           Length_of_snake += 1

        # Установка скорости змейки
       clock.tick(snake_speed)
   pygame.quit()
   quit()

# Запуск игрового цикла
game_loop()