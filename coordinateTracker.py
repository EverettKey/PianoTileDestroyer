from directKeys import queryMousePosition
import time

while True:
    cursor = queryMousePosition()
    print('cursor at {}, {}'.format(cursor.x, cursor.y))
    time.sleep(0.2)