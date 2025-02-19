import time

import pandas as pd
from matplotlib import pyplot as plt


def iterative_fibonacci(n):
    if (n <= 1):
        return n
    one_step_back = 0
    current = 0

    for i in range(n):
        two_steps_back = one_step_back
        one_step_back = current
        current = two_steps_back + one_step_back
    return current

if __name__ == '__main__':
    n_values = [10, 25, 50, 100, 250, 501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
    time_taken = []

    for n in n_values:
        repetitions = 10000
        start_time = time.perf_counter()
        for _ in range(repetitions):
            iterative_fibonacci(n)
        end_time = time.perf_counter()

        avg_time = (end_time - start_time) / repetitions
        time_taken.append(avg_time if avg_time > 0 else 1e-9)

    df = pd.DataFrame({"Input Size (n)": n_values, "Time Taken (seconds)": time_taken})
    print(df)

    plt.figure(figsize=(8, 5))
    plt.plot(n_values, time_taken, marker='o', linestyle='-', color='b', label="Execution Time")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Iterative approach for Fibonacci Sequence Execution Time")
    plt.legend()
    plt.grid(True)

    plt.show()


