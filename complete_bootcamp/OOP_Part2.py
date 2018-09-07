class Animal:
    def __init__(self, name, color, age):
        self._name = name
        self.color = color
        self.age = age
    cool = True
    def __repr__(self):
        return f"{self.name} color: {self.color}"

    def __add__(self, other):
        if isinstance(other, Animal):
            return Animal(name="hussan", color="white", age=0)
    def make_noise(self, sound):
        print(f"this animal is {sound}")

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if value.startswith("G"):
            self._name = value
class Cat(Animal):
    def __init__(self,name,color,age, sound, tall):
        super().__init__(name,color,age)
        self.sound = sound
        self.tall = tall
    def sound(self):
        return f"miaw miwa {self.sound}"
blue = Cat("jack","white",5,"waka","4ft")
c = Cat("rex", "black", 7,"maa", "4ft")
w = blue + c
print(w)
print(blue)
print(blue.sound)
