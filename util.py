import time
import cv2
import math
import numpy
import pyautogui
import config
import os

# 展示图片
def show(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)

# 保存图片
os.makedirs("log", exist_ok=True)
def save_img(img):
    cv2.imwrite(f"log/{time.time_ns()//1000}.jpg", img)

def distance(c1, c2):
    t = 0.0
    for i in range(3):
        t += (c1[i] - c2[i]) ** 2
    return math.sqrt(t)

# 判断蛇的类型
def clicks(img, pos):
    if range_check(img, pos, config.green_color):
        return 1
    if range_check(img, pos, config.blue_color):
        return 2
    if range_check(img, pos, config.red_color):
        return 3
    return 0

# 判断pos为中心的矩形 颜色是否相似
def range_check(img, pos, color, radius=6, threshold=0.1):
    y, x = pos
    total = (radius * 2 + 1) ** 2
    count = 0
    for i in range(y - radius, y + radius + 1):
        for j in range(x - radius, x + radius + 1):
            if distance(color, img[i, j]) < 40:
                count += 1
    return count / total >= threshold
    
    

# 在图上打点(y,x)
def draw_point(img, pos):
    cv2.circle(img, pos[::-1], 6, (0,0,255), -1)

# 在图上写字(y,x)
def draw_text(img, pos, text):
    cv2.putText(
        img, str(text), pos[::-1],
        cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
        1.5, (0,0,255)
        )

# 判断是否是 fever 状态
def is_fever(img):
    y, x = config.fever_pos
    return distance(img[y, x], config.fever_color) < 150

# 判断游戏是否结束(没用 因为游戏会出错(手动滑稽))
def is_end(img):
    y, x = config.end_pos
    return distance(img[y, x], config.end_color) < 10

# 截图屏幕
def screen():
    return cv2.cvtColor(
        numpy.array(pyautogui.screenshot()), 
        cv2.COLOR_RGB2BGR)

# 截图屏幕并裁剪出游戏区域
def game():
    p1, p2 = config.game_pos
    return screen()[p1[0]:p2[0], p1[1]:p2[1]]

# 点击屏幕
pyautogui.PAUSE = 0.0095
def click(pos, count, interval):
    for i in range(count):
        
        pyautogui.mouseDown(*pos[::-1])
        pyautogui.mouseUp()
        time.sleep(interval)
