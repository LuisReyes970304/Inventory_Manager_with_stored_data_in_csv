import csv

lista = []

class ProductManagement:
    def __init__(self, product_list: list, doc="doc.csv"):
        self.doc = doc
        self.product_list = product_list

    def synchronize_list_with_db(self):
        try:
            with open(self.doc, newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.product_list.append(row)
            return self.product_list
        except FileNotFoundError:
            with open(self.doc, "w", newline="") as csvfile:
                csvfile.write("")

    def create_new_product(self, **product_data):
        self.product_list.append(product_data)
        return f"New product added"
    
    def save_to_database(self):
        with open(self.doc, "w", newline="") as csvfile:
            fieldnames = ["name", "price", "quantity"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in self.product_list:
                writer.writerow(product)
    
    def delete_product(self):
        pass
            
    def check_product_list(self):
        print(self.product_list)

    def check_more_expensive(self):
        pass
    


# test = ProductManagement(lista)

# test.synchronize_list_with_db()

