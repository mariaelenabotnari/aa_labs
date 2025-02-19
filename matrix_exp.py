import time

from matplotlib import pyplot as plt
import pandas as pd


def multiply_matrix(a, b):
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
    ]

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2)
        return multiply_matrix(half, half)
    else:
        return multiply_matrix(matrix, matrix_power(matrix, n - 1))

def fibonacci(n):
    if n <= 1:
        return n
    base_matrix = [[1, 1], [1, 0]]
    result = matrix_power(base_matrix, n - 1)
    return result[0][0]

if __name__ == '__main__':
    n_values = [10, 25, 50, 100, 250, 501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
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
    plt.title("Matrix Exponentiation for Fibonacci Sequence Execution Time")
    plt.legend()
    plt.grid(True)

    plt.show()