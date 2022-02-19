import random

from sympy import true

# left bottom : (0,0), right top : (1000,1000)
field=(0.0,0.0,100.0,100.0)

rects=[]
randint_min=4
randint_max=10
m=2.0
a=m*float(random.randint(randint_min,randint_max))   # horizontal length
b=m*float(random.randint(randint_min,randint_max))   # vertical length
S=a*b
print(a,b,S)
rects.append((0.0,0.0,a,b))
#print("first rect : ", rects)

 # (1,0):right , (-1,0):left , (0,1):up , (0,-1):down
direction_list=[(1,0), (-1,0), (0,1), (0,-1)]

i=0
tot=0
cnt_overlay=0
cnt_outside=0
#for _ in range(10):
while(true):
    tot+=1
    direction=direction_list[random.randint(0,3)]
    print("direction : ",direction)
    seed=random.choice([0,0,0,0,0,0,0,0,0,0,0,1])
    if seed%2==0:
        offset=0
    else:
        offset=float(random.randint(randint_min,randint_max))
    if(direction==(1,0)):
        a=m*float(random.randint(randint_min,randint_max))
        S=a*b
        print(a,b,S)
        newrect=(rects[i][2]+offset,rects[i][1],rects[i][2]+offset+a,rects[i][3])
    elif(direction==(-1,0)):
        a=m*float(random.randint(randint_min,randint_max))
        S=a*b
        print(a,b,S)
        newrect=(rects[i][0]-a-offset,rects[i][1],rects[i][0]-offset,rects[i][3])
    elif(direction==(0,1)):
        b=m*float(random.randint(randint_min,randint_max))
        S=a*b
        print(a,b,S)
        newrect=(rects[i][0],rects[i][3]+offset,rects[i][2],rects[i][3]+offset+b)
    elif(direction==(0,-1)):
        b=m*float(random.randint(randint_min,randint_max))
        S=a*b
        print(a,b,S)
        newrect=(rects[i][0],rects[i][1]-offset-b,rects[i][2],rects[i][1]-offset)
    appendfalg=1
    if newrect[0]>=field[0] and newrect[1]>=field[1] and newrect[2]<=field[2] and newrect[3]<=field[3]:
        for j in rects:
            if (newrect[0]-j[0])*(newrect[0]-j[2])<0 or (newrect[2]-j[0])*(newrect[2]-j[2])<0 \
                or (newrect[1]-j[1])*(newrect[1]-j[3])<0 or (newrect[1]-j[1])*(newrect[1]-j[3])<0:
                    appendfalg=0
                    print("+++++ overlay")
                    cnt_overlay+=1
                    break
        if appendfalg:    
            rects.append(newrect)
            i+=1
    else:
        print("===== outside")
        cnt_outside+=1
    #print("========== i : ",i)
    if i==100:
        print("---")
        break
print(rects)
print("tot, cnt_overlay, cnt_outside : ",tot, cnt_overlay, cnt_overlay)

import matplotlib.pyplot as plt
from matplotlib import patches
 
fig, ax = plt.subplots(figsize=(4,4))

ax.set_xticks([-10,0,10,20,30,40,50,60,70,80,90,100,110])
ax.set_yticks([-10,0,10,20,30,40,50,60,70,80,90,100,110])

color=["red","green","blue"]
cmap = plt.get_cmap("tab10")
for i in range(len(rects)):
    #i=0
    init=(rects[i][0],rects[i][1])
    w=rects[i][2]-rects[i][0]
    h=rects[i][3]-rects[i][1]
    r = patches.Rectangle( init , w, h, fill=False, edgecolor=color[i%3], linewidth=1)
    #b = patches.FancyBboxPatch(init , w, h, facecolor=color[i%3], boxstyle="square")
    ax.add_patch(r)
    #ax.add_patch(b)

plt.show()
