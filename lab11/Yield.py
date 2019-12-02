def fibo(n):
    yield 1
    if n > 0:
        yield 1
        if n > 1:
            prev = 1
            prevprev = 1
            for i in range(n-2):
                num = prevprev+prev
                prevprev = prev
                yield num
                prev = num

n = int(input())
fib = fibo(n)
for i in range(n):
    print(next(fib))