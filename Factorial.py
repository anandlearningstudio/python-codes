

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

fact_5 = factorial(5)
print (fact_5)