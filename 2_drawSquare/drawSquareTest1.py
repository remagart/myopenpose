## 測試畫框使用另一隻py
#%%

import cv2
import matplotlib.pyplot as plt
import sys
sys.path.append("/Users/richard/myworkspace/mygitlab/myopenpose/1_crop/")
from rotateFuntion import cropByRotate

url = "/Users/richard/myworkspace/mygitlab/myopenpose/1_crop/baconfireRB.mp4"

cap = cv2.VideoCapture(url)
for i in range(1):
    ret, frame = cap.read()
    if not ret:
        break
    
    frame2 = frame
    
    # p1 = {"x": 100,"y":226}
    # p2 = {"x": 150,"y":150}
    # L_p = {"x":100,"y":150}
    # B_p = {"x":120,"y":226}
    p1 = {"x":200,"y":226}
    p2 = {"x":300,"y":150}
    L_p = {"x":200,"y":226}
    B_p = {"x":300,"y":150}
    
    frame2 = cropByRotate(frame2,p1,p2,L_p,B_p)
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    
    plt.imshow(frame)   
    plt.show()
    
    plt.imshow(frame2)   
    plt.show()

# %%
