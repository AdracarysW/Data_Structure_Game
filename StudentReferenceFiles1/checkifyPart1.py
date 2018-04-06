isorganism = 1
isnonplant = 1
isplant = 1
iscard = 1
iswave = 1
isgame = 1
try:
	from organism import Organism
except ImportError:
	isorganism = 0
try:
	from plant import Plant
except ImportError:
	isplant = 0
try:
	from non_plant import Non_Plant
except ImportError:
	isnonplant = 0
try:
	from card import Card
except ImportError:
	iscard = 0
try:
	from wave import Wave
except ImportError:
	iswave = 0
try:
	from game import Game
except ImportError:
	isgame = 0

######################################################################################################################################
#-----------------ATTENTIONNNNNNNN-------------------WARNING-------------------------------------------------------------------------#
# DON'T COPY THIS STYLE OF CODE, ITS BADLY WRITTEN CODE. BECUASE THIS WAS WRITTEN IN LESS THAN A DAY AND VERY SLEEP DEPRIVED ^_^     #
#													-By: Alnim  																	 #
######################################################################################################################################
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def style(style_type, text):
	return style_type + text

def end_style():
	return ENDC

def test_organism():
	print(style(HEADER, "---Start: Organism Class checking---"))
	erron = 0
	o = Organism()
	if (hasattr(o, "dmg") & hasattr(o, "hp")) == 0:
		print(style(WARNING, "Your organism class doesn't initialize properly"))
		return
	if o.hp != 35:
		erron += 1
		print(style(FAIL, "You don't initialize"
		" the organism's ") + style(UNDERLINE, "hp") + end_style() +
		style(FAIL, " to ") + style(BOLD,"35") + end_style())
	if o.dmg != 10:
		erron += 1
		print(style(FAIL, "You don't initialize"
		" the organism's ") + style(UNDERLINE, "dmg") + end_style() +
		style(FAIL, " to ") + style(BOLD,"10") + end_style())
	prev_hp = o.hp
	o.take_damage(10)
	if (prev_hp - o.hp) != 10:
		erron += 1
		print(style(FAIL, "The ") + style(UNDERLINE, "take_damage") + end_style() +
		style(FAIL, " method, doesn't modify the hp properly"))
	if erron == 0:
		print(style(OKGREEN, "Organism Class, perfect."))

def test_card():
	pass

def test_plant():
	print(style(HEADER, "---Start: Plant Class checking---"))
	erron = 0
	o = Plant()
	o2 = Plant()
	if (hasattr(o, "dmg") & hasattr(o, "hp")) == 0:
		print(style(WARNING, "Your Plant class doesn't inherit the properties of the Non_Plant"));
		return
	if hasattr(o, "powerup") == 0:
		print(style(WARNING, "You didn't initialize your ") + style(UNDERLINE, "Plant") + end_style() + style(WARNING, " class properly"));
		return
	if hasattr(o, "cost") == 0:
		print(style(WARNING, "You didn't create a " + style(UNDERLINE, "cost") + end_style() + style(WARNING, " class variable for your function")));
		return
	if(o.cost != 35):
		erron += 1
		print(style(FAIL, "You didn't initialize"
		" the plant classes ") + style(UNDERLINE, "cost") + end_style() +
		style(FAIL, " class variable to ") + style(BOLD,"35") + end_style())

	if o.powerup != 0:
		erron += 1
		print(style(FAIL, "You didn't initialize"
		" the plant's ") + style(UNDERLINE, "powerup") + end_style() +
		style(FAIL, " to ") + style(BOLD,"0") + end_style())
	prev_hp = o2.hp
	o.attack(o2)
	if (prev_hp - o2.hp) != (o.dmg + o.powerup):
		erron += 1
		print(style(FAIL, "The ") + style(UNDERLINE, "attack") + end_style() +
		style(FAIL, " method, doesn't reduce the nonplant's hp enough"))
	if iscard:
		c = Card(10)
		prev_powerup = o.powerup
		o.apply_powerup(c)
		if(o.powerup != prev_powerup + c.power):
			erron += 1
			print(style(FAIL, "The ") + style(UNDERLINE, "apply_powerup") + end_style() +
			style(FAIL, " method, doesn't increase the plant's powerup"))
	prev_powerup = o.powerup
	o.weaken_powerup()
	if(o.powerup != prev_powerup / 2):
			erron += 1
			print(style(FAIL, "The ") + style(UNDERLINE, "weaken_powerup") + end_style() +
			style(FAIL, " method, doesn't decrease the plant's powerup appropriately"))
	if erron == 0:
		print(style(OKGREEN, "Plant Class, perfect."))

def test_nonplant():
	print(style(HEADER, "---Start: Non_Plant Class checking---"))
	erron = 0
	o = Non_Plant()
	o2 = Non_Plant()
	if (hasattr(o, "dmg") & hasattr(o, "hp")) == 0:
		print(style(WARNING, "Your Non_Plant class doesn't inherit the properties of the Organism"));
		return
	if hasattr(o, "worth") == 0:
		print(style(WARNING, "You didn't create a " + style(UNDERLINE, "cost") + end_style() + style(WARNING, " class variable for your function")));
		return
	if o.hp != 80:
		erron += 1
		print(style(FAIL, "You didn't initialize"
		" the nonlplant's ") + style(UNDERLINE, "hp") + end_style() +
		style(FAIL, " to ") + style(BOLD,"80") + end_style())
	if o.dmg != 5:
		erron += 1
		print(style(FAIL, "You didn't initialize"
		" the nonplant's ") + style(UNDERLINE, "dmg") + end_style() +
		style(FAIL, " to ") + style(BOLD,"5") + end_style())
	prev_hp = o2.hp
	o.attack(o2)
	if (prev_hp - o2.hp) != (o.dmg):
		erron += 1
		print(style(FAIL, "The ") + style(UNDERLINE, "attack") + end_style() +
		style(FAIL, " method, doesn't reduce the plant's hp enough"))
	if erron == 0:
		print(style(OKGREEN, "Non_Plant Class, perfect."))

def test_card():
	print(style(HEADER, "---Start: Card Class checking---"))
	erron = 0
	o = Card(3.1415926535)
	if hasattr(o, "power") == 0:
		print(style(WARNING, "You didn't initialize your ") + style(UNDERLINE, "Card") + end_style() + style(WARNING, " class properly"));
		return
	if hasattr(o, "cost") == 0:
		print(style(WARNING, "You didn't create a " + style(UNDERLINE, "cost") + end_style() + style(WARNING, " class variable for your Card class")));
		return
	if o.cost != 5:
		erron += 1
		print(style(FAIL, "You didn't initialize"
		" the card's ") + style(UNDERLINE, "cost") + end_style() +
		style(FAIL, " to ") + style(BOLD,"5") + end_style())
	if o.power != 3.1415926535:
		erron += 1
		print(style(FAIL, "You didn't initialize"
		" the card's ") + style(UNDERLINE, "power") + end_style() +
		style(FAIL, " to ") + style(BOLD,"the value that's passed into the __init__ function") + end_style())
	if erron == 0:
		print(style(OKGREEN, "Card Class, perfect."))

def test_wave():
	print(style(HEADER, "---Start: Wave Class checking---"))
	erron = 0
	o = Wave(1, 2, 3)
	if (hasattr(o, "wave_num") & hasattr(o, "row") & hasattr(o, "num")) == 0:
		print(style(WARNING, "You didn't initialize your ") + style(UNDERLINE, "Wave") + end_style() + style(WARNING, " class properly"));
		return
	if o.wave_num != 1:
		erron += 1
		print(style(FAIL, "You didn't initialize"
		" the wave's ") + style(UNDERLINE, "wave_num") + end_style() +
		style(FAIL, " to ") + style(BOLD,"the value that's passed into the __init__ function for the 1st argument") + end_style())
	if o.row != 2:
		erron += 1
		print(style(FAIL, "You didn't initialize"
		" the wave's ") + style(UNDERLINE, "row") + end_style() +
		style(FAIL, " to ") + style(BOLD,"the value that's passed into the __init__ function for the 2nd argument") + end_style())
	if o.num != 3:
		erron += 1
		print(style(FAIL, "You didn't initialize"
		" the wave's ") + style(UNDERLINE, "num") + end_style() +
		style(FAIL, " to ") + style(BOLD,"the value that's passed into the __init__ function for the 3rd argument") + end_style())
	if erron == 0:
		print(style(OKGREEN, "Wave Class, perfect."))

def test_game(file=None):
	print(style(HEADER, "---Start: Game Class checking---"))
	if file == None:
		print(style(WARNING, "You need to pass in a valid example file to check the Game Class"))
		return
	erron = 0
	o = Game(file)
	for r in range(o.height):
		for c in range(o.width):
			if(type(o.board[r][c].peek()).__name__ != "Queue"):
				print(style(FAIL, "Your Board is not initialized properly" + str(o.board[r][c].peek())))
				return
	o.board[0][0].enqueue(Non_Plant())
	if erron == 0:
		print(style(OKGREEN, "Game Class, perfect."))

def testify(file):
	if isorganism:
		test_organism()
	if iscard:
		test_card()
		print()
	if isplant:
		test_plant()
		print()
	if isnonplant:
		test_nonplant()
	if iswave:
		test_wave()
	# if isgame:
	# 	test_game(file)
	if(isorganism == 0 and isnonplant == 0 and isplant == 0 and iscard == 0 and iswave == 0):
		print(style(WARNING, "You need to try some tests out ;/"))

import sys

if __name__ == "__main__":
	# if len(sys.argv) == 2:
		testify(None)
		end_style()
	# else:
	# 	print(style(WARNING, "You need to pass in a valid example file to check the Game Class"))
