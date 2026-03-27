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
        new_product = product_data.get("name")
        if any(d.get("name") == new_product for d in self.product_list):
            print(f"Error: the product '{new_product}' already exist in database.")
            print("If you want to add more of the product, decrease amount, choose option 3. update product")
            return self.product_list
        self.product_list.append(product_data)
        print("Product successfully added to the database!")
        return self.product_list
    
    def check_specific_product(self, query: str) -> Table:
        for product in self.product_list:
            if query == product["name"]:
                subtotal = float(product["price"]) * int(product["quantity"])
                create_table(product["name"], float(product["price"]), product["quantity"], float(subtotal))
                return "Done"
        print("Product not found")
            
    def check_product_list(self):
        create_loop_table(self.product_list)
            
    def check_more_expensive(self):
        most_expensive = max(self.product_list, key=lambda p: p["price"])
        name = most_expensive["name"]
        price = most_expensive["price"]
        print(f"The most expensive product is {name} with a price of {price}")
    
    def delete_product(self, name: str):
        for product in self.product_list:
            if name == product["name"]:
                self.product_list.remove(product)
                print("Product deleted successfully!")
                return self.product_list
            else:
                print("Product deleted successfully!")
                return self.product_list
            
    def update_product(self, **product_data):
        pass