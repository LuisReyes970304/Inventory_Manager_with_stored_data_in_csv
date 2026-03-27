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

    elif question == "2":
        print("\nYou selected: Check product!")

        sub_while = True
        while sub_while:
            print(sub_menu)
            sub_question = input("Choose an opction: ").upper()

            if sub_question == "A":
                print("\nYou selected: Check specific product!")
                product_name = input("Enter the product's name you are looking for: ").capitalize()
                app.check_specific_product(product_name)
                app.save_to_database()

            elif sub_question == "B":
                print("\nYou selected: Check the list of productst!")
                app.check_product_list()

            elif sub_question == "C":
                print("\nYou selected: Check the more expensive product")
                app.check_more_expensive()

            elif sub_question == "D":
                print("\nYou selected: Come to the main menu!")
                sub_while = False

            else: 
                print("That is not a valid option try again!")

    elif question == "4":
        product_to_delete = input("Enter the name of the product to deleted: ").capitalize()
        app.delete_product(product_to_delete)
        app.save_to_database()

    elif question == "5":
        keep = False


bye_message_function()
