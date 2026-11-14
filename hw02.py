# Завдання 2. Сніжинка Коха

import turtle

# Рекурсивно малює криву Коха.
# - t: об'єкт Turtle для малювання
# - level: кількість рівнів рекурсії, що залишилися
# - length: довжина відрізка
def koch_curve(t: turtle.Turtle, level: int, length: float):
    if level == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, level - 1, length / 3)
            t.left(angle)


# Малює сніжинку Коха із заданою глибиною рекурсії.
# - level: глибина рекурсії
# - length: довжина сторони початкового трикутника
def draw_koch_snowflake(level: int, length: float = 500):
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")
    screen.tracer(100, 0)

    t = turtle.Turtle()
    
    t.hideturtle()

    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, level, length)
        t.right(120)

    
    screen.update()
    screen.mainloop()


def main():
    
    try:
        level = int(input("Введіть рівень рекурсії (рекомендація 0-5): "))

        if level < 0:
            print("Рівень рекурсії не може бути від'ємним")
            return

        draw_koch_snowflake(level)

    except ValueError:
        print("Помилка: введіть ціле число")


if __name__ == "__main__":
    main()
