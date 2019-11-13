## 畫框框的函式
#%%
import matplotlib.pyplot as plt
import cv2
import math

def handleDraw(x1,y1,x2,y2):
    RATE = 10
    aa = {"x": x1,"y": y1}
    bb = {"x": x2,"y": y2}
    direct = [bb["x"]-aa["x"],bb["y"]-aa["y"]]
    
    value = math.sqrt(direct[0] * direct[0] + direct[1] * direct[1]) / 3
    direct = [direct[0]/value,direct[1]/value]
    
    dir1 = [direct[1]*(-RATE),direct[0]*RATE]   
    dir2 = [direct[1]*(RATE),direct[0]*(-RATE)]   


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

    print(f"YCC p1: {p1x} , {p1y}")
    print(f"YCC p2: {p2x} , {p2y}")
    print(f"YCC p3: {p3x} , {p3y}")
    print(f"YCC p4: {p4x} , {p4y}")
    
    plt.plot(tmp,tmp2);
    plt.scatter([aa["x"],bb["x"]],[aa["y"],bb["y"]]);
    
#%%

# url = "/Users/richard/myworkspace/mygitlab/myopenpose/1_crop/baconfireRB.mp4"
# cap = cv2.VideoCapture(url) 

# for i in range(1):
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     frame2 = frame
    
#     handleDraw(200,226,300,150)
    
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     # frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    
#     plt.imshow(frame)   
#     plt.show()
    
#     # plt.imshow(frame2)   
#     # plt.show()
    
# %%
