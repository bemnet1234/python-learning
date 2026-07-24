check=""
while True :
    choice = input("> ")
    if check == choice.lower() :
        if check == "start" :
            print("Car is already started!")    
        elif check == "stop" :
            print("Car is already stopped!")
    else :
        
        if choice.lower() == "start" :
            print("Car started...Ready to go!")
        elif choice.lower() == "stop" :
            print("Car stopped.")    
        elif choice.lower() == "quit" :
            print("Exiting the game.") 
            break
        elif choice.lower() == "help" :
            print( """
start- to start the car 
stop- to stop the car
quit- to exit the game""") 
        else :
            print("I don't understand that...")
            choice = input("> ")
    check = choice.lower()