class Student:
	def __init__(self,name,school):
		self.name = name
		self.school = school
		self.marks = []
	
	def average(self):
		return sum(self.marks)/len(self.marks)
	
	@classmethod
	def friend(cls, origin,friend_name,salary):
		return cls(friend_name,origin.school,salary)

	


class WorkingStudent(Student):

	def __init__(self,name,school,salary):
		super().__init__(name,school)
		self.salary = salary
		

anna = WorkingStudent("Anna","MIT",20)

arush = anna.friend(anna,"Arush",14.07)

print(arush.name)
print(arush.school)
print(arush.salary)
