from face_detect import face_det
from face_recognition import face_rec
from face_train import face_tra
import cv2 as cv
import numpy as np



def main():
    svar=True
    while svar:
        print("""
        Select an OpenCV operation
        1.Face detect and data gathering
        2.Face training
        3.Face recognition
        4.Halp
        5.Quit
        """)

        ans=input("Välj ett av alternativen mellan 1-5: ")
        print()
        if ans =="1":
            print("Face detection")
            face_det()
        if ans == "2":
            print("Training in the faces")
            face_tra()
        if ans =="3":
            print("Face recognitionz")
            face_rec()
        if ans =="4":
            print("Ring poolia or Hans Jones")
            print()
        if ans =="5":
            print("Nu har du snuskat klart, hejdå")
            print()
            svar = False












main()