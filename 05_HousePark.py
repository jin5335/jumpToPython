# 초기값 설정, 상속, 연산자 오버로#
# 초기값 설정 __init__ function
class HousePark:
	lastname = "박"

	def setname(self, name):
		self.fullname = self.lastname + name

	def travel(self, where):
		print("%s, %s가다" % (self.fullname, where))

pey = HousePark()
pey.setname("응용")
pey.travel("부산")

pey = HousePark()
pey.travel("부산")

class HousePark_addInit:
	lastname = "박"

	def __init__(self, name):
		self.fullname = self.lastname + name

	def travel(self, where):
		print("%s, %s가다" %(self.fullname, where))

pey = HousePark_addInit("응용")
pey.travel("부산")

# 상속(Inheritance)

class HouseKim(HousePark_addInit):
	lastname="김"

juliet = HouseKim("줄리엣")
juliet.travel("독도")

# Method overriding
# 상속받은 클래스의 method와 이름은 동일하지만, 다른 일을 하는 Method
# 즉, 상속받은 클래스의 method를 덮어쓴다.
# -> 상속을 받는 클래스를 정의할때, 같은 이름의 method를 재정의 해주면 된다.

class HouseKim_override(HousePark_addInit):
	lastname = "김"

	def travel(self, where, day):
		print("%s, %s여행 %d일 가네"  %(self.fullname, where, day))

juliet = HouseKim_override("줄리엣")
juliet.travel("독도", 3)

# 연산자 오버로딩(Operator overloading)
# +, -, *, / 등의 연산자를 객체 끼리도 가능하게 하는 것

class HousePark_overload:
	lastname = "박"

	def __init__(self, name):
		self.fullname = self.lastname + name

	def travel(self, where):
		print("%s, %s여행을 가다." %(self.fullname, where))

	def love(self, other):
		print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname))

	def __add__(self, other):   #operator 정의
		print("%s, %s 결혼했네" %(self.fullname, other.fullname))


class HouseKim_overload(HousePark_overload):
	lastname = "김"

	def travel(self, where, day):
		print("%s, %s여행을 %d일 가네." %(self.fullname, where, day))

pey = HousePark_overload("응용")
juliet = HouseKim_overload("줄리엣")
pey + juliet

# final

class HousePark_final:
	lastname = "박"

	def __init__(self, name):
		self.fullname = self.lastname + name

	def travel(self, where):
		print("%s, %s여행을 가다." %(self.fullname, where))

	def love(self, other):
		print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname))

	def fight(self, other):
		print("%s, %s 싸우네" %(self.fullname, other.fullname))

	def __add__(self, other):
		print("%s, %s 결혼했네" %(self.fullname, other.fullname))

	def __sub__(self, other):
		print("%s, %s 이혼했네" %(self.fullname, other.fullname))

class HouseKim_final(HousePark_final):
	lastname = "김"

	def travel(self,where, day):
		print("%s, %s여행을 %d일 가다" %(self.fullname, where, day))

pey = HousePark_final("응용")
juliet = HouseKim_final("줄리엣")
pey.travel("부산")
juliet.travel("독도", 3)
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet
