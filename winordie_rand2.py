#An updated version of WinOrDie_rand - using left/right in the random choice area of gruedoor to make the 

import random

def doors_printer():
    for i in range (0,8):
        print("\n")
    print(" " * 10 + " ╔" + "═" * 21 + "╗" + " " * 10 + " ╔" + "═" * 21 + "╗")
    for i in range(0, 10):
        print(" " * 10 + " ║"+" " * 21 + "║" + " " * 10 + " ║"+" " * 21 + "║")
    print(" " * 10 + " ║  /\\" +  " " * 17 + "║" + " " * 10 + " ║  /\\" + " " * 17 + "║")
    print(" " * 10 + " ║  \\/" +  " " * 17 + "║" + " " * 10 + " ║  \\/" + " " * 17 + "║")
    for i in range(0, 11):
        print(" " * 10 + " ║"+" " * 21 + "║" + " " * 10 + " ║"+" " * 21 + "║")
    print(" " * 10 + " ╚" + "═" * 21 + "╝" + " " * 10 + " ╚" + "═" * 21 + "╝")
    for i in range (0,3):
        print("\n")
		
def gruedoor():
	global grue_door
	options = ['left', 'right']
	grue_door = random.choice(options) #In this case if the door is True the Grue is behind the left door, if False it's behind the right door, this is checked in the first if statement of the dooreval function.
	return grue_door
def dooreval(door):	
	global player_state
	if (door == grue_door):
		print('I\'m sorry, you were eaten by a grue.')
		player_state = 'dead'
		return player_state
	elif (door == 'left' or door == 'right'):
		print('You escaped!')
		player_state = 'won'
		return player_state	
	else:
		print('Try again')	
		
player_state = 'null'
grue_door = 'empty'
while player_state != 'won' or 'dead':  #the game loop - keeps asking for a door until one is entered by the player.
	if player_state != 'null':
		break
	#print(player_state)  #debug line - to ensure the player state was being correctly updated.
	gruedoor()  #runs the gruedoor function, randomly setting the Grue behind one of the doors.
	doors_printer()
	#print(grue_door)  #testing line - Uncomment the print statement to know where the Grue is.
	print ("A Grue is behind one of these doors. It will eat you.")
	door = input("Please choose a door, Left or Right:\n").lower() #assigns the input to a var and lowers the input for evaluation.
	#print (door)
	dooreval(door)