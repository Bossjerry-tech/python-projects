weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper == "L":
     converted = weight * 0.45
     print(f"You are {converted} kilos")
else:
    converted = weight/ 0.45
    print(f"You are {converted} pounds")
    
    
    i = 1
    while i <= 5:
        print( '*' *i)
        i = i + 1
    print("Done")
    
    #Guess game
    secret_number = 9
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count += 1
        if guess == secret_number:
           print("You won!")
           break
    else:
        print("Sorry you lost try again!")
  
  
  # car game
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Hey, the car is already started!")
        else:
            started = True
            print("Car started... Ready to go!")
    elif command == "stop":
        if not started:
            print("The car is already stopped.")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that!")