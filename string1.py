import turtle

name = turtle.textinput("name","what is your name?")
name = name.lower()
if name.startswith("mr"):
    print("Hello Sir,how are you")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello Madam,how are you")
else :
    name = name.capitalize()
    s = "Hi" + "name" + "!How are you?"
    print(s)

turtle.exitonclick()