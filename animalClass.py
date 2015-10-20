class animal:
	def __init__(self):
		self.name = "Dog"
		self.tail = "Yes"
		self.legs = "4"
		self.paws = "Yes"
		print("__init__ has been executed")

	def setname(self, name):
		self.name = name

	def print_name(self):
		print(self.name)

if __name__ == "__main__":
	x = animal()
	x.setname("Frog")
	x.print_name()



