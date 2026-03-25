import csv

lista = []

class ProductManagement:
    def __init__(self, product_list: list, doc="doc.csv"):
        self.doc = doc
        self.product_list = product_list

    def add_new_product(self, **product_data):
        self.product_list.append(product_data)
        return f"New product added"
    
    def save_to_database(self):
        with open(self.doc, 'w', newline='') as csvfile:
            fieldnames = ["name", "price", "quantity"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in self.product_list:
                writer.writerow(product)
            


test = ProductManagement(lista)

test.add_new_product(name="gallina", price=2000.0, quantity=8)
test.add_new_product(name="pollo", price=1000.0, quantity=1)
print(test.product_list)
test.save_to_database()

