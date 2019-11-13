#%%
import math

def covertToInt(obj):
    obj["x"] = int(obj["x"])
    obj["y"] = int(obj["y"])
    return obj


## p1,p2 骨架
## p1={"x":,"y":""}
def getTouchPoint(p1,p2):
    RATE = 10
    direct = [p2["x"]-p1["x"],p2["y"]-p1["y"]]
    
    ## 計算向量
    value = math.sqrt(direct[0] * direct[0] + direct[1] * direct[1]) / 3
    direct = [direct[0]/value,direct[1]/value]
    ## 有兩個方向
    dir1 = [direct[1]*(-RATE),direct[0]*RATE]   
    dir2 = [direct[1]*(RATE),direct[0]*(-RATE)]
    
    
    e1 = {
        "x": p1["x"] + dir1[0],
        "y": p1["y"] + dir1[1]
    }
    e2 = {
        "x": p2["x"] + dir1[0],
        "y": p2["y"] + dir1[1]
    }
    e3 = {
        "x": p2["x"] + dir2[0],
        "y": p2["y"] + dir2[1]
    }
    e4 = {
        "x": p1["x"] + dir2[0],
        "y": p1["y"] + dir2[1]
    }
    
    sort_x = [e1["x"],e2["x"],e3["x"],e4["x"]]
    sort_y = [e1["y"],e2["y"],e3["y"],e4["y"]]
    
    print(f"sort_x111: {sort_x}")
    print(f"sort_y111: {sort_y}")
    
    sort_x.sort()
    sort_y.sort()
    
    print(f"e1: {e1}")
    print(f"e2: {e2}")
    print(f"e3: {e3}")
    print(f"e4: {e4}")
    
    print(f"sort_x: {sort_x}")
    print(f"sort_y: {sort_y}")

    t1 = {"x":sort_x[0],"y":sort_y[0]}
    t2 = {"x":sort_x[3],"y":sort_y[3]}
    
    list_e = [e1,e2,e3,e4]
    left_touch = e1
    bottom_touch = e1
    i = 0
    while i < 4:
        if left_touch["x"] > list_e[i]["x"]:
            left_touch = list_e[i]
        if bottom_touch["y"] < list_e[i]["y"]:
            bottom_touch = list_e[i]
        i = i + 1
    print(f"left_touch: {left_touch}")
    print(f"bottom_touch: {bottom_touch}")
    
    t1 = covertToInt(t1)
    t2 = covertToInt(t2)
    t3 = covertToInt(left_touch)
    t4 = covertToInt(bottom_touch)
    
    rtn = [t1,t2,t3,t4]

    return rtn 

#%%