from util import *
from config import *

#显示当前游戏画面 并显示判定点
def show_game(draw_points=True):
    img = game()
    if draw_points:
        #画出蛇的判定点
        for i in sum(snake_pos, []):
            print(i)
            draw_point(img, i)

        #画出fever判定点
        draw_point(img, fever_pos)
    show(img)

#保存游戏画面
def save_game():
    save_img(game())

def save_screenshot():
    save_img(screen())

# show_game()
# save_game()
# print(is_end(game()))
# img = game()
# t = range_check(img, snake_pos[0][0], blue_color, 5)
# t = clicks(img, snake_pos[0][0])
# print(t)
save_screenshot()