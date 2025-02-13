#Task 2

arr2d= [[2,3,5],[9,4,7],[3,9,6]]
sumx = 0
sumy = 0


for x in arr2d:
    maxx = [0]
    minx = [0]
    for y in arr2d:
    maxy = [0]
    miny = [0]
    
    sumy = sumy + y
    if y > maxy:
        maxy = y
    elif y < miny:
        miny = y

        
    sumx = sumx + x
    if x > maxx:
        maxx = x
    elif x < minx:
        minx = x

    




