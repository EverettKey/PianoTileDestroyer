import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click
import time

gameCoords = []

screen = np.array(Image)

for i in range(1000):
    startTime = time.time()
    print(queryMousePosition())
    