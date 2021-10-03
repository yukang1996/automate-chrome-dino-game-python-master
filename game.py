import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# initialize variable
land = 0
dino_position_down_left = 0
cactus_y = 0
ptero_y = 0
obstacle_detection_start = 0
obstacle_detection_end = 0


def locater():
    # find dino icon
    dino_img = './dino icon.png'
    dino_img = Image.open(dino_img)
    # dino_img.show()
    screenshot = ImageGrab.grab().convert('L')
    # screenshot.show()
    # find position of dino_img in screenshot
    position_x, position_y = pyautogui.locateCenterOnScreen(dino_img)
    print('x: {}, y: {}'.format(position_x,position_y))
    # pyautogui.moveTo(position_x, position_y)
    # time.sleep(5)
    global land
    global sky
    global dino_position_down_left
    global cactus_y
    global ptero_y
    global obstacle_detection_end
    global obstacle_detection_start 
    land= position_y 
    sky = position_y - 70
    dino_position_down_left = position_x - 30, position_y+30
    cactus_y = position_y - 35
    ptero_y = position_y - 40
    obstacle_detection_start = position_x + 100
    obstacle_detection_end = position_x +170

def click(key):
    pyautogui.keyDown(key)
    print('click ', key)
    return

def isCollision(data):
# Check colison for birds
    for i in range(obstacle_detection_start,obstacle_detection_end):
        for j in range(sky, ptero_y):
            if data[i, j] < 171:
                click("down")
                return
 # Check colison for cactus
    for i in range(obstacle_detection_start,obstacle_detection_end):
        for j in range(cactus_y, land):
            if data[i, j] < 100:
                print(i,j)
                click("up")
                return
    return

if __name__ == "__main__":
    
    locater()

    time.sleep(5)
    click('up') 

    
    while True:

        image = ImageGrab.grab().convert('L')
        print(image)
        data = image.load()
        # pass the image to genetic algorithm
        # get result(1-jump,0-stay,-1-duck)
        isCollision(data)
        
        # Draw the rectangle for cactus
        # x
        # for i in range(obstacle_detection_start,obstacle_detection_end):
        #     # y
        #     for j in range(cactus_y, land):
        #     #     print(i,j)
        #         data[i,j] = 0      
        
        # # Draw the rectangle for birds
        # for i in range(obstacle_detection_start, obstacle_detection_end):
        #     for j in range(sky, ptero_y):
        #         data[i, j] = 171

        # image.show()
        # break
      

