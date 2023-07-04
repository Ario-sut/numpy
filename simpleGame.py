import numpy as np

def main():
    # create numpy array to store the state of game
    game = np.zeros((3,3))

    #set the first cell to 1
    game[0,0]=1

    print(game)
    # check if the game is over
    if np.all(game == 0):
        print("Game Over")
        return
    
    # make a move
    row = np.random.randint(0,3)
    col = np.random.randint(0,3)
    game[row,col]=1

    # print the game state
    print(game)
    
if __name__ == "__main__":
    main()