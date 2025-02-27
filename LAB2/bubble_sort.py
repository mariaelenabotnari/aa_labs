import random
import time

import pandas as pd
from matplotlib import pyplot as plt


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

sizes = [400, 800, 1000, 2000, 2500, 3000, 5000, 7000, 10000]

#Positive numbers
# execution_times_positive = []
# for size in sizes:
#     array = [random.randint(10**6, 10**9) for _ in range(size)]
#     start_time = time.time()
#     sorted_array = bubble_sort(array)
#     end_time = time.time()
#     execution_times_positive.append(end_time - start_time)
#
# plt.figure(figsize=(10, 5))
#
# plt.plot(sizes, execution_times_positive, marker='o', linestyle='-', label='Positive Numbers')
#
# for i, txt in enumerate(execution_times_positive):
#     plt.annotate(f"{sizes[i]}: {txt:.6f}", (sizes[i], execution_times_positive[i]),
#                  textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
#
# df = pd.DataFrame({"Array size (n)": sizes, "Time Taken (seconds)": execution_times_positive})
# print("\nFinal Execution Time Table:\n", df)
#
# plt.xlabel('Array Size')
# plt.ylabel('Execution Time (seconds)')
# plt.title('BubbleSort Execution Time for Positive Numbers')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True)
# plt.legend()
# plt.show()

#Negative numbers
# execution_times_negative = []
# for size in sizes:
#     array = [random.randint(-10**9, -10**6) for _ in range(size)]
#     start_time = time.time()
#     sorted_array_2 = bubble_sort(array)
#     end_time = time.time()
#     execution_times_negative.append(end_time - start_time)
#     print(f"Array size: {size}, Execution time for negative numbers: {end_time - start_time:.6f} seconds")
#
# plt.figure(figsize=(10, 5))
#
# plt.plot(sizes, execution_times_negative, marker='o', linestyle='-', label='Negative Numbers')
#
# for i, txt in enumerate(execution_times_negative):
#     plt.annotate(f"{sizes[i]}: {txt:.6f}", (sizes[i], execution_times_negative[i]),
#                  textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
#
# df = pd.DataFrame({"Array size (n)": sizes, "Time Taken (seconds)": execution_times_negative})
# print("\nFinal Execution Time Table:\n", df)
#
# plt.xlabel('Array Size')
# plt.ylabel('Execution Time (seconds)')
# plt.title('Bubble Sort Execution Time for Negative Numbers')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True)
# plt.legend()
# plt.show()

#Decreasing numbers
execution_times_decreasing = []
for size in sizes:
    array = [random.randint(10**6, 10**9) for _ in range(size)]
    array.sort(reverse=True)
    start_time = time.time()
    sorted_array_3 = bubble_sort(array)
    end_time = time.time()
    execution_times_decreasing.append(end_time - start_time)

plt.figure(figsize=(10, 5))

plt.plot(sizes, execution_times_decreasing, marker='o', linestyle='-', label='Decreasing Numbers')

for i, txt in enumerate(execution_times_decreasing):
    plt.annotate(f"{sizes[i]}: {txt:.6f}", (sizes[i], execution_times_decreasing[i]),
                 textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

df = pd.DataFrame({"Array size (n)": sizes, "Time Taken (seconds)": execution_times_decreasing})
print("\nFinal Execution Time Table:\n", df)

plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Bubble Sort Execution Time for Decreasing Numbers')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.show()