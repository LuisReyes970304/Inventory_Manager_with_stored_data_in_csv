from messages import welcome_message_fun, bye_message_function, invalid_amount_message, invalid_price_message, invalid_ValueError_message_int, menu_function
from application import add_new_product

database = []

welcome_message_fun()
keep = True
while keep:
    menu_function()
    question = input("Enter the number of the option you want to select: ")
    if question == "1":
        add_new_product()
    if question == "5":
        keep = False

bye_message_function()
