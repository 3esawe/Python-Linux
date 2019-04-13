class Doctor(object):
	"""docstring for Doctor"""
	def __init__(self, name,salary):
		super(Doctor, self).__init__()
		self.name = name
		self.salary = salary
		self.hospitals = []
	def doublesalary(self):
		self.salary = self.salary * 2
	@property	
	def printName(self):
		return f"{self.name} {self.salary} is Doctor name"
	def __len__(self):
		return len(self.name)
	def __getitem__(self, i):
		return self.hospitals[i]

	def __reprt__(self):
		return f'<Doctor {self.hospitals}> '
	def __str__(self):
		return f'Doctor name len {len(self)} '
	@classmethod
	def Times(cls): # it's better than staticmethod 
		print("12123")
if __name__ == '__main__':
	doct = Doctor("Ali", 50)
	doct.hospitals.append("salmaniah")
	doct.doublesalary()
	c = doct.printName
	Doctor.Times()
	print(c)
	print(doct)
	print(doct)	
	