from linked_list import linked_list
from queue import Queue
from stack import Stack
from wave import Wave
from non_plant import Non_Plant
from plant import Plant
from card import Card
import random

class Game:

    def __init__(self, file):
        with open(file, 'r') as f:
            self.cash, self.height, self.width = [int(x) for x in f.readline().split('')]
            self.waves = LinkedList()
            self.waves_num = 0
            for line in iter(f.readline, ''):
                self.waves.add(Wave(*[int(x) for x in line.split('')]))
                self.waves_num += 1
        self.board = 0
        self.game_over = False
        self.turn_number = 0
        self.powerup_cards = 0

    def draw(self):
        print("Cash: $", self.cash, "\nWaves: ", self.waves_num, sep = '')
        s = ''.join([str(i) for i in range(self.width - 1)])
        print('', s)
        for row in range(self.height):
            s = []
            for col in range(self.width):
                if self.is_plant(row, col):
                    char = 'P'
                elif self.is_nonplant(row, col):
                    size = self.board[row][col].size()
                    char = str(size) if size < 10 else "#"
                else:
                    char = '.'
                s.append(char)
            print(row, '', ''.join(s), '\n', sep='')
        print()
