import sys
import traceback
import os.path

isorganism = 1
isnonplant = 1
isplant = 1
iscard = 1
iswave = 1
isgame = 1

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

def print_traceback_error():
		print(FAIL)
		traceback.print_exc()
		print(ENDC)

file_import_errors_msg = "############################################\n""#                  ERRORS                  #\n""############################################"
print(FAIL + file_import_errors_msg)
try: 
	from organism import Organism
except ImportError:
	isorganism = 0
	print(style(HEADER, "---Found: Organism Class Errors---"), end="")
	if(os.path.isfile("organism.py") == True):
		print_traceback_error()
	else:
		print(style(WARNING, "\nCan't find the organism.py file"))
	
try: 
	from plant import Plant
except ImportError:
	isplant = 0
	print(style(HEADER, "---Found: Plant Class Errors---"), end="")
	if(isorganism == 0):
		print(style(OKBLUE, "\nThis class won't work without the Organism Class working fine ^_^"))
	elif(os.path.isfile("plant.py") == True):
		print_traceback_error()
	else:
		print(style(WARNING, "\nCan't find the plant.py file"))
try: 
	from non_plant import Non_Plant
except ImportError:
	isnonplant = 0
	print(style(HEADER, "---Found: Non_Plant Class Errors---"), end="")
	if(isorganism == 0):
		print(style(OKBLUE, "\nThis class won't work without the Organism Class working fine ^_^"))
	elif(os.path.isfile("non_plant.py") == True):
		print_traceback_error()
	else:
		print(style(WARNING, "\nCan't find the non_plant.py file"))
try:  
	from card import Card
except ImportError:
	print(style(HEADER, "---Found: Card Class Errors---"), end="")
	if(os.path.isfile("card.py") == True):
		print_traceback_error()
	else:
		print(style(WARNING, "\nCan't find the card.py file"))
	iscard = 0
try: 
	from wave import Wave
except ImportError:
	print(style(HEADER, "---Found: Wave Class Errors---"), end="")
	if(os.path.isfile("wave.py") == True):
		print_traceback_error()
	else:
		print(style(WARNING, "\nCan't find the wave.py file"))
	iswave = 0
try: 
	from game import Game
except ImportError:
	isgame = 0
	print(style(HEADER, "---Found: Game Class Errors---"), end="")
	if((isorganism & isnonplant & isplant & iswave & iscard) == 0):
		print(style(OKBLUE, "\nThis class won't work without the other classes working fine ^_^"))
	elif(os.path.isfile("game.py") == True):
		print_traceback_error()
	else:
		print(style(WARNING, "\nCan't find the game.py file"))
	
######################################################################################################################################
#																																	 #
# DON'T COPY THIS STYLE OF CODE, ITS BADLY WRITTEN CODE. BECUASE THIS WAS WRITTEN IN LESS THAN A DAY AND VERY SLEEP DEPRIVED ^_^     #
#													-By: Alnim  																	 #
######################################################################################################################################

	
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
	if hasattr(o, "take_damage") == 1:
		o.take_damage(10)
		if (prev_hp - o.hp) != 10:
			erron += 1
			print(style(FAIL, "The ") + style(UNDERLINE, "take_damage") + end_style() + 
			style(FAIL, " method, doesn't modify the hp properly"))
	else:
		erron += 1
		print(style(FAIL, "No ") + style(UNDERLINE, "take_damage") + end_style() + 
		style(FAIL, " method in class"))
		
	if erron == 0:
		print(style(OKGREEN, "Organism Class, perfect."))
	
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
	if hasattr(o, "attack") == 1:
		o.attack(o2)
		if (prev_hp - o2.hp) != (o.dmg + o.powerup):
			erron += 1
			print(style(FAIL, "The ") + style(UNDERLINE, "attack") + end_style() + 
			style(FAIL, " method, doesn't reduce the nonplant's hp enough"))
	else:
		erron += 1
		print(style(FAIL, "No ") + style(UNDERLINE, "attack") + end_style() + 
		style(FAIL, " method in class"))
		
	if iscard:
		c = Card(10)
		prev_powerup = o.powerup
		if hasattr(o, "apply_powerup") == 1:
			o.apply_powerup(c)
			if (o.powerup != prev_powerup + c.power):
				erron += 1
				print(style(FAIL, "The ") + style(UNDERLINE, "apply_powerup") + end_style() + 
				style(FAIL, " method, doesn't increase the plant's powerup"))
		else:
			erron += 1
			print(style(FAIL, "No ") + style(UNDERLINE, "apply_powerup") + end_style() + 
			style(FAIL, " method in class"))
	else:
		erron += 1
		print(style(FAIL, "Make a ") + style(UNDERLINE, "Card") + end_style() + 
		style(FAIL, " class then we'll test the apply_powerup method"))


	prev_powerup = o.powerup
	if hasattr(o, "weaken_powerup") == 1:
		o.weaken_powerup()
		if(o.powerup != prev_powerup / 2):
			erron += 1
			print(style(FAIL, "The ") + style(UNDERLINE, "weaken_powerup") + end_style() + 
			style(FAIL, " method, doesn't decrease the plant's powerup appropriately"))
	else:
		erron += 1
		print(style(FAIL, "No ") + style(UNDERLINE, "weaken_powerup") + end_style() + 
		style(FAIL, " method in class"))
		
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
	if hasattr(o, "attack") == 1:
		o.attack(o2)
		if (prev_hp - o2.hp) != (o.dmg):
			erron += 1
			print(style(FAIL, "The ") + style(UNDERLINE, "attack") + end_style() + 
			style(FAIL, " method, doesn't reduce the plant's hp enough"))
	else:
		erron += 1
		print(style(FAIL, "No ") + style(UNDERLINE, "attack") + end_style() + 
		style(FAIL, " method in class"))
		
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
class UT_game():
	def is_nonplant(o):
		if(o.is_nonplant(0, 0) == False):
			print(style(FAIL, "The " + style(UNDERLINE, "is_nonplant") + end_style() + 
			style(FAIL, " method doesn't work") + end_style()))
	def is_plant(o):
		if(o.is_plant(1, 1) == False):
			print(style(FAIL, "The " + style(UNDERLINE, "is_plant") + end_style() + 
			style(FAIL, " method doesn't work") + end_style()))
			return 1
		return 0

	def remove(o, old_cash):
		if(o.is_nonplant(0, 0) == True):
			print(style(FAIL, "The " + style(UNDERLINE, "remove") + end_style() + 
			style(FAIL, " method doesn't work") + end_style()))
		if(o.cash - old_cash != Non_Plant.worth):
			print(style(FAIL, "The " + style(UNDERLINE, "remove") + end_style() + 
			style(FAIL, " method doesn't lower the amount of cash...(also make sure you decrease the nonplants counter by one if a nonplant is removed)") + end_style()))
	
	def place_plant(o):
		row, col = 1, 2
		old_cash = o.cash
		func_name = style(UNDERLINE, "place_plant")
		fail_str = style(FAIL, "The " + func_name + end_style() + ' ' + FAIL +  "{}" +  end_style())
		o.place_plant(row, col)
		if o.is_plant(row, col):
			if old_cash < 35:
				msg = "method doesn't check if the player has enough cash"
				print(fail_str.format(msg))
			if old_cash == o.cash:
				msg = "method doesn't decrement the player's cash when placing a plant"
				print(fail_str.format(msg))
			if old_cash - o.cash != Plant.cost:
				msg = "method doesn't take away the right amount of player cash"
				print(fail_str.format(msg))

		row, col = 0, o.width - 1
		o.cash += 35;
		old_cash = o.cash
		o.place_plant(row, col)
		if o.is_plant(row, col):
			msg	= "method allows placement of plant in the last column"
			print(fail_str.format(msg))
		if o.cash != old_cash:
			msg = "method removed money even though you shouldn't place a plant in the last column"
		o.cash += 70;
		row, col = 1, 1
		o.place_plant(row, col)
		old_cash = o.cash
		o.place_plant(row, col)
		q = o.board[row][col]
		q2 = o.board[2][2]
		if hasattr(q, "size"):
			if q.size() == 2:
				msg = "method doesn't check if a plant already occupies the space"
				print(fail_str.format(msg))
			old_size = q2.size()
			o.place_plant(2,2)
			o.cash += 35
			if(q2.size() != old_size + 1):
				msg = "doesn't add one plant to the queue"
				print(fail_str.format(msg))

		else:
			msg = "uses a Queue without a size() method"
			print(fail_str.format(msg))
		if old_cash > o.cash:
			msg = "method removed cash even though you shouldn't place a plant on another plant"
			print(fail_str.format(msg))
	
	def place_nonplant(o, row):
		if(o.is_nonplant(row, o.width - 1) == False):
			print(style(FAIL, "The " + style(UNDERLINE, "nonplant") + end_style() + 
			style(FAIL, " method doesn't work") + end_style()))

	msg_dead = "No Tests for this, yer on yer own ;P"
	
	def place_wave():
		print(style(OKBLUE, "place_wave: " + UT_game.msg_dead))
	
	def plant_turn():
		print(style(OKBLUE, "plant_turn: " + UT_game.msg_dead))
		
	def nonplant_turn():
		print(style(OKBLUE, "nonplant_turn: " + UT_game.msg_dead))

	def run_turn():
		print(style(OKBLUE, "plant_turn: " + UT_game.msg_dead))
		
	def draw_card(o):
		old_cash = o.cash
		o.draw_card()
		if old_cash - o.cash != Card.cost:
			print(style(FAIL, "The " + style(UNDERLINE, "draw_card") + end_style() + 
			style(FAIL, " method doesn't work") + end_style()))
		old_cash = o.cash = 3
		o.draw_card()
		if old_cash != o.cash:
			print(style(FAIL, "The " + style(UNDERLINE, "draw_card") + end_style() + 
			style(FAIL, " method doesn't work") + end_style()))

			

def test_game(file=None):
	print(style(HEADER, "---Start: Game Class checking---"))
	if file == None:
		print(style(WARNING, "You need to pass in a valid example file to check the Game Class"))
		return
	erron = 0
	o = Game(file)
	w = Wave(0, 0, 0)
	for r in range(o.height):
		for c in range(o.width):
			if(type(o.board[r][c]).__name__ != "Queue"):
				print(style(FAIL, "Your Board is not initialized properly"))
				return
	o.board[0][0].enqueue(Non_Plant())
	if (hasattr(o, "is_nonplant")) == 1:
		UT_game.is_nonplant(o)
	else:
		print(style(WARNING, "No is_nonplant method in class"))
		erron += 1
	o.board[1][1].enqueue(Plant())
	
	if (hasattr(o, "is_plant")) == 1:
		erron += UT_game.is_plant(o)
	else:
		print(style(WARNING, "No is_plant method in class"))
		erron += 1
	old_cash = o.cash
	
	if (hasattr(o, "is_nonplant") & hasattr(o, "remove")) == 1:
		o.remove(0, 0)
		UT_game.remove(o, old_cash)
	else:
		print(style(WARNING, "No remove method in class"))
		erron += 1
	
	if (hasattr(o, "place_plant") & hasattr(o, "is_plant")) == 1:
		UT_game.place_plant(o)
	else:
		erron += 1
		print(style(WARNING, "No place_plant method in class"))
		
	if (hasattr(o, "place_nonplant")) == 1:
		o.place_nonplant(0)
		UT_game.place_nonplant(o, 0)
	else:
		erron += 1
		print(style(WARNING, "No place_nonplant method in class"))
		
	if (hasattr(o, "place_wave")) == 1:
		UT_game.place_wave()
	else:
		erron += 1
		print(style(WARNING, "No place_wave method in class"))
		
	if (hasattr(o, "plant_turn")) == 1:
		UT_game.plant_turn()
	else:
		erron += 1
		print(style(WARNING, "No plant_turn method in class"))
		
	if (hasattr(o, "nonplant_turn")) == 1:
		UT_game.nonplant_turn()
	else:
		erron += 1
		print(style(WARNING, "No nonplant_turn method in class"))
		
	if (hasattr(o, "run_turn")) == 1:
		UT_game.run_turn()
	else:
		erron += 1
		print(style(WARNING, "No run_turn method in class"))
		
	if (hasattr(o, "draw_card")) == 1:
		UT_game.draw_card(o)
	else:
		erron += 1
		print(style(WARNING, "No draw_card method in class"))
		
	if erron == 0:
		print(style(OKGREEN, "Game Class, within tests perfect! Otherwise...good luck with the last 4 functions!!"))
	else:
		print(style(OKBLUE, "\n--------(:P for the lack of error details ^_^)"))
		print(style(WARNING, "--------∆ IF YOU GET ALOT OF UNEXPECTED ERRORS, MAKE SURE YOU PROPERLY COPIED AND PASTED THE CODE GIVEN TO YOU #_#") + end_style())
		
def testify(file):
	if isorganism:
		test_organism()
		print()
	if iscard:
		test_card()
		print()
	if isplant:
		test_plant()
		print()
	if isnonplant:
		test_nonplant()
		print()
	if iswave:
		test_wave()
		print()
	if isgame:
		test_game(file)
		print()

start_tests_msg = "############################################\n""#                   TESTS                  #\n""############################################"
if __name__ == "__main__":
	if len(sys.argv) == 2:
		print(OKGREEN + start_tests_msg)
		testify(sys.argv[1])
		end_style()
	else:
		print(style(WARNING, "You need to pass in a valid example file to check the Game Class"))
	end_style()