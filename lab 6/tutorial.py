import cv2

img = cv2.imread('val\leffe_gw\leffe2.jpg' , 0) # spara bilden i img, 0 = svartvit, -1 = default color mode

img = cv2.resize(img, (500, 500)) # storlek på bilden 300px x 300px, annars fx=2, fy=2
#img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE) # rotera bilden 90 grader

cv2.imwrite("val\leffe_gw\leffe2new.jpg", img) # spara bilden i en ny fil
cv2.imshow('Bild', img) # visa bilden, med rubriken Bild.

cv2.waitKey(0) # väntar på att du ska trycka på något
cv2.destroyAllWindows() # ta bort alla fönster som dykt upp