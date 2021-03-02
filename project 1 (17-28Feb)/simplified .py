while True:
    while True:
        start = input("type S to start")
        if start == 'S':
            print("welcome")
            
            main=""
            while main!="R" or main!="L":
                print("choose R or L")
                main=input(">")
                if main=='R':
                    R=""
                    while R!="L" or R!="S":
                        print("choose L or S")
                        R=input(">")
                        if R == "L":
                            R_L=""
                            while R_L!="L" or R_L!="R":
                                print("choose L or R")
                                R_L=input(">")
                                if R_L=="L":
                                    print("DEAD")
                                    break
                                elif R_L=="R":
                                    print("DEAD")
                                    break
                        elif R == "S":
                            R_S=""
                            while R_S!="S" or R_S!="L":
                                print("choose S or L")
                                input(">")
                                if R_S == "S":
                                    print("DEAD")
                                    break
                                elif R_S =="L":
                                    R_S_L=""
                                    while R_S_L !="R" or R_S_L !="L":
                                        print("Choose R od L")
                                        input(">")
                                        if R_S_L=="R":
                                            print("DEAD")
                                            break
                                        elif R_S_L =="L":
                                            print("CONGRATULATIONS")
                                            break
                elif main=='L':
                    L=""
                    while L!="S" or L!="R":
                        print("choose S or R")
                        input(">")
                        if L == "S":
                            print("DEAD")
                            break
                        elif L == "R":
                            L_R=""
                            while L_R!="L" or L_R!="S":
                                print("choose L or S")
                                input(">")
                                if L_R=="L":
                                    print("DEAD")
                                    break
                                elif L_R=="S":
                                    print("DEAD")
                                    break
    q=input("Continue? Y/N")            
    if q=="N":
        break
print('Thank you for playing')

