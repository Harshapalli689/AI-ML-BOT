from cv2 import VideoCapture,imshow,imwrite,waitKey,destroyWindow
from cv2 import *
import pyautogui
import time
import pywhatkit

def send_image():
    image="unauthorized.png"
    Caption="UnAuthorized Person Trying to Access your PC BoT"
    pywhatkit.sendwhats_image("+919121350688","unauthorized.png",Caption)
    print("image Sent Successfully")

def unauthorized():
    # initialize the camerak
    # If you have multiple camera connected with 
    # current device, assign a value in cam_port 
    # variable according to that
    cam_port =0
    cam = VideoCapture(cam_port)
    
    # reading the input using the camera
    result, image = cam.read()
    
    # If image will detected without any error, 
    # show result
    if result:
    
        # showing result, it take frame name and image 
        # output
        imshow("UnAuthorized Person Image", image)
        # saving image in local storage
        imwrite("unauthorized.png", image)
        time.sleep(2)
        # If keyboard interrupt occurs, destroy image 
        # window
        pyautogui.press('k')
        destroyWindow("UnAuthorized Person Image")
        send_image()
    
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")
