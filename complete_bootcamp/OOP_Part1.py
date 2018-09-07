class User:
    online_users  = 0
    def __init__(self, first, last):
        self.first = first
        self._last = last
        User.online_users += 1
    @classmethod
    def display_active(cls):
        return f"{cls.online_users}"
    @classmethod
    def user_from_string(cls,string):
        first, last = string.split(",")
        return cls(first,last)
    def full_name(self):
        return User("ali","bani-essa")
    def __repr__(self):
        return f"{self.first} {self._last}"
user1 = User("omar","ali")
user2 = user1.full_name()
print(user2.first)
user3 = User.user_from_string("omar,ali")
print(user3)
print(User.display_active())
