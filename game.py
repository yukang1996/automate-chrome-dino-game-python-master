import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

x_cac = 227,300
y_cac = 296,437

def click(key):
    pyautogui.keyDown(key)
    print('click ', key)
    return

def isCollision(data):
# Check colison for birds
    # for i in range(x_cac):
    #     for j in range(y_cac):
    #         if data[i, j] < 171:
    #             click("down")
    #             return
 # Check colison for cactus
    for i in range(227,300):
        for j in range(296,437):
            if data[i, j] < 100:
                click("up")
                return
    return

def displayImage(image):
    mngr = plt.get_current_fig_manager()
    # to put it into the upper left corner for example:
    mngr.window.setGeometry = (1600,1800,928, 1228)
    imgplot = plt.imshow(image)
    plt.ion()
    plt.show()
    plt.close()

if __name__ == "__main__":
    time.sleep(5)
    click('up') 
    
    while True:

        image = ImageGrab.grab().convert('L')
        # pil_image = Image.open(image)
        print(image)
        # displayImage(image)
        data = image.load()
        isCollision(data)
        
        # Draw the rectangle for cactus
        # x
        # for i in range(227,300):
        #     # y
        #     for j in range(296, 437):
        #          data[i, j] = 0
        
        # # Draw the rectangle for birds
        # for i in range(530, 560):
        #     for j in range(174, 550):
        #         data[i, j] = 171

        # image.show()
        # break
      

