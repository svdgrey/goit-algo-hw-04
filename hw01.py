# Завдання 1. Сортування файлів за розширеннями

import argparse
import shutil
from pathlib import Path


# Рекурсивно відображає структуру директорії.
# - path: шлях до директорії, яку потрібно відобразити
# - level: поточний рівень вкладеності
def show_directory(path: Path, level: int = 0):
    try:
        for item in sorted(path.iterdir()):
            indent = "   " * level

            try:
                if item.is_dir():
                    print(indent + item.name + "/")
                    show_directory(item, level + 1)
                else:
                    print(indent + item.name)

            except OSError as error:
                print(f"Помилка обробки {item}: {error}")

    except OSError as error:
        print(f"Помилка читання директорії {path}: {error}")




# Повертає унікальний шлях до файлу, додаючи числовий суфікс у разі збігу імен.
# - target_file: початковий шлях до файлу
def get_unique_path(target_file: Path) -> Path:
    counter = 1
    unique_path = target_file

    while unique_path.exists():
        unique_path = target_file.with_name(
            f"{target_file.stem} ({counter}){target_file.suffix}"
        )
        counter += 1

    return unique_path



# Копіює файли з вихідної директорії до директорії призначення.
# Створює піддиректорії за розширеннями файлів та копіює файли до відповідних піддиректорій.
#
# ПРИМІТКА 1: в умові завдання не уточнено, як обробляти файли без розширення,
# тому такі файли копіюються безпосередньо до директорії призначення.
#
# ПРИМІТКА 2: якщо вихідні файли мають однакові імена та розширення,
# до наступних копій додається порядковий номер, щоб уникнути перезапису.
#
# - source: шлях до вихідної директорії
# - destination: шлях до директорії призначення
def copy_files(source: Path, destination: Path):

    try:
        for item in source.iterdir():
            try:
                if item.is_dir():
                    copy_files(item, destination)

                elif item.is_file():
                    extension = item.suffix.lower().lstrip(".")
                    target_dir = destination / extension if extension else destination
                    target_dir.mkdir(parents=True, exist_ok=True)

                    target_file = get_unique_path(target_dir / item.name)
                    shutil.copy2(item, target_file)

                    print(f"Скопійовано: {item} -> {target_file}")

            except OSError as error:
                print(f"Помилка обробки {item}: {error}")

    except OSError as error:
        print(f"Помилка читання директорії {source}: {error}")


def main():
    parser = argparse.ArgumentParser( description="Рекурсивне сортування файлів за розширеннями по субдиректоріях" )

    parser.add_argument( "source", type=Path, help="Шлях до вихідної директорії" )
    parser.add_argument( "destination", type=Path, nargs="?", default=Path("dist"), 
        help="Шлях до директорії призначення (за замовчуванням dist)"
    )
    args = parser.parse_args()

    source = args.source.resolve()
    destination = args.destination.resolve()

    if not source.is_dir():
        print(f"Вихідна директорія не існує: {source}")
        return

    if destination.is_relative_to(source):
        print("Директорія призначення не може бути всередині вихідної")
        return

    try:

        print(f"Вихідна директорія: {source}")
        show_directory(source)
        print()

        print("Копіювання файлів...")
        destination.mkdir(parents=True, exist_ok=True)
        copy_files(source, destination)
        print("Копіювання файлів завершено\n")

        print(f"Директорія призначення: {destination}")
        show_directory(destination)
        print()
    except OSError as error:
        print(f"Помилка: {error}")


if __name__ == "__main__":
    main()
