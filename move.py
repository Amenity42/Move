from random import random
from turtle import down
from typing import Any
import mouse
import time

# Move the mouse to the center of the screen   
# loop forever

# i=0
# move_x = 200
# move_y = 200
# while i <= 1:
#     mouse.move(move_x, move_y)
#     time.sleep(0.2)
#     mouse.move(move_x, move_y) 
#     time.sleep(0.2)
#     mouse.move(move_x, move_y) 
#     #randomly move the mouse to a new location
#     move_x = 200 + random() * 100
#     move_y = 200 + random() * 100 
#     if(mouse.is_pressed()):
#         i=1
    

pressed = False
mouseRecordedData = []

def recordMouseInput():
    global pressed
    pressed = mouse.is_pressed()

    global mouseRecordedData
    if(pressed):
        for x in mouseRecordedData:
            mouse.move(x[0], x[1])
            print(x[0], x[1])
        print('Finished Replay')
    else:
        # pressed = False
        mouseRecordedData.append(mouse.get_position())
        print('The mouse is not pressed - Recording')


while(True):
    recordMouseInput()

    


