import turtle

pen = turtle.Turtle()
pen.pencolor("blue")
pen.pensize(2)

def draw_letter(letter):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.circle(0)
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.write(letter, align="center", font=("Arial", 24, "bold"))

initials = "AB"
for letter in initials:
    draw_letter(letter)
    pen.forward(150)

turtle.done()