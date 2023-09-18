#Name: Daniel Duclos
#Date: January 28, 2021
#Purpose: Create a fully functioning minesweeper game.
import random

#Decides how big the map will be
def find_map_size():
    size = 9
    return size
    
#Creates certain number of rows and columns based on the size
def build_map(size):
    game_map = []
    for i in range (size):
        game_map.append([])
        for y in range (size):
            initializedSquare = {'NearbyBombs': 0, 'IsRevealed' : False, 'IsFlagged' : False}
            game_map[i].append(initializedSquare)
    return game_map

#Finds a difficulty to determine the probability of a bomb being placed.
def find_difficulty():
    return 25
    
#Randomly decides if a space is a bomb   
def decide_if_Bomb(difficulty):
    rando = random.randint(1, 100)
    if rando <= difficulty:
        return True
    else:
        return False

#goes through the map and uses (decide_if_bomb) to determine which spot is a bomb. Using a for loop to sweep through all spaces.
def place_bombs(game_map, difficulty):
    for i in range (len(game_map)):
        for y in range(len(game_map)):
            isBomb = decide_if_Bomb(difficulty)
            game_map[i][y]['IsBomb'] = isBomb

#"master map" to help creator test code, can see where bombs are.
def master_map(game_map):
    for i in range(len(game_map)):  
        for j in range(len(game_map[i])):       
            if game_map[i][j]['IsBomb'] == True:    
                print('B ', end='')
            else:
                print('S ', end='')
        print()

#This works with (scan_around) to go through each space and find the neighboring bombs
def find_nearby_bombs(game_map, size):
    for i in range(len(game_map)):  
        for j in range(len(game_map[i])):
            scan_around(game_map, i, j)

#Checks if a given square is inside the game map
def check_if_in_map(game_map, i, j):
    if i < 0 or j < 0:
        return  False
    elif i >= len(game_map) or j >= len(game_map):
        return  False
    else:
        return True

#Scans around specific space to find how many neighbouring bombs there are
def scan_around(game_map, i, j):
    #Below selected spot
    spot_in_or_out = check_if_in_map(game_map, i+1, j)
    if spot_in_or_out == True:
        if game_map[i+1][j]['IsBomb'] == True:
            game_map[i][j]['NearbyBombs'] = game_map[i][j]['NearbyBombs'] + 1
    #Below to the right of selected spot                        
    spot_in_or_out = check_if_in_map(game_map, i+1, j+1)
    if spot_in_or_out == True:
        if game_map[i+1][j+1]['IsBomb'] == True:
            game_map[i][j]['NearbyBombs'] = game_map[i][j]['NearbyBombs'] + 1
    #Below to the left of selected spot
    spot_in_or_out = check_if_in_map(game_map, i+1, j-1)
    if spot_in_or_out == True:
        if game_map[i+1][j-1]['IsBomb'] == True:
            game_map[i][j]['NearbyBombs'] = game_map[i][j]['NearbyBombs'] + 1
    #Left of selected spot
    spot_in_or_out = check_if_in_map(game_map, i, j-1)
    if spot_in_or_out == True:
        if game_map[i][j-1]['IsBomb'] == True:
            game_map[i][j]['NearbyBombs'] = game_map[i][j]['NearbyBombs'] + 1
    #Right of selected spot
    spot_in_or_out = check_if_in_map(game_map, i, j+1)
    if spot_in_or_out == True:
        if game_map[i][j+1]['IsBomb'] == True:
            game_map[i][j]['NearbyBombs'] = game_map[i][j]['NearbyBombs'] + 1
    #Above selected spot
    spot_in_or_out = check_if_in_map(game_map, i-1, j)
    if spot_in_or_out == True:
        if game_map[i-1][j]['IsBomb'] == True:
            game_map[i][j]['NearbyBombs'] = game_map[i][j]['NearbyBombs'] + 1
    #Above to the left of selected spot
    spot_in_or_out = check_if_in_map(game_map, i-1, j-1)
    if spot_in_or_out == True:
        if game_map[i-1][j-1]['IsBomb'] == True:
            game_map[i][j]['NearbyBombs'] = game_map[i][j]['NearbyBombs'] + 1 
    #Above to the right of selected spot
    spot_in_or_out = check_if_in_map(game_map, i-1, j+1)
    if spot_in_or_out == True:
        if game_map[i-1][j+1]['IsBomb'] == True:
            game_map[i][j]['NearbyBombs'] = game_map[i][j]['NearbyBombs'] + 1                     
    return game_map

#Prints the actual game map, either an empty space (S) or the number to represent nearby bombs or an (F) to represent a flag.
def print_game_map(game_map, size):
    print ("    1   2   3   4   5   6   7   8   9")
    print ("----------------------------------------")
    for i in range(len(game_map)):
        print (i + 1, "|", end=' ')
        
        for j in range(len(game_map[i])):        
            if game_map[i][j]['IsFlagged'] == True:
                print("F | ", end='')
                
            elif game_map[i][j]['IsRevealed'] == False:
                print("X | ", end='')

            elif game_map[i][j]['IsBomb'] == True and game_map[i][j]['IsRevealed'] == True:    
                print('B | ', end='')
    
            else:
                print(game_map[i][j]['NearbyBombs'], "|", end=' ')
                
        print()
        for j in range (len(game_map)-1):
            print("-----", end='')
        print()

#Takes whatever spot the user wants to uncover as two inputs, a row and column
def take_user_choice(size):
    user_choice = []
    while True:
        try:
            user_choice_row = int(input("What row? "))
            if user_choice_row < 0 or user_choice_row > size:
                print("\nThat selection does not fit in the map, please enter a valid number.")      

        except ValueError:
            print("\nEntry must be an integer!")
            
        else:
            break
        
    while True:
        try:
            user_choice_column = int(input("What column? "))
            if user_choice_column < 0 or user_choice_column > size:
                print("\nThat selection does not fit in the map, please enter a valid number.")   

        except ValueError:
            print("\nEntry must be an integer!")

        else:
            break
        
    while True:
        user_choice_flag = input("\nDo You Want To Flag This Location? (Yes/No) ").lower()
        if user_choice_flag == "yes" or user_choice_flag == "no" or user_choice_flag == "n" or user_choice_flag == "y":
            break
        
        else:
            print("\nInvalid entry, please try again. \n")
            
    user_choice.append(user_choice_row)
    user_choice.append(user_choice_column)
    user_choice.append(user_choice_flag)
    return user_choice

#Uncovers the spot and checks if it is a bomb or not
def uncover_spot(user_choice, game_map):
    row = user_choice[0]
    column = user_choice[1]
    flag = user_choice[2]
    column = column - 1
    row = row - 1
    
    if flag == "yes" or flag == "y":
        game_map[row][column]['IsFlagged'] = True
        game_map[row][column]['IsRevealed'] = True
    
    elif flag == "no" or flag == "n":
        if game_map[row][column]['IsFlagged'] == True:
            game_map[row][column]['IsFlagged'] = False
            game_map[row][column]['IsRevealed'] = False
            
        elif game_map[row][column]['IsRevealed'] == False:
            if game_map[row][column]['IsBomb'] == False and game_map[row][column]['NearbyBombs'] == 0:
                dig(game_map, row, column)
            game_map[row][column]['IsRevealed'] = True
            
            if game_map[row][column]['IsBomb'] == True:
                ans = if_bomb_found(game_map, row, column)
                return ans

#Uses recursion to dig around if a selected square's nearby bomb count is 0, uncovers squares until each one has at least one nearby bomb.
def dig(game_map, x, y):
    if x < 0:
            return
    if y < 0:
            return
    if y > len(game_map) - 1:
        return
    if x > len(game_map) - 1:
        return
    if game_map[x][y]['IsRevealed'] == True:
        return
    
    if game_map[x][y]['IsBomb'] != True:
        game_map[x][y]['IsRevealed'] = True
        
    if game_map[x][y]['NearbyBombs'] == 0:
        dig(game_map, x-1, y-1)    
        dig(game_map, x, y-1)    
        dig(game_map, x+1, y-1)    
        dig(game_map, x-1, y)    
        dig(game_map, x+1, y)    
        dig(game_map, x-1, y+1)    
        dig(game_map, x, y+1)    
        dig(game_map, x+1, y+1)    

#Checks if all nonbomb spots have won
def check_if_win(game_map):
    for i in range(len(game_map)):  
        for j in range(len(game_map[i])):
            if game_map[i][j]['IsBomb'] == False and game_map[i][j]['IsRevealed'] == False:
                return False
    return True

#Sees if a bomb was found 
def if_bomb_found(game_map, row, column):
    game_map[row][column]['IsRevealed'] = True
    print("\nYou've unconvered a bomb! Please answer this question correctly to continue.")
    ans = random_math()
    return ans

#Makers a random math problem
def random_math():
    x = random.randint(1,100)
    y = random.randint(1,100)
    j = random.randint(1,3)
    if j == 1:
        while True:
            try:
                UserAns = int(input("\nWhat is %s + %s? " % (x, y)))
                if UserAns == x + y:
                    print("\nYou are right!\n")
                    break
                else:
                    return 0
            
            except ValueError:
                print("\nEntry must be an integer!")
            
    if j == 2:
        while True:
            try:
                UserAns = int(input("\nWhat is %s - %s? " % (x, y)))
                if UserAns == x - y:
                    print("\nYou are right!\n")
                    break
                else:
                    return 0
                
            except ValueError:
                print("\nEntry must be an integer!")
            
            
    if j == 3:
        while True:
            try:
                UserAns = int(input("\nWhat is %s * %s? " % (x, y)))
                if UserAns == x * y:
                    print("\nYou are right!\n")
                    break
                else:
                    return 0
                
            except ValueError:
                print("\nEntry must be an integer!")

#Calls all functions to create the game
def main():
    playing = "yes"
    while playing == "yes" or playing == "y":
        size = find_map_size()
        game_map = build_map(size)
        difficulty = find_difficulty()
        place_bombs(game_map, difficulty)
        find_nearby_bombs(game_map, size)
        #master_map(game_map)
        print()
        
        while True:
            print_game_map(game_map, size)
            user_choice = take_user_choice(size)
            ans = uncover_spot(user_choice, game_map)
            
            if ans == 0:
                print("\nWrong answer, you blew up.. Thanks for playing though!")
                return
            win_lose = check_if_win(game_map)
            
            if win_lose == True:
                print("\nYou Won!!! Congratulations!!")

        
                playing = input("\nWould you like to play again? (Y/N)")
                break


print ("Hello, welcome to Minesweeper! Here, the goal of this game is to clear a rectangular board containing hidden bombs without detonating any of them, with help from clues about the number of neighboring mines in each field.")
print ("An unknown space is represented by an 'X'. You can flag a space you know is a bomb, these are represented by the letter 'F'")

main()

    
    


