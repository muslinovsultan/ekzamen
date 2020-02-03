class CoffeeMachine:
	def __init__(self, milk,coffee,sugar):
		self.milk = milk
		self.coffee = coffee
		self.sugar = sugar
	def make_coffee(self,milk,coffee,sugar):
			if milk > self.milk and coffee > self.coffee and sugar > self.sugar:
				min = milk - self.milk
				min2 = coffee - self.coffee
				min3 = sugar - self.sugar
				print(f"Не достаточно \n молока-{min}\n кофе-{min2}\n сахара-{min3}")
			elif milk > self.milk and coffee > self.coffee and sugar < self.sugar:
				min = milk - self.milk
				min2 = coffee - self.coffee
				print(f"Не достаточно молока-{min} и кофе-{min2}")
			elif milk > self.milk and coffee < self.coffee and sugar > self.sugar:
				min = milk - self.milk
				min2 = coffee - self.coffee
				print(f"Не достаточно молока-{min} и сахара-{min2}")
			elif milk < self.milk and coffee > self.coffee and sugar > self.sugar:
				min = sugar - self.sugar
				min2 = coffee - self.coffee
				print(f"Не не достаточно кофе-{coffee} и сахара-{sugar}")
			elif milk > self.milk and coffee < self.coffee and sugar < self.sugar:
				min = milk - self.milk
				print(f"Не достаточно молока-{min}")
			elif milk < self.milk and coffee > self.coffee and sugar < self.sugar:
				min = coffee - self.coffee
				print(f"Не достаточно кофе-{min}")
			elif milk < self.milk and coffee < self.coffee and sugar > self.sugar:
				min = sugar - self.sugar	
				print(f"Не достаточно сахара-{min}")
			elif milk < self.milk and coffee < self.coffee and sugar < self.sugar:
				self.__substract_milk(milk)
				self.__substract_coffee(coffee)
				self.__subtsract_sugar(sugar)
				print(f"Кофе готов \nмолока-{self.milk}\nкофе-{self.coffee}\nсахара{self.sugar}")
	def __substract_milk(self,milk):
		self.milk -= milk	
	def __substract_coffee(self,coffee):
		self.coffee -= coffee
	def __subtsract_sugar(self,sugar):
		self.sugar -= sugar
def main():
	coffemachine = CoffeeMachine(1000,1000,1000)
	coffemachine.make_coffee(1111,2222,3333)
if __name__ == "__main__":
	main()
def main():
	coffemachine = CoffeeMachine(1000,1000,1000)
	coffemachine.make_coffee(222,444,666)
if __name__ == "__main__":
	main()


