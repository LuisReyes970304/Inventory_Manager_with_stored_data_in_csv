def add_new_product(database: list, **product_data):
    database.append(product_data)
    return f"New product {product_data.name} added"