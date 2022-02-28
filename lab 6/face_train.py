import os 
import cv2 as cv
import numpy as np

def face_tra():


    # skapa en lista med personernas namn
    people = ['Ben Afflek', 'Elton John','Jerry Seinfield', 'Madonna', 'Mindy Kaling','Leffe']


    #skapa en directory med basmappen TRAIN
    DIR = r'C:\Users\valli\Documents\GitHub\SkriptProg\lab 6\train'

    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    features = []
    labels = []

    def create_train():
        for person in people: # loopar igenom listan people 
            path =  os.path.join(DIR, person) # koppla ihop DIR med personen
            label = people.index(person) # skapa en laben som sätts efter vilket index det är i listan
            # nu inne i mappen
            for img in os.listdir(path): # för vaje bild innuti path 
                img_path = os.path.join(path,img) # koppla path till img
                # läs in bilden från path
                img_array = cv.imread(img_path) # läser in bilden från img_path
                gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY) # sparar bilden som grå
                
                # detect faces
                # detectar en grå bild(gray) med factor 1.1 och min neighbors 4
                faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
                # loopa igenom alla faces den ska detektera
                for (x,y,w,h) in faces_rect:
                    faces_roi = gray[y:y+h , x:x+w]
                    features.append(faces_roi)
                    labels.append(label)


    create_train()

    print('Training done -------------')

    features = np.array(features, dtype='object')
    labels = np.array(labels)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    # Train the recognizer on the feateres list and the labels list
    face_recognizer.train(features, labels)
    # sparar features med features variablen
    face_recognizer.save('face_trained.yml')
    np.save('features.npy', features)
    np.save('labels.npy', labels)