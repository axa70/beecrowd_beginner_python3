t_c = int(input())

#type,damage, level 1,2,3
spell = {"fire":[200,20,30,50],
         "water":[300,10,25,40],
         "earth":[400,25,55,70],
         "air":[100,18,38,60]}

for i in range(t_c):

    w,h,xbl,ybl = map(int, input().split())
    power,level,cx,cy = input().split()
    level = int(level)
    cx = int(cx)
    cy = int(cy)

    for key,value in spell.items():
        if key==power:
            radius = value[level]
            break
    #rectangle 4 corners
    #bottom left | xbl,ybl
    xbr,ybr = xbl+w,ybl     #bottom right
    xtl,ytl = xbl,ybl+h     #top left
    xtr, ytr = xbl+w,ybl+h  #top right
    tx,ty = cx,cy           #test center
    if cx<xbl: tx = xbl #clamping left
    elif cx>xbr: tx = xbr #clamping right

    if ty<ybl: ty=ybl #clamping bottom
    elif ty>ytl: ty=ytl #clamping top

    distance = ((tx-cx)**2 + (ty-cy)**2)**0.5

    #calculate damage if intersects
    if distance<=radius:
        print(value[0])
    else:
        print("0")



