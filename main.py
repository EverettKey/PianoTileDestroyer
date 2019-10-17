import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, moveMouseTo
from directKeys import queryMousePosition
import time
import sys, signal

game_coords = [1140, 150, 1750, 770] #(left_x, top_y, right_x, bottom_y)
w = game_coords[2] - game_coords[0]
h = game_coords[3] - game_coords[1]
x_np_pos = np.arange(w/8, w, w/4).astype(np.int64)
x_positions = [int(x_np_pos[0]), int(x_np_pos[1]), int(x_np_pos[2]), int(x_np_pos[3])]
print(x_positions)
score = 0
previous_column = x_positions[0]

# screen = np.array(Image)
previous_column = -1

def clickOnBlack(screen, w, h, x_positions):
    global previous_column
    x0 = 1140
    y0 = 150
    for y in reversed(range(0, h, 5)):
        for x in x_positions:
            if x != previous_column:
                if screen[y][x] < 40:
                    actual_y = y0 + y
                    actual_x = x0 + x
                    click(actual_x, actual_y)
                    previous_column = x
                    print('clicked at {}, {}'.format(actual_x, actual_y))
                    return 1
    return 0

            
time.sleep(1)
while(True):
    cursor = queryMousePosition()
    
    
    if game_coords[0] < cursor.x < game_coords[2]:
        startTime = time.time()
        screen = np.array(ImageGrab.grab(bbox=game_coords))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        score += clickOnBlack(screen, w, h, x_positions)
        print("processing this frame took {} second".format(time.time()-startTime))
        
    else:
        print("score:{}".format(score))
        break