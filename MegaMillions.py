

from breezypythongui import EasyFrame
from tkinter.font import Font
import random

class MegaMillions(EasyFrame):
	
	def __init__(self):
		"""sets up the window and widgets."""
		EasyFrame.__init__(self, title = "Mega Millions !", width = 420, height = 280, resizable = "False")
		titleFont = Font(family = "Arial", size = 20,)
		self.titleLabel = self.addLabel(text = "Mega Millions!",
			row = 0, column = 2, columnspan = 3, sticky = "NSEW", font = titleFont, 
			background = "SkyBlue", foreground = "DarkOrange")


		#Fields for the random numbers to appear
		self.numField1 = self.addIntegerField(value = 0, row = 1, column = 1, sticky = "NSEW")
		self.numField2 = self.addIntegerField(value = 0, row = 1, column = 2, sticky = "NSEW")
		self.numField3 = self.addIntegerField(value = 0, row = 1, column = 3, sticky = "NSEW")
		self.numField4 = self.addIntegerField(value = 0, row = 1, column = 4, sticky = "NSEW")
		self.numField5 = self.addIntegerField(value = 0, row = 1, column = 5, sticky = "NSEW")

		# Command Button
		self.drawButton = self.addButton(text = "DRAW!", row = 2, column = 2, columnspan = 3, command = self.draw)


		# Label for the output message
		self.outputLabel = self.addLabel(text = "", row = 3, column = 2, columnspan = 3,
		sticky = "NSEW", background = "SkyBlue", foreground = "DarkOrange", font = Font(family = "Arial",
		 size = 10))


	# Event handling method
	def draw(self):
		# Variables and constants
		num1 = random.randint(1, 70)
		num2 = random.randint(1, 70)
		num3 = random.randint(1, 70)
		num4 = random.randint(1, 70)
		num5 = random.randint(1, 70)

		# Caculation phase
		if num3 <= 25:
			result = "MEGA BALL!"
		elif num3 >= 26:
			result = "Sorry"





		# Output phase
		self.numField1.setNumber(num1)
		self.numField2.setNumber(num2)
		self.numField3.setNumber(num3)
		self.numField4.setNumber(num4)
		self.numField5.setNumber(num5)
		self.outputLabel["text"] = result

		














		# definition of the main() method for program entry
def main():
	"""Instantiates an object from the class in the graphics loop"""
	MegaMillions().mainloop() 

# global call to the main() method
if __name__ == "__main__":
	main()


