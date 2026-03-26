from messages import welcome_message_fun, bye_message_function, invalid_amount_message, invalid_price_message, invalid_ValueError_message_int, menu_function, sub_menu
from application import ProductManagement

product_list = []

app = ProductManagement(product_list)
app.synchronize_list_with_db()

welcome_message_fun()
keep = True
while keep:
    menu_function()
    question = input("Enter the option you want to select: ")
    if question == "1":
        print("\nYou selected: Create a new product!")
        name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the order quantity: "))
        app.create_new_product(name=name, price=price, quantity=quantity)
        app.save_to_database()
        print("Product added successfully to the csv database!")

    elif question == "2":
        print("\nYou selected: Check product!")
        print(sub_menu)
        sub_question = input("Enter the leter to choose: ").upper()
        if sub_question == "a":
            pass

    elif question == "5":
        keep = False

bye_message_function()
