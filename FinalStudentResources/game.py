from linked_list import LinkedList
from queue import Queue
from stack import Stack
from wave import Wave
from non_plant import Non_Plant
from plant import Plant
from card import Card
import random

class Game:

    def init(self, file):
        with open(file, 'r') as f:
            self.cash, self.height, self.width = [int(x) for x in f.readline().split(' ')]
            self.waves = LinkedList()
            self.waves_num = 0
            for line in iter(f.readline, ' '):
                self.waves.add(Wave(*[int(x) for x in line.split(' ')]))
                self.waves_num += 1
        self.board = [[Queue() for x in range(self.width)] for y in range(self.height)]
        self.game_over = False
        self.turn_number = 0
        self.nonplants = 0
        self.deck_powerup_cards = Stack()
        for i in range(100):
            self.deck_powerup_cards.push(Card(random.randint(0, 6)))


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

    def is_nonplant(self, row, col):
        obj = self.board[row][col].peek()
        return type(obj) is Non_Plant

    def is_plant(self, row, col):
        obj = self.board[row][col].peek()
        return type(obj) is Plant

    def remove(self, row, col): #dequeue
