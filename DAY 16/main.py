# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# screen = Screen()
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(200)
# timmy.rt(90)
# timmy.forward(200)
# timmy.rt(90)
# timmy.forward(200)
# timmy.rt(90)
# timmy.forward(200)
# screen.exitonclick()

from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY


table = PrettyTable()
table.field_names= ['Fname', 'Lname', 'DoB', 'Email']
table.add_row(['Aminu', 'Yiwere', '20th April, 1997', 'yiwereamin@gmail.com'])
table.add_row(['Kofi', 'Amankwah', '12th June, 1987', 'amankwahkofi@gmail.com'])
table.align = 'l'
table.set_style(MSWORD_FRIENDLY)
print(table)

