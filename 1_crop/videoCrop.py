# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:25:02 2019
@description 實作圖片截圖
@author: jfmamjjasond
"""
#%%
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as plimg

#%%

def handleCrop(pic,x1,x2,y1,y2):
    print("Start crop")
    print(f"shape : {pic.shape}")
    pic = pic[y1:y2,x1:x2,:]
    return pic


#%%

# url = "./baconfireRB.mp4"
url = "/Users/richard/myworkspace/mygitlab/myopenpose/1_crop/baconfireRB.mp4"
cap = cv2.VideoCapture(url)

for i in range(1):
    ret, frame = cap.read()
    if not ret:
        break
#   plt.figure(figsize=(10,10))

    print("pic size",frame.shape)
#   frame = handleCrop(frame,218,216,219,224)
#   frame = handleCrop(frame,131,132,236,230)
#   
#   frame = handleCrop(frame,132,131,231,230)
    frame2 = frame
    frame = handleCrop(frame,221,234,196,213)
    frame2 = handleCrop(frame2,200,270,170,226)
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

    plt.imshow(frame)   
    plt.show()
    plt.imshow(frame2)  
    plt.show()


#%%

## 測試旋轉

#%%
import math

def rotate_crop(img,x1,x2,y1,y2,left_point,bottom_point):
    shape = (img.shape[1],img.shape[0])
    
    y1 = shape[1] - y1
    y2 = shape[1] - y2
    left_point["y"] = shape[1] - left_point["y"]
    bottom_point["y"] = shape[1] - bottom_point["y"]
    
    center_x = int((x1+x2)/2)
    center_y = int((y1+y2)/2)
    
    v1 = left_point["x"] - bottom_point["x"]
    v2 = left_point["y"] - bottom_point["y"]
    print(f"v1: {v1}  v2: {v2}")
    theta = math.atan2(v2,v1)
    theta = int(theta*180/math.pi)
    
    theta = - (int(180-theta))
    print(f"theta: {theta}")
    
    width = x2 - x1
    height = y2 - y1
    
    print(f"YCC center_x: {center_x}  center_x: {center_x}")
    
    matrix = cv2.getRotationMatrix2D( center=(center_x,center_y), angle=theta, scale=1 )
    
    print(f"YCC matrix: {matrix}")
    img = cv2.warpAffine( src=img, M=matrix, dsize=shape )
    
    print(f"YCC imggggg: {img}")
    
    center_y = int(shape[1] - center_y)
    
    x = int(center_x - width/2)
    y = int(center_y - height/2)
    
    print(f"YCC imgggggxxx: {x}")
    print(f"YCC imgggggyyy: {y}")
    print(f"YCC imgggggwidth: {width}")
    print(f"YCC imgggggheight: {height}")
    
    img = img[y:y+height,x:x+width]
    print(f"YCC img: {img}")
    return img


#%%

# url = "./baconfireRB.mp4"
url = "/Users/richard/myworkspace/mygitlab/myopenpose/1_crop/baconfireRB.mp4"

cap = cv2.VideoCapture(url)


for i in range(1):
    ret, frame = cap.read()
    if not ret:
        
        break
    print("pic size",frame.shape)

    
    
    frame2 = frame
    frame3 = frame
    
    # tmp1 = {"x":200,"y":26}
    # tmp2 = {"x":250, "y": 0}
    
    # frame2 = rotate_crop(frame2,200,300,150,226,tmp1,tmp2)
    
    
    tmp1 = {"x":90,"y":200}
    tmp2 = {"x":120, "y": 226}
    
    frame2 = rotate_crop(frame2,90,150,150,226,tmp1,tmp2)
    
    frame3 = frame3[150:226,90:150,:]
    
    print(frame2)
    
#    frame2 = handleCrop(frame2,150,250,0,100)
    
    # frame3 = frame3[150:226,200:300,:]
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    frame3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGB)
    
    plt.imshow(frame)   
    plt.show()
    
    plt.imshow(frame2)   
    plt.show()

    plt.imshow(frame3)   
    plt.show()




#%%

import math

AB = [1,-3,5,-2]
CD = [4,1,4.5,4.5]

def angle(v1, v2):
    dx1 = v1[2] - v1[0]
    dy1 = v1[3] - v1[1]
    dx2 = v2[2] - v2[0]
    dy2 = v2[3] - v2[1]
    angle1 = math.atan2(dy1, dx1)
    angle1 = int(angle1 * 180/math.pi)
    print(f"angle1: {angle1}")
    angle2 = math.atan2(dy2, dx2)
    angle2 = int(angle2 * 180/math.pi)
    print(f"angle2: {angle2}")
    if angle1*angle2 >= 0:
            included_angle = abs(angle1-angle2)
    else:
        included_angle = abs(angle1) + abs(angle2)
        if included_angle > 180:
            included_angle = 360 - included_angle
    return included_angle


ang1 = angle(AB, CD)
print("AB和CD的夾角")
print(ang1)

#%%