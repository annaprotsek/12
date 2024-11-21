import turtle

def decode_and_execute(commands):
    for command in commands:
        if command == 'F': 
            turtle.forward(50)
        elif command == 'L': 
            turtle.left(90)
        elif command == 'R':
            turtle.right(90)
        elif command == 'U':
            turtle.penup()
        elif command == 'D': 
            turtle.pendown()

def main_turtle():
 
    commands = input("Введіть команди (F, L, R, U, D): ").upper()
    turtle.speed(1) 
    decode_and_execute(commands)
    turtle.done()

if __name__ == "__main__":
    main_turtle()
