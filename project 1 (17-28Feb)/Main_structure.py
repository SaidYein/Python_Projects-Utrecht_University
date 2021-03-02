print("Welcome to .....")
while True:    
    while True:
        print("Choose a world to play")
        choose_world = input("(1). Dungeon crawler\n(2). Music Quiz\n(3). Maze\n")
        if choose_world =="1" or choose_world =="2" or choose_world == "3":
            break
        else:
            print("invalid")
           
    if choose_world == '1':
        print("World 1 goes here")
    elif choose_world == '2':
        print("World 2 goes here")
    elif choose_world == '3':
        print("World 3 goes here")
    
    play=input("Do you want to play another world? y/n")
    if play=="n":
        break
print("\nThank you for playing our games")
#Is ıt possible to run the worlds as a function???