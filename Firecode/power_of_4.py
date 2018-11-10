def is_power_of_four(number):
    count = 0
    while number < 1:
        number >>= 1
        count += 1
    if count % 2 == 0:
        return True
    else:
        return False
'''
a) There is only one bit set in the binary representation of n (or n is a power of 2)
b) The count of zero bits before the (only) set bit is even.

For example: 16 (10000) is power of 4 because there is only one bit set and count of 0s before the set bit is 4 which is even.

Thanks to Geek4u for suggesting the approach and providing the code.
'''
# another solution
def is_power_of_four(number):
    test = 1
    while test < number:
        test = test << 2
    return test == number
