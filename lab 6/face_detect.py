import cv2 as cv 


def face_det():
    
    img = cv.imread('train\Leffe\inkludering.jpg')
    cv.imshow('Gruppen', img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('gruppen', gray)

    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)


    print(f'Number of face found = {len(faces_rect)}')
    # loopa genom faces_rect och skapa en rektangel med hjälp av koordinater

    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detected faces', img) 

    cv.waitKey(1)