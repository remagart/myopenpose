# 測試畫框 和裁切
#%%
import cv2
import matplotlib.pyplot as plt
import sys
sys.path.append("/Users/richard/myworkspace/mygitlab/myopenpose/2_drawSquare/")
from drawSquareFun import handleDraw
sys.path.append("/Users/richard/myworkspace/mygitlab/myopenpose/1_crop/")
from rotateFuntion import cropByRotate

# %%

url = "/Users/richard/myworkspace/mygitlab/myopenpose/1_crop/baconfireRB.mp4"
cap = cv2.VideoCapture(url) 

for i in range(1):
    ret, frame = cap.read()
    if not ret:
        break
    
    frame2 = frame
    
    handleDraw(200,226,300,150)
    
    p1 = {
        "x": 200,
        "y": 226
    }
    p2 = {
        "x": 300,
        "y": 150
    }
    p3 = {
        "x":182,
        "y":202
    }
    p4 = {
        "x": 218,
        "y": 250
    }
    
    frame2 = cropByRotate(frame2,p1,p2,p3,p4)
    
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    
    plt.imshow(frame)   
    plt.show()
    
    plt.imshow(frame2)   
    plt.show()


# %%
