def fib(n, memo = {}):
    if n == 1 or n == 0:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib(n-1) + fib(n-2)
        memo[n] = result
        return result


print(fib(100))
