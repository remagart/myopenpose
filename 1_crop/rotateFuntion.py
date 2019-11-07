## 旋轉然後截圖
#%%

import math
import cv2
# p1 = {"x":2,"y":3}
# p1 最左下 p2 最右上
def cropByRotate(img,p1,p2,L_p,B_p):
    shape = (img.shape[1],img.shape[0])
    print(f"shape: {shape}")
    
    L_p_vec = {"x": L_p["x"],"y": shape[1] - L_p["y"]}
    B_p_vec = {"x": B_p["x"],"y": shape[1] - B_p["y"]}
    
    center_x = int((p1["x"]+p2["x"])/2)
    center_y = int((p1["y"]+p2["y"])/2)
    
    v1 = L_p_vec["x"] - B_p_vec["x"]
    v2 = L_p_vec["y"] - B_p_vec["y"]
    theta = math.atan2(v2,v1)
    theta = int(theta*180/math.pi)
    theta = int(180-theta)
    print(f"theta: {theta}")
    
    width = abs(p2["x"] - p1["x"]) 
    height = abs(p2["y"] - p1["y"])
    
    matrix = cv2.getRotationMatrix2D( center=(center_x,center_y), angle=theta, scale=1 )
    
    img = cv2.warpAffine( src=img, M=matrix, dsize=shape )
    
    x = int(center_x - width/2)
    y = int(center_y - height/2)
    
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"width: {width}")
    print(f"height: {height}")
    
    img = img[y:y+height,x:x+width]
    return img

import cv2
import matplotlib.pyplot as plt

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

#%%


# %%
