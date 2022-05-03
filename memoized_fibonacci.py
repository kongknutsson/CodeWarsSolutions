def fibonacci(n, cached={}):
    if n in [0, 1]:
        return n
    if n in cached:
        return cached[n]
    else:
        cached[n] = fibonacci(n - 1, cached) + fibonacci(n - 2, cached)
    return cached[n]