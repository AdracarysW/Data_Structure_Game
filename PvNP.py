import sys
from game import Game

if __name__ == "__main__":
    if len(sys.argv) == 2:
        game = Game(sys.argv[1]);
        game.place_wave()
        game.draw()
        game.get_input()
        #ADD ADDITIONAL CODE HERE
        print("Game Over");
