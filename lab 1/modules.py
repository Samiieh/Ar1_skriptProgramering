from random import randint

                                #<------------ Gissnings spelet ------------>

def gissnings_spel():
    guesses_made = 0
    name = input("Hej! Vad heter du? \n")
    number = randint(1,100)
    print(f"Hej {name} jag tänker på ett nummer mellan 1 och 100.\n")
    print("Du har oändligt med gissningar så kör hårt! :D\n")
    
    while guesses_made != number:
        guess = int(input("Skriv in din gissning: "))
        guesses_made += 1
        if guess < number:
            print()
            print("Din gissning var för låg, gissa igen!")
            print(f"Du har gissat: {guesses_made} gånger \n")
        elif guess > number:
            print("Talet du gissade på är för stort ")
            print(f"Du har gissat: {guesses_made} gånger \n")
        else:
            break
    
    
    if guess == number:
        print(f"Snyggt jobbat {name}! Du gissade fram rätt nummer, med {guesses_made} antal gissningar! \n")
    else:
        print(f"Ouch :( , talet jag tänkte på var: {number} \n")  
        
        
                                #<------------ Gissnings spelet ------------>
        
def delbara_heltal():
    print("Du har kommit till delbara tal! \n")
    print("Skriv in det första talet: ")
    tal1 = error_handler()
    #tal1 = int(input("Skriv in det första talet \n"))
    #tal2 = int(input("Skriv in det andra talet \n"))
    print("Skriv in det andra talet: ")
    tal2 = error_handler()
    lista = []
    
    for index in range(1, 1001):
        if (index % tal1==0 and index % tal2 == 0):
            lista.append(index)
    
    print(lista)         
    
    
                                #<---------- error handler -------------->
            
def error_handler():
    while True:
        tal = input("Skriv in ett heltal: ")
        try:
            return int(tal)
        except ValueError:                      ## Exeption som 
            print("Oops!  Fel input, försök igen! det måste vara ett heltal!")
    
            
            
        
            


        

