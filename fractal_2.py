import turtle

# Настройки окна
window = turtle.Screen()
window.setup(800, 800, 0, 0)

def draw_fractal(ln):
    if ln > 50:
        ln3 = ln // 3
        draw_fractal(ln3)
        turtle.left(60)
        draw_fractal(ln3)
        turtle.right(120)
        draw_fractal(ln3)
        turtle.left(60)
        draw_fractal(ln3)
    else:
        turtle.fd(ln)
        turtle.left(60)
        turtle.fd(ln)
        turtle.right(120)
        turtle.fd(ln)
        turtle.left(60)
        turtle.fd(ln)
turtle.teleport(-350, 100)
turtle.ht()
draw_fractal(200)
turtle.right(120)
draw_fractal(200)
turtle.right(120)
draw_fractal(200)
window.exitonclick()
