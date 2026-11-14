
from pathlib import Path

import matplotlib.pyplot as plt

from hw03 import benchmark

CHARTS_DIR = Path(__file__).resolve().parent / "charts"

# Будує графік часу виконання алгоритмів.
# - results: результати вимірювань часу сортування (повертає функція benchmark із hw03)
def plot_execution_time(results: dict[str, dict[int, float]]):
    plt.figure(figsize=(10, 6))

    for name, times in results.items():
        sizes = sorted(times)
        values = [times[size] for size in sizes]
        plt.plot(sizes, values, marker="o", label=name)

    plt.yscale("log")
    plt.xlabel("Кількість елементів")
    plt.ylabel("Час виконання (секунди)")
    plt.title("Порівняння часу виконання алгоритмів")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "sorting_performance.png", dpi=150)
    plt.close()


# Будує графік зростання часу виконання алгоритмів.
# - results: результати вимірювань часу сортування (повертає функція benchmark із hw03)
def plot_growth(results: dict[str, dict[int, float]]):
    sizes = sorted(next(iter(results.values())))
    small_size = sizes[0]
    large_size = sizes[-1]

    names = list(results)
    ratios = [
        results[name][large_size] / results[name][small_size]
        for name in names
    ]

    plt.figure(figsize=(10, 6))
    plt.bar(names, ratios)

    plt.ylabel("Коефіцієнт зростання")
    plt.title(f"Зростання часу виконання ({small_size} -> {large_size})")
    plt.xticks(rotation=15)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "sorting_growth.png", dpi=150)
    plt.close()


def main():
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    results = benchmark()

    plot_execution_time(results)
    plot_growth(results)

    print(f"Графіки збережено в директорії: {CHARTS_DIR}")


if __name__ == "__main__":
    main()

