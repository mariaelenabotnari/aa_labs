import time

import pandas as pd
from matplotlib import pyplot as plt


def fibonacci(n):
    if n <= 1:
        return n

    fib = {0: 0, 1: 1}
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


if __name__ == '__main__':
    n_values = [10, 25, 50, 100, 250, 501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000]
    time_taken = []

    for n in n_values:
        repetitions = 10000
        start_time = time.perf_counter()
        for _ in range(repetitions):
            fibonacci(n)
        end_time = time.perf_counter()

        avg_time = (end_time - start_time) / repetitions
        time_taken.append(avg_time if avg_time > 0 else 1e-9)

    df = pd.DataFrame({"Input Size (n)": n_values, "Time Taken (seconds)": time_taken})
    print(df)

    plt.figure(figsize=(8, 5))
    plt.plot(n_values, time_taken, marker='o', linestyle='-', color='b', label="Execution Time")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Memoization Method for Fibonacci Sequence Execution Time")
    plt.legend()
    plt.grid(True)

    plt.show()
