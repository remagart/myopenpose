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
   pic = pic[x1:x2,y1:y2,:]
   return pic


#%%

url = "./baconfireRB.mp4"
cap = cv2.VideoCapture(url)

for i in range(1):
   ret, frame = cap.read()
   if not ret:
      break
   plt.figure(figsize=(10,10))
   

   frame = handleCrop(frame,98,226,200,328)   
   
   frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

   plt.imshow(frame)   
   plt.show()


#%%


   








































