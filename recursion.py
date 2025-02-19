import time

import pandas as pd
from matplotlib import pyplot as plt


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    n_values = [5, 7, 10, 12, 15, 17, 27, 30]
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
    plt.title("Recursive Method for Fibonacci Sequence Execution Time")
    plt.legend()
    plt.grid(True)

    plt.show()
