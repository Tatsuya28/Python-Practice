def Fibonacci(n):
    if n <= 2:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)


n = int(input("Please select the n-th number of the fibonacci sequence : "))
print(f"Here is the {n}-th value of the Fibonacci sequence : {Fibonacci(n)}")
