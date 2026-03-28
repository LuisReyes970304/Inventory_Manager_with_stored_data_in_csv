from messages import invalid_price_message, invalid_amount_message, invalid_name_message, invalid_ValueError_message_int, invalid_ValueError_message_float

#This is the name validation, it makes sure the product name is not an empty str 
def name_validator():
    """This function validates the product name, it makes sure the name is not empty and it capitalizes the first letter of the name."""
    validator = True
    while validator:
        name = input("Write the product's name: ").strip().capitalize()
        if not name:
            invalid_name_message()
            validator = True
        if name: 
            validator = False
    return name

#This is the price validator, it makes sure the price is a float and a valid number    
def price_validator(name):
    """This function validates the product price, it makes sure the price is a float and a valid number."""
    validator = True
    while validator:
        try:
            price = float(input(f"Write the {name}'s price: "))
            if price <= 0: 
                invalid_price_message()
                validator = True
            if price > 0:
                validator = False
        except ValueError:
            invalid_ValueError_message_float()
    return price

#This function makes sure the amount of product is a valid number and a integer
def amount_validator(name):
    """This function validates the product amount, it makes sure the amount is a valid number and a integer."""
    validator = True
    while validator:
        try:
            amount = int(input(f"Write the {name}'s amount: "))
            if amount <= 0: 
                invalid_amount_message()
                validator = True
            if amount > 0:
                validator = False
        except ValueError:
            invalid_ValueError_message_int()
    return amount

