from tkinter import *
from tkinter import messagebox
import random
import time



game_width = 500  # Переменные для работы с полем
game_height = 500
snake_item = 10
game_x = game_width // snake_item
game_y = game_height // snake_item
Game = True
point = 0

game = Tk()  # Переменные для работы с приложением
game.title("Игра змейка")
game.resizable(0, 0)
game.wm_attributes("-topmost", 1)

snakeColor1 = "red"  # Переменные для работы со змейкой
snakeColor2 = "yellow"
snake_x = game_x // 2
snake_y = game_y // 2
snake_x_navigation = 0
snake_y_navigation = 0
snake_list = []
snake_size = 3

presents = []  # Переменные для работы с печеньками#
presents_size = 5
presentsColor1 = "blue"
presentsColor2 = "white"

canvas = Canvas(game, width=game_width, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
game.update


# for i in range(presents_size): #Рисуем печеньки
#   x = random.randrange(game_x)
#    y = random.randrange(game_y)  # добавить проверки на уникальность
#   id0 = canvas.create_oval(x * snake_item, y * snake_item, x * snake_item + snake_item,
#                            y * snake_item + snake_item,
#                            fill=presentsColor2)
#   id1 = canvas.create_oval(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
#                            y * snake_item + snake_item - 2, fill=presentsColor1)
#   presents.append([x, y, id0, id1])
def checl_len():
    if len(presents) > 1:
        presents.pop(0)


def cookies():
    x = random.randrange(game_x)
    y = random.randrange(game_y)  # добавить проверки на уникальность
    id0 = canvas.create_oval(x * snake_item, y * snake_item, x * snake_item + snake_item,
                             y * snake_item + snake_item,
                             fill=presentsColor2)
    id1 = canvas.create_oval(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                             y * snake_item + snake_item - 2, fill=presentsColor1)
    presents.append([x, y, id0, id1])
    checl_len()


def snake_ipait_items(canvas, x, y):  # Рисуем змейку
    global snake_list
    id0 = canvas.create_rectangle(x * snake_item, y * snake_item, x * snake_item + snake_item,
                                  y * snake_item + snake_item,
                                  fill=snakeColor2)
    id1 = canvas.create_rectangle(x * snake_item + 2, y * snake_item + 2, x * snake_item + snake_item - 2,
                                  y * snake_item + snake_item - 2, fill=snakeColor1)
    snake_list.append([x, y, id0, id1])


snake_ipait_items(canvas, snake_x, snake_y)
cookies()


def check_delete():  # Удаляем след змейки
    if len(snake_list) >= snake_size:
        temp = snake_list.pop(0)
        canvas.delete(temp[2])
        canvas.delete(temp[3])


def checl_presents():  # Если съесть печеньку
    global snake_size
    global point
    for i in range(len(presents)):
        if presents[i][0] == snake_x and presents[i][1] == snake_y:
            snake_size += 1
            canvas.delete(presents[i][2])
            canvas.delete(presents[i][3])
            point += 1
            cookies()

    # [snake_x, snake_y]


def snake_move(event):  # Фунцкия отвечающая за управление
    global snake_x, snake_y_navigation, snake_x_navigation
    global snake_y
    if event.keysym == "Up":
        snake_x_navigation = 0
        snake_y_navigation = -1
        check_delete()
    if event.keysym == "Down":
        snake_x_navigation = 0
        snake_y_navigation = 1
        check_delete()
    if event.keysym == "Left":
        snake_x_navigation = -1
        snake_y_navigation = 0
        check_delete()
    if event.keysym == "Right":
        snake_x_navigation = 1
        snake_y_navigation = 0
        check_delete()
    snake_y = snake_y + snake_y_navigation
    snake_x = snake_x + snake_x_navigation
    snake_ipait_items(canvas, snake_x, snake_y)
    checl_presents()


def touch_youself(future_x, future_y):  # Если мы коснемся себя
    global Game
    if not (snake_x_navigation == 0 and snake_y_navigation == 0):
        for i in range(len(snake_list)):
            if snake_list[i][0] == future_x and snake_list[i][1] == future_y:
                game_over()


def game_over():  # Функция выхода из игры
    global Game
    Game = False
    messagebox.showinfo("", "Увы, Вы проиграли :( \n Ваш счет: %s" % point)
    # exit(1)
    # Вывести текст на экран


def overdisplay():  # функция отвечающая за выход за пределы экрана
    if snake_y >= game_y or snake_x >= game_x or snake_x < 0 or snake_y < 0:
        game_over()


canvas.bind_all("<Left>", snake_move)
canvas.bind_all("<Right>", snake_move)
canvas.bind_all("<Down>", snake_move)
canvas.bind_all("<Up>", snake_move)

while Game:  # Автоматическое движение
    check_delete()
    checl_presents()
    overdisplay()
    touch_youself(snake_x + snake_x_navigation, snake_y + snake_y_navigation)
    snake_y = snake_y + snake_y_navigation
    snake_x = snake_x + snake_x_navigation
    snake_ipait_items(canvas, snake_x, snake_y)
    game.update_idletasks()
    game.update()
    time.sleep(0.15)


def stop():  # функция служащая для того, чтобы пользователь не мог нажимать кнопки после поражения
    pass


canvas.bind_all("<Left>", stop)
canvas.bind_all("<Right>", stop)
canvas.bind_all("<Down>", stop)
canvas.bind_all("<Up>", stop)
game.mainloop()
