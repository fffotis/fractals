import turtle

# Функция для рисования треугольника
def draw_triangle(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)

# Функция для создания фрактала
def draw_fractal(length, depth):
    if depth == 0:
        draw_triangle(length)
    else:
        length /= 2
        draw_fractal(length, depth - 1)
        turtle.forward(length)
        draw_fractal(length, depth - 1)
        turtle.backward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.right(60)
        draw_fractal(length, depth - 1)
        turtle.left(60)
        turtle.backward(length)
        turtle.right(60)

# Настройки Turtle
turtle.speed(0)
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

# Задайте длину и глубину фрактала
initial_length = 400
fractal_depth = 6

# Нарисуем фрактал
draw_fractal(initial_length, fractal_depth)

# Завершим работу при клике
turtle.exitonclick()
