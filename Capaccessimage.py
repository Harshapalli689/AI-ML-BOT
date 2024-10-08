import os
import cv2
import time
import pyautogui
camera=cv2.VideoCapture(0)
current_frame_count=0
total_time=10
start_time=time.time()
while(int(time.time()-start_time)<total_time):
    name=input("Enter name :")
    ret,frame=camera.read()
    cv2.imshow("frame",frame)
    if ret:
        name='C:/Users/harsh/OneDrive/Desktop/Major Project BoT/Face_Samples_Dataset/1/'+str(name)+str(current_frame_count)+'.jpg'
        print(name)
        cv2.imwrite(name,frame)
        current_frame_count+=1
    else:
        break
    time.sleep(2)
    pyautogui.press('k')
camera.release()
cv2.destroyAllWindows()

