print("\n\nWELCOME TO THE WORLD 1.\n\nAre you ready to put your memory in a test? Come step in to the dark world of the 'Maze of Eternity'.\n")
# main loop
while True:
        #entrance to the maze:
        while True:
            start = input("Type 's' to enter the maze: \n")
            if start == 's':
                break
        
        #condition 1
        print('\n\nYou have entered the Maze of Eternity! \n\n\t"If you wanna leave this world behind,\n\tYou better use the power of your mind!"\n\nYou walked down in the corridor for a while. \n')
        
        while True:
            op_1 = input("There seems two options in front of you to choose : (l) Left or (r) Right: \n")
            
            if op_1 =='l' or  op_1 =='r':
                break
            elif op_1 !='l' and  op_1 !='r':
                print("Invalid Entry! Pull yourself together and try again! \n")
    
        
        #condition 1 on MAIN BRANCH
        if op_1 == 'l':
            print('\n\t"It is getting colder you see,\n\tIs this the place you really want to be?"\n\nAs soon as you take the left, you faced another two corridors relatively darker:\n')
            while True:
                op_2 = input("Another decision needs to be made; \n(s) Straight or (r) Right\n")                
                if op_2 =='s' or op_2 =='r':
                    break
                elif op_2 !='s' and  op_2 !='r':
                    print("Invalid Entry! Pull yourself together and try again! \n")
        
                    
            #condition 2 (S) SECOND BRANCH
            if op_2 == 's':
                print('\n\t"I smell the fear in your breath,\n\tIs it because of your coming DEATH?"\n\nThere was a giant spider and it bit you. YOU ARE DEAD!\n')
                
            #condition 1 (R) SECOND BRANCH
            elif op_2 == 'r':
                print('\n\t"Do you see the beams of light getting weaker,\n\tHere, the death and darkness walk together!"\n\nThat was a relief. You have survived so far. You move forward and see two path in front of you;\n')
                
                while True:
                    op_3 = input("Which way are you gonna go?; \n(s) Straight or (l) Left\n")
                    if op_3 =='s' and op_3 == 'l':
                        break 
                    
                    elif op_3 !='s' and  op_3 !='l':
                        print('Invalid Entry! Come on, you can do it. Try again!\n')
                                
                #condition 1 (S) THIRD BRANCH
                    if op_3 == 's':
                        print('\n\t"Beware the ground you stand,\n\tScream and shout, here comes the end!"\n\nThere was a "Booby Trap" and YOU ARE DEAD!\n')
                        break 
                
                #condition 2 (L) THIRD BRANCH
                    elif op_3 == 'l':
                        print('\n\t"Oh! your hope for survival was absurdity,\n\tNow you fool, shall keep falling for eternity"\n\nYou did not watch your step while walking and fell in to the endless well. YOU ARE DEAD!\n')
                        break                     
         
       
        #condition 2 (R) on MAIN BRANCH
        elif op_1 =='r':
            print('\n\t"The entrance stands right behind,\n\tGo back and scream if you like"\n\n You go deeper into the maze now. You walk a little and follow the corridor that turns left.\n')
            while True:
                op_4 = input(" Now you need to choose between (l) Left and (s) Straight\n")                
                if op_4 =='l' or op_4 =='s':
                    break
                elif op_4 !='s' and  op_4 !='l':
                    print("Invalid Entry! You need to be more carefull! Try again! \n")
        
                    
            #condition 4 (S) SECOND BRANCH
            if op_4 == 's':
                print('\n\t"We have just started, the fun begins, \n\tBut on this battlefield, no one wins"\n\nYou have made a correct decision it seems. You start to feel the breeze on your skin. You must be close to see the daylight! There are two options stands in front of you to move on:\n')
     #_____________________________________      
                while True:
                    op_6 = input(" The dilemma of your life; (s) Straight or (l) Left\n")                
                    if op_6 =='l' or op_6 =='s':
                        break
                    elif op_6 !='s' and  op_6 !='l':
                        print("Invalid Entry! It's ok! Try again! \n")            
                   
                if op_6 == 's':
                    print('\n\t"Candle lights are shimmering on the walls,\n\tIf you listen, you can hear, your death calls"\n\nYour heart couldn\'t stand with the action and the fear. You had an heart attack and YOU ARE DEAD!\n')
            
                elif op_6 == 'l':
                    print('\n\t"Is it the exit? Maybe your mind is playing tricks,\n\tYou have to make a decision and count up to six"\n\nYou must be very lucky to come this far in the maze! Well done. You have survived enough to make another decision.\n')
                
                    while True:
                        op_7 = input("Which way are you gonna go?; (r) Right or (l) Left\n")
                        if op_7 =='r' and op_7 == 'l':
                            break 
                    
                        elif op_7 !='r' and  op_7 !='l':
                            print("Invalid Entry! Come on, you can do it. Try again!\n")
                                
                #condition 3 (L) THIRD BRANCH
                        if op_7 == 'r':
                            print('\n\t"So when you\'re waiting for the next attack,\n\tYou\'d better stand, there is no turning back"\n\nYou are attacked by a poisonous snake and could not fight back. YOU ARE DEAD!\n')
                            break 
                
                #condition 4 (R) THIRD BRANCH
                        elif op_7 == 'l':
                            print('\n\t"With your escape all the pain and sorrow now seems fake,\n\tWho knows, maybe you were dreaming when you are awake"\n\nCONGRATULATIONS! You survived the Maze of Eternity!\n')
                            break                 
     #_____________________
            
            #condition 3 (R) SECOND BRANCH
            elif op_4 == 'l':
                print('\n\t"You race towards the end among these walls,\n\tWith the screams of lost souls as the rain falls"\n\nThat was close! Anyway, you are still alive and walking. You stepped into a hole that splits in to two hallways;\n')
                
                while True:
                    op_5 = input("Choose your way; (r) Right or (l) Left\n")
                    if op_5 =='r' and op_5 == 'l':
                        break 
                    
                    elif op_5 !='r' and  op_5 !='l':
                        print("Invalid Entry! It's ok! Try again!\n")
                                
                #condition 3 (L) THIRD BRANCH
                    if op_5 == 'r':
                        print('\n\t"Dying because of walking is not very usual,\n\tBut don\'t worry, rats will celebrate your funeral"\n\nYou exhausted and even cannot move a finger. Now all kinds of creatures are waiting for you to fall asleep. YOU ARE DEAD!\n')
                        break 
                
                #condition 4 (R) THIRD BRANCH
                    elif op_5 == 'l':
                        print('\n\t""Among all the people who lost their path,\n\tYou are the one that is doomed to DEATH!"\n\nIt is very dark and you are completely lost, Few days past and YOU ARE DEAD!\n')
                        break                     
            
    
        answer = input("do you wanna continue? y/n: \n")
        if answer == 'n':
            print('Thank you for playing')
            break