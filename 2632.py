#https://www.geeksforgeeks.org/dsa/check-if-any-point-overlaps-the-given-circle-and-rectangle/
#https://www.jeffreythompson.org/collision-detection/circle-rect.php 

t_c = int(input())

#type,damage, level 1,2,3
spell = {"fire":[200,20,30,50],
         "water":[300,10,25,40],
         "earth":[400,25,55,70],
         "air":[100,18,38,60]}

for i in range(t_c):

    w,h,xbl,ybl = map(int, input().split())
    power,level,cx,cy = input().split()
    #radius,cx,cy = map(int, input().split())
    level = int(level)
    cx = int(cx)
    cy = int(cy)

    for key,value in spell.items():
        if key==power:
            #print(f"{key} {value}")
            radius = value[level]
            #print(radius)
            break

    #rectangle 4 corners
    #bottom left | xbl,ybl
    #bootom right
    xbr,ybr = xbl+w,ybl
    #top left  
    xtl,ytl = xbl,ybl+h
    #top right  
    xtr, ytr = xbl+w,ybl+h

    #clamping limiting bounds of circle center
    #updating center of circle to point
    tx,ty = cx,cy
    if cx<xbl: tx = xbl #clamping left
    elif cx>xbr: tx = xbr #clamping right

    if ty<ybl: ty=ybl #clamping bottom
    elif ty>ytl: ty=ytl #clamping top

    #print(f"tx={tx},ty={ty}")

    #find nearest point from center of circle to test point(clamped point)
    distance = ((tx-cx)**2 + (ty-cy)**2)**0.5
    #print(f"distance = {distance}")

    '''
    #cheking is circle intersects rectangle
    if distance<=radius: print("intersects")
    else: print("does not")
    '''

    #calculate damage if intersects
    if distance<=radius:
        print(value[0])

    else:
        print("0")
