import another_module

from turtle import Turtle, Screen
#
# print(another_module.another_variable)
#
# #creating a new object
# timmy = Turtle()
# print(timmy)
#
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("blue2")
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Ipswich Player names", "Type"]
table.add_rows(
    [
        ["Conor Chaplin", "Forward"],
        ["Freddie Ladapo", "Forward"],
        ["Leif Davis", "Left Back"]
    ]
)
table.align ="r"
print(table)

