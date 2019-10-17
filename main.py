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


def clickOnBlack(screen):
    global gameCoords, score, w, h, x_positions, previous_column
    for y in reversed(range(h)):
        for x in x_positions:
            if x != previous_column:
                if screen[y][x] < 40:
                    actual_y = int(game_coords[1] + y)
                    actual_x = int(game_coords[0] + x)
                    click(actual_x, actual_y)
                    previous_column = x
                    print('clicked at {}, {}'.format(actual_x, actual_y))
                    return

            
time.sleep(1)
while(True):
    cursor = queryMousePosition()
    
    if game_coords[0] < cursor.x < game_coords[2]:
        screen = np.array(ImageGrab.grab(bbox=game_coords))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        clickOnBlack(screen)
        
    else:
        break