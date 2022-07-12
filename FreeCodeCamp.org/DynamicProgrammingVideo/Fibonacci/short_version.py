# Memoization
def Fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = Fibonacci(n - 1, memo) + Fibonacci(n - 2, memo)
    return memo[n]


n = int(input("Please select the n-th number of the fibonacci sequence : "))
print(f"Here is the {n}-th value of the Fibonacci sequence : {Fibonacci(n)}")
