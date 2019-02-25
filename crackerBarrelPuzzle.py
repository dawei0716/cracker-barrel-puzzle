from random import randint

possibleMove = {0:(3,5), 1:(6,8), 2:(7,9),
				3:(0,5,10,12), 4:(11,13),
				5:(0,3,12,14), 6:(1,8),
				7:(2,9), 8:(1,6), 9:(2,7),
				10:(3,12), 11:(4,13),
				12:(3,5,10,14), 13:(4,11),
				14:(5,12)}

def main():
	replay = True
	while(replay):
		brd = ['X', 'X', 'X', 'X', 'X','X','X','X','X','X','X','X','X','X','X',]
		brd[randint(0,14)] = 'O'
		printBoard(brd)

		moveAvailable = moveIsAvailable(brd)
		while(moveAvailable):
			
			moveFrom, moveTo = promptMove()
			while(moveFrom < 0 or moveFrom > 14 or moveTo < 0 or moveTo > 14):
				print("Both indices must be integers 0~14")
				moveFrom, moveTo = promptMove()
			#(moveFrom+moveTo)//2 calculates the index that is jumped over.  
			while(brd[(moveFrom+moveTo)//2] == 'O' or moveTo not in possibleMove[moveFrom] or
				brd[moveFrom] == 'O' or brd[moveTo] == 'X'): 
				print("Invalid move. Try again.")
				moveFrom, moveTo = promptMove()

			brd[moveFrom] = 'O'
			brd[moveTo] = 'X'
			brd[(moveFrom+moveTo)//2] = 'O' 

			printBoard(brd)
			moveAvailable = moveIsAvailable(brd)
		
		remainingPegs = brd.count('X')
		if(remainingPegs == 1):
			print(f'Wow! You won the game with only 1 peg remaining!')
		else:
			print(f'You finished the game with {remainingPegs} pegs remaining. You can do better!')
		replay = askPlayAgain()
	
def moveIsAvailable(brd):
	for key, values in possibleMove.items():
		for value in values:
			if brd[(key+value)//2] == 'X':
				if brd[key] != brd[value]:
					return True
	return False


def printBoard(brd):
	print()
	print('Game Board    Index Reference ')
	print(f'    {brd[0]}    ' + '           0')
	print(f'   {brd[1]} {brd[2]}   ' + '          1 2          ')
	print(f'  {brd[3]} {brd[4]} {brd[5]}  ' + '        3  4  5         ')
	print(f' {brd[6]} {brd[7]} {brd[8]} {brd[9]} ' + '       6  7  8  9        ')
	print(f'{brd[10]} {brd[11]} {brd[12]} {brd[13]} {brd[14]}' + '     10 11 12 13 14')
	print()

def promptMove():
	while True:
		try: 
			moveFrom, moveTo = map(int, input("enter two indices 'move-from' and 'move-to':").split())
			break
		except: 
			print("Invalid input. Input must be two integers separated by space.")
	return moveFrom, moveTo

def askPlayAgain():
    replay = input("Play again? Enter 1 for yes, 0 for no: ")
    while not (replay == '1' or replay == '0'):
        replay = input("Invalid Input. Play again? Enter 1 for yes, 0 for no: ")
    if (replay == '1'):
        return True
    else:
        return False

if __name__ == '__main__':
    main()

print("Thanks for playing")
