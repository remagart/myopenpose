#%%
import cv2
import matplotlib.pyplot as plt
import sys
sys.path.append("/Users/richard/myworkspace/mygitlab/myopenpose/2_drawSquare/")
import Func_DrawSquare
sys.path.append("/Users/richard/myworkspace/mygitlab/myopenpose/1_crop/")
import rotateFuntion

url = "/Users/richard/myworkspace/mygitlab/myopenpose/1_crop/baconfireRB.mp4"
cap = cv2.VideoCapture(url) 

for i in range(1):
    ret, frame = cap.read()
    if not ret:
        break
    
    p1={"x":200,"y":226}
    p2={"x":300,"y":150}
    
    test = Func_DrawSquare.getTouchPoint(p1,p2)
    
    print("========================")
    print(test)
    
    frame2 = frame
    
    frame2 = rotateFuntion.cropByRotate(frame2,test[0],test[1],test[2],test[3])
    
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    
    plt.imshow(frame)   
    plt.show()
    
    plt.imshow(frame2)   
    plt.show()


#%%