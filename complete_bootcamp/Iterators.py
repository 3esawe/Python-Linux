#custom for loop

def my_for(iters):
    iterator  = iter(iters)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break





#custom iterator

class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return self


    def __next__(self):
        if self.low < self.high:
            num = self.low
            self.low += 1
            return num
        raise StopIteration




#Genarator

def prime_numbers(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:
                break
            else:
                yield n

c = prime_numbers(15)

#fib_series

def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums
fib_numbers = fib_list(10)
print(fib_numbers)
