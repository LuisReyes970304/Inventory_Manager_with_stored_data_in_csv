from messages import welcome_message_fun, bye_message_function, invalid_amount_message, invalid_price_message, invalid_ValueError_message_int, menu_function, sub_menu
from application import ProductManagement

product_list = []

app = ProductManagement(product_list)
app.synchronize_list_with_db()

welcome_message_fun()
keep = True
while keep:
    menu_function()
    question = input("Choose an option: ")
    if question == "1":
        print("\nYou selected: Create a new product!")
        name = input("Enter the product name: ").title()
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the order quantity: "))
        app.add_new_order(name=name, price=price, quantity=quantity)
        print("Product added successfully to the csv database!")

    elif question == "2":
        print("\nYou selected: Check product!")
        print(sub_menu)
        sub_question = input("Enter the leter to choose: ").upper()

        if sub_question == "A":
            product_name = input("Enter the product's name you are looking for: ").capitalize()
            app.check_specific_product(product_name)

        if sub_question == "B":
            app.check_product_list()

        if sub_question == "C":
            app.check_product_list()

    elif question == "5":
        keep = False

app.save_to_database()
bye_message_function()
