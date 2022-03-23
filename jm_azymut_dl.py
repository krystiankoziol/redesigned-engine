import numpy as np
import math 

def Read_write(file):
    A = []
    i = 1
    for line in file:
        C = (line.split(';'))
        C[1] = C[1].replace('\n','')
        C[0] = float(C[0])
        C[1] = float(C[1])
        C.append((i))
        i= i+1
        A.append(C)
    return A

def M_point(lst):
    l = len(lst)
    i = 0
    xsr = 0
    ysr = 0
    while i<l:
        xsr=xsr + lst[i][0]
        ysr=ysr + lst[i][1]
        i = i + 1
    xsr = xsr/l
    ysr = ysr/l
    return xsr, ysr

def Distance(lst):
    filepath = 'Dystans.txt'
    f = open(filepath, 'w')
    m_point = M_point(lst)
    l = len(lst)
    distance = []
    i = 0
    while i < l:
        distance.append(np.sqrt((lst[i][0]-m_point[0])**2+(lst[i][1]-m_point[1])**2))
        i = i + 1
    f.write(str(np.transpose(distance)))
    f.close()
    return distance

def Azimuth(pkt1, pkt2):
    angle = 0.0
    x1 = pkt1[0]
    x2 = pkt2[0]
    y1 = pkt1[1]
    y2 = pkt2[1]
    dx = x2 - x1
    dy = y2 - y1
    if x2 == x1:
        angle = math.pi / 2.0
    if y2 == y1 :
        angle = 0.0
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dx / dy)
    elif x2 > x1 and y2 < y1 :
        angle = math.pi / 2 + math.atan(-dy / dx)
    elif x2 < x1 and y2 < y1 :
        angle = math.pi + math.atan(dx / dy)
    elif x2 < x1 and y2 > y1 :
        angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
    return (angle * 180 / math.pi)

def Az(lst):
    filepath = 'Azymuty.txt'
    f = open(filepath, 'w')
    le = len(lst)
    az_ = [0,0,0]
    i = 0
    while i < le:
        j = 0
        while j < le:
            if i == j:
                j = j + 1
            else:
                az_[0]=i+1
                az_[1]=j+1
                az_[2]=Azimuth(lst[i],lst[j])
                f.write(str(az_)+'\n')
                j = j + 1
        i = i + 1
    f.close()
    return 

filepath = 'pkt_cosinusy.txt'
f = open(filepath, 'r')
lst = Read_write(f)
f.close()
print(lst)
Distance(lst)
Az(lst)
