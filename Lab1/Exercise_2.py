def isPointInRectangle (x, y, w,h , x1 , y1) :
    if x <= x1 <= x + w and y <= y1 <= y +h :
        return True
    else :
        return False

x1 = float (input ("Insert x1: "))
y1 = float (input ("Insert y1: "))
if isPointInRectangle(4,6,3,3,x1 , y1):
     print ("The point is inside the rectangle")
else :
    print ("The point is outside the rectangle")
