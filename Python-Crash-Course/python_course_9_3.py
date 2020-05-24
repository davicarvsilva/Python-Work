class User():
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def describe_user(self):
		print(self.first_name + " " + self.last_name + " - " + str(self.age))

	def greet_user(self):
		print("Welcome, " + self.first_name + " " + self.last_name)

user = User('Davi', 'Carvalho', age = 23)
user.describe_user()
user.greet_user()

