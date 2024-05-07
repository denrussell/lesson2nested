# Task 1: Code Correction
'''
place = input("Choose a place: forest or cave? ")

if place == "forest":                # Need another equal sign here
    action = input("climb a tree or cross a river? ")   # Added a space before end quote
    if action == "climb a tree":       # Need another equal sign here
        print("You found a bird's nest!")
    elif action == "cross a river":    # Changed else to elif and added another =
        print("You found a boat!")    
    else:     # added else for all other answers
        print("You are in for an adventure!")
elif place == "cave":            # Need another equal sign here
    print("You found a hidden treasure!")   # replaced find with found
else:
    print("You're in for an adventure!")   # added an else for all other answers
'''


# Task 2: Setting the Scene
# Task 3: Default Path

place = input("Choose a place: forest or cave? ")

if place == "forest":                
    action = input("climb a tree or cross a river? ")   
    if action == "climb a tree":      
        print("You found a bird's nest!")
    elif action == "cross a river":    
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":          
        print("You found a hidden treasure!")  
    elif action == "proceed in the dark":
        print("There is a monster lurking. Be careful!")
    else:
        pass
else:
    pass   
