from messages import welcome_message_fun, bye_message_function, menu_function, sub_menu_function
from validation import name_validator, price_validator, amount_validator
from inventory import ProductManagement

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
        name = name_validator()
        price = price_validator(name)
        quantity = amount_validator(name)
        app.add_new_order(name=name, price=price, quantity=quantity)

    elif question == "2":
        print("\nYou selected: Check product!")

        sub_while = True
        while sub_while:
            sub_menu_function()
            sub_question = input("Choose an opction: ").upper()

            if sub_question == "A":
                print("\nYou selected: Check specific product!")
                product_name = name_validator()
                app.check_specific_product(product_name)
                app.save_to_database()

            elif sub_question == "B":
                print("\nYou selected: Check the list of productst!")
                app.check_product_list()

            elif sub_question == "C":
                print("\nYou selected: Check the more expensive product")
                app.check_more_expensive()

            elif sub_question == "D":
                print("\nYou selected: Check total earnings!")
                app.check_total_earnings()
                

            elif sub_question == "E":
                print("\nYou selected: Come to the main menu!")
                sub_while = False

            else: 
                print("That is not a valid option try again!")
    elif question == "3":
        print("\nYou selected: Update product")
        product_name = name_validator()
        verified = app.check_specific_product(product_name)
        if verified == product_list:
            price = price_validator(product_name)
            quantity = amount_validator(product_name)
            app.update_product(product_name, price=price, quantity=quantity)
            app.save_to_database()


    elif question == "4":
        print("\nYou selected: Delete product!")
        product_to_delete = name_validator()
        print(f"Are you sure you want to delete {product_to_delete}? (Y/N)")
        confirmation = input().upper()
        if confirmation != "Y":
            print("Deletion cancelled.")
            continue
        deleted = app.delete_product(product_to_delete)
        if deleted == product_list:
            app.save_to_database()
        else:
            print("Product not found!")

    elif question == "5":
        keep = False
    
    elif question not in ["1", "2", "3", "4", "5"]:
        print("That is not a valid option, please try again!")



bye_message_function()
