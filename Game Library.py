"""
Game Library
"""
#Pre made list of games
game_List = ['Berserk', 'Donkey Kong', 'Frogger', 'Galaga', 'Missile Command', 'Space Invaders', 'Tetris']

#Loop so that it will keep going untill stopped
while True:
#Main Menu, new line on main menu so it is not clustered
    print ('''
	Main Menu
    1.   Display all Games
    2.   Search for Games
    3.   Insert Game
    4.   Delete Game
    5.   Exit
	''')
  
    menuInput = input ('Enter a menu selection: ')
#Error checking for input
    try:
        menuInput = int(menuInput)
    except:
        print ('Please enter a proper numrical value to select menu option')
        menuInput = input ('Enter a menu selection: ')
        menuInput = int(menuInput)
#Creats vertical list
    if (menuInput == 1):
        print ('Game Libary\n')
        print ('==============\n')
        for i in game_List:
           print(i)
#Searches for games
    elif (menuInput == 2):
        searchGame = input ('Enter the name of the Game to find: ')
        if searchGame in game_List :
            print (str(searchGame) + ' is in the game libary')
        else:
            print (str(searchGame) + ' is not in the game libary')
#Adds new games
    elif (menuInput == 3):
        addGame = input ('Enter the name of the game to add: ')
        if addGame in game_List :
            print (str(addGame) + ' is already in the game libary')
        else:
            game_List.append (str(addGame))
            print ('Game added')
#Deletes games
    elif (menuInput == 4):
        removeGame = input ('Enter the name of the game to delete: ')
        if removeGame in game_List :
            game_List.remove(str(removeGame))
            print (str(removeGame) + ' removed from the game libary')
        else:
            print (str(removeGame) + ' is not in the game libary')
#Quits the program
    elif (menuInput == 5):
        exit()
#Error checking for menu
    else:
        print ('Please enter a numrical value between 1 and 5 to select menu option')
