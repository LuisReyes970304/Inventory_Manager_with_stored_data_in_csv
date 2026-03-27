import csv
from app_tables import create_table, create_loop_table, Table


lista = []

subtotal = lambda price, quantity: price * quantity

class ProductManagement:
    def __init__(self, product_list: list, doc="database.csv"):
        self.doc = doc
        self.product_list = product_list

    def synchronize_list_with_db(self) -> list:
        try:
            with open(self.doc, newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.product_list.append(row)
            return self.product_list
        except FileNotFoundError:
            with open(self.doc, "w", newline="") as csvfile:
                csvfile.write("")

    def save_to_database(self):
        with open(self.doc, "w", newline="") as csvfile:
            fieldnames = ["name", "price", "quantity"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in self.product_list:
                writer.writerow(product)

    def add_new_order(self, **product_data) -> list:
        self.product_list.append(product_data)
        return f"New product added"
    
    def check_specific_product(self, query: str) -> Table:
        for product in self.product_list:
            if  query == product["name"]:
                subtotal = float(product["price"]) * int(product["quantity"])
                create_table(product["name"], float(product["price"]), product["quantity"], float(subtotal))
            
    def check_product_list(self):
        create_loop_table(self.product_list)
            

    def check_more_expensive(self):
        for product in self.product_list:
            pass
    
    def delete_product(self):
        pass

# test = ProductManagement(lista)

# test.synchronize_list_with_db()

