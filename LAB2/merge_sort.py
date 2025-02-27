import random
import time

import pandas as pd
from matplotlib import pyplot as plt


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_array = array[:middle]
    right_array = array[middle:]

    left_array_sorted = merge_sort(left_array)
    right_array_sorted = merge_sort(right_array)

    return merge(left_array_sorted, right_array_sorted)

def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000]

#Negative numbers
# execution_times_negative = []
# for size in sizes:
#     array = [random.randint(-10**9, -10**6) for _ in range(size)]
#     start_time = time.time()
#     sorted_array_2 = merge_sort(array)
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
# plt.title('MergeSort Execution Time for Negative Numbers')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True)
# plt.legend()
# plt.show()

#Positive numbers
# execution_times_positive = []
# for size in sizes:
#     array = [random.randint(10**6, 10**9) for _ in range(size)]
#     start_time = time.time()
#     sorted_array = merge_sort(array)
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
# plt.title('MergeSort Execution Time for Positive Numbers')
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
    sorted_array_3 = merge_sort(array)
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
plt.title('MergeSort Execution Time for Decreasing Numbers')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.show()
