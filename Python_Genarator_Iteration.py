class Genarator:
    """docstring for ."""
    def __init__(self):
        self.number = 0
    def prime(self, bound):
        for n in range(2,bound):
            for x in range(2,n):
                if n % x == 2:
                    break
                else:
                    yield n
primex = Genarator()
print(primex.prime(20))
