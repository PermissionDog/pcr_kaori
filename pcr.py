import cv2
import pyautogui
import numpy
import time
import math

def show(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
green = [49, 97, 90]
blue = [165, 77, 66]
red = [57, 48, 123]
fever = [57, 81, 255]

def distance(c1, c2):
    t = 0.0
    for i in range(3):
        t += (c1[i] - c2[i]) ** 2
    return math.sqrt(t)

def clicks(color) -> int:
    if distance(color, green) < 10:
        return 1
    if distance(color, blue) < 10:
        return 2
    if distance(color, red) < 10:
        return 3
    return 0

#l3 l2 l1 l0 r0 r1 r2 r3
pos = [
    [[502, 476], [502, 748]],
    [[502, 326], [502, 893]],
    [[502, 182], [502, 1034]],
    [[502, 38], [502, 1180]]
]
print("3秒后运行")
time.sleep(3)
while True:
    image = pyautogui.screenshot()
    image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    image = image[780:1540, 1280:2495]
    # fever条的最后一格
    f = image[631, 726]
    if distance(f, fever) < 150:
        print("fever")
        pyautogui.press("A", 120, 0.05)
        time.sleep(0.82)
        continue
    for p in pos:
        left = image[p[0][0], p[0][1]]
        right = image[p[1][0], p[1][1]]
        lc = clicks(left)
        rc = clicks(right)
        if lc != 0:
            pyautogui.press("A", lc, 0.05)
            print(f"left {lc}")
        if rc != 0:
            pyautogui.press("D", rc, 0.05)
            print(f"right {rc}")
    time.sleep(0.54)