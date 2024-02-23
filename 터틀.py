import turtle
t= turtle.Pen()

while True:
    direction = input("왼쪽 = left, 오른쪽 = righ")
    if direction == "left":
        t.left(60)
        t.forward(50)

    if direction == "rieght":
        t.riht(60)
        t.forward(50)
    
