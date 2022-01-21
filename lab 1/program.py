from concurrent.futures.process import _sendback_result
from shutil import SameFileError
import modules


def main():          
        svar=True
        while svar:
            print ("""
            1.Delbara heltal
            2.Gissningsleken
            3.Exit / breKK
            """)
            ans=input("Vad skulle du vilja göra? ") 
            if ans=="1":
                modules.delbara_heltal() 
            elif ans=="2":
                modules.gissnings_spel()
            elif ans=="3":
                print("Tack hejdå.")
                svar = False 
            else:
                print("fel input, välj mellan 1-3....")
        
main()