# Завдання 3. Порівняння алгоритмів сортування

import random
import timeit

from insertion_sort import insertion_sort
from merge_sort import merge_sort


# Кількість повторень та розміри тестових масивів
REPEAT_COUNT = 10
DATA_SIZES = [1000, 5000, 10000]


# Вимірює час сортування масиву.
# - sort_function: функція сортування
# - data: вхідний масив
# - repeat_count: кількість повторень
def measure_sort(sort_function, data: list[int], repeat_count: int) -> float:
    return timeit.timeit(
        lambda: sort_function(data[:]),
        number=repeat_count
    )



# Виконує тестування алгоритмів сортування та повертає результати.
# Результати містять час виконання кожного алгоритму для різних розмірів масивів.
def benchmark() -> dict[str, dict[int, float]]:
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Timsort (sorted)": sorted,
        "Timsort (sort)": lambda arr: (arr.sort(), arr)[1],
    }

    results = {name: {} for name in algorithms}

    rng = random.Random(55)

    for size in DATA_SIZES:
        data = [rng.randint(0, size) for _ in range(size)]
        expected = sorted(data)

        for name, algorithm in algorithms.items():
            # Перевіряємо правильність сортування
            assert algorithm(data[:]) == expected, (
                f"Помилка сортування: {name}"
            )

            # Вимірюємо час виконання
            elapsed = measure_sort(algorithm, data, REPEAT_COUNT)
            results[name][size] = elapsed

    return results



def main():
    results = benchmark()

    # Виводимо таблицю результатів
    print(f"Час виконання {REPEAT_COUNT} повторень (секунди)")
    print()

    header = f"{'Алгоритм':<20}"
    for size in DATA_SIZES:
        header += f" | {size:>12}"
    print(header)
    print("-" * len(header))

    for name, times in results.items():
        row = f"{name:<20}"
        for size in DATA_SIZES:
            row += f" | {times[size]:>12.5f}"
        print(row)

    # Порівнюємо зростання часу
    small_size = DATA_SIZES[0]
    large_size = DATA_SIZES[-1]

    print()
    print(f"Зростання часу ({small_size} -> {large_size}):")

    for name, times in results.items():
        ratio = times[large_size] / times[small_size]
        print(f"{name:<20}: {ratio:.2f}x")

if __name__ == "__main__":
    main()
