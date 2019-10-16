# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 00:39:15 2019

@description 測試截圖
@author: jfmamjjasond
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
import cv2
import math
from PIL import ImageGrab


#%%

def handleDraw(x1,y1,x2,y2):
    aa = {"x": x1,"y": y1}
    bb = {"x": x2,"y": y2}
    direct = [bb["x"]-aa["x"],bb["y"]-aa["y"]]
    
    value = math.sqrt(direct[0] * direct[0] + direct[1] * direct[1]) / 3
    direct = [direct[0]/value,direct[1]/value]
    
    dir1 = [direct[1]*-1,direct[0]*1]   
    dir2 = [direct[1]*1,direct[0]*-1]   


    p1x = aa["x"]+dir1[0]
    p2x = bb["x"]+dir1[0]
    p3x = bb["x"]+dir2[0]
    p4x = aa["x"]+dir2[0]

    p1y = aa["y"]+dir1[1]
    p2y = bb["y"]+dir1[1]
    p3y = bb["y"]+dir2[1]
    p4y = aa["y"]+dir2[1]

    tmp = [p1x,p2x,p3x,p4x,p1x]
    tmp2 = [p1y,p2y,p3y,p4y,p1y]

    plt.plot(tmp,tmp2);
    plt.scatter([aa["x"],bb["x"]],[aa["y"],bb["y"]]);

#%%
import matplotlib.image as mpimg

handleDraw(600,1000,400,100)
handleDraw(9,10,9,18)

img_c = mpimg.imread("screenshot.jpg")
img_x = img_c[500:628,1000:1128,:]

print(img_x.shape)

plt.imshow(img_x)


plt.show()

#im = ImageGrab.grab(100,100,500)
#im.save("screenshot.jpg")
print("Done")



#%%
























