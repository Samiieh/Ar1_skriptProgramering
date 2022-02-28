import cv2
import random

img = cv2.imread('marty.jpg', -1)

# print(img.shape) # berättar antal rader och kolumner i numpy arrayen
# Blue green red
# [123, 22 , 0] 123= mängd blått, 22= mängd grön, 0 = mängd röd
# färg sträcker sig från 0-255 svart -> vit
# numpy array för 2pixlar:
#[
#[[0, 0, 0], [255, 255, 255]] en vit pixel=0 och en svart pixel=255
#[[255, 255, 255], [0, 0, 0]] en svart pixel och en vit pixel
#] 
#print(img[150][45:300]) # skriv ut en viss rad och en viss del från den columnen
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
