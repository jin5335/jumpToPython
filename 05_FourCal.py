class FourCal:

	def setdata(self, a, b):
		self.num1 = a
		self.num2 = b

	def sum(self):
		result = self.num1 + self.num2

		return result

	def sub(self):
		result = self.num1 - self.num2

		return result
k
	def mul(self):
		result = self.num1 * self.num2

		return result

	def div(self):
		result = self.num1/self.num2

		return result

a = FourCal()
a.setdata(2, 4)
print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())

type(a)
