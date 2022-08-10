import mouse
import keyboard
import time

pressed = False
mouseRecordedData = []
key = None
keyState = None

def recordMouseInput():
    global pressed
    pressed = mouse.is_pressed()
    mouseRecordedData.append(mouse.get_position())
    keyboardInput() # call the keyboard input function to get the next key

def playMouseInput():
    global mouseRecordedData
    for x in mouseRecordedData:
        mouse.move(x[0], x[1])
        print(x[0], x[1])
    mouseRecordedData = [] # reset the list
    print('Finished Replay')

def keyboardInput():
    global key
    key = keyboard.read_key()
    #print(key)

    if(key == 'q'):
        print('Quitting')
        exit()
    elif(key == 'r'):
        print('Recording')
        recordMouseInput()
    elif(key == 'm'):
        print('Replaying')
        playMouseInput()



while(True):
    recordMouseInput()
    keyboardInput()

    


