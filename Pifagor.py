import turtle


def draw_pifagoras_tree(t, size, level):
    if level == 0:
        return
    t.forward(size)
    t.left(45)
    draw_pifagoras_tree(t, size * 0.707, level - 1)
    t.right(90)
    draw_pifagoras_tree(t, size * 0.707, level - 1)
    t.left(45)
    t.backward(size)


def main():
    # Створення вікна та об'єкту черепахи
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.color("green")
    t.speed(0)

    # Ввід рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії (рекомендовано до 10): "))

    # Позиціонування черепахи та малювання фрактала
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    draw_pifagoras_tree(t, 100, level)

    # Закриваємо вікно при натисканні на нього
    window.exitonclick()


if __name__ == "__main__":
    main()
