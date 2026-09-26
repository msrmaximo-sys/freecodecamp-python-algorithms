def fibonacci(n):
    sequence = [0, 1]
    for x in range(n - 1):
     num = sequence[-2] + sequence[-1]
     sequence.append(num)
    return sequence[n]
