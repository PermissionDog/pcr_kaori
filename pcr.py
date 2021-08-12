import cv2
import pyautogui
import numpy
import time
from util import *
from config import *

print("3秒后运行")
time.sleep(3)
while True:
    img = game()
    if is_end(img):
        print("游戏结束")
        exit(0)

    if is_fever(img):
        print("fever")
        click(click_left_pos, 210, 0.005)
        time.sleep(0.9)
        continue
    
    move = []
    for p in snake_pos:
        lp, rp = p
        lc, rc = clicks(img, lp), clicks(img, rp)
        if lc != 0 and rc != 0:
            print("识别错误: 左右同时检测到蛇")
            draw_point(img, lp)
            draw_text(img, lp, lc)
            draw_point(img, rp)
            draw_text(img, rp, rc)
            show(img)
        
        if lc == 0 and rc == 0:
            move = []
            break

        if lc != 0:
            move.append([lc, 0])
            draw_point(img, lp)
            draw_text(img, lp, lc)
        elif rc != 0:
            move.append([0, rc])
            draw_point(img, rp)
            draw_text(img, rp, rc)
    
    # 过滤掉不足 4 个蛇的识别
    if len(move) == 0:
        time.sleep(0.001)
        # print("!!")
        continue

    for m in move:
        lc, rc = m
        if lc != 0:
            click(click_left_pos, lc, 0.022)
            print(f"left {lc}")
        if rc != 0:
            click(click_right_pos, rc, 0.022)
            print(f"right {rc}")
    
    # 保存点击后图片
    # save_img(game())
    
    time.sleep(0.035)
    
    # 保存本次识别结果
    # save_img(img)
        