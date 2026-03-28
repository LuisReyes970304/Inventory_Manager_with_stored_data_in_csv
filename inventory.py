import csv
from app_tables import create_table, create_loop_table
from rich.console import Console

console = Console()

class ProductManagement:
    """This class is responsible for managing the products, it has methods to add new products, check specific products, check the list of products, check the more expensive product, check total earnings, delete products and update products.
    Attributes:
        product_list (list): A list of dictionaries that contains the products information.
        doc (str): The name of the csv file that will be used as a database.
    Methods:
        synchronize_list_with_db: 
        save_to_database: 
        add_new_order: 
        check_specific_product: 
        check_product_list: 
        check_more_expensive: 
        check_total_earnings: 
        delete_product: 
        update_product: 
    """
    def __init__(self, product_list: list, doc="database.csv"):
        self.doc = doc
        self.product_list = product_list



    def synchronize_list_with_db(self) -> list:
        """This method synchronizes the product list with the database, it reads the csv file and updates the product list with the information from the csv file."""
        try:
            with open(self.doc, newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                self.product_list.clear()
                for row in reader:
                    self.product_list.append(row)
            return self.product_list
        except FileNotFoundError:
            with open(self.doc, "w", newline="") as csvfile:
                csvfile.write("")



    def save_to_database(self) -> None:
        """This method saves the product list to the database, it writes the product list to the csv file."""
        with open(self.doc, "w", newline="") as csvfile:
            fieldnames = ["name", "price", "quantity"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in self.product_list:
                writer.writerow(product)



    def add_new_order(self, **product_data) -> list:
        """
        This method adds a new product to the product list, it takes the product information as keyword arguments and adds it to the product list.
        Args:            
            product_data (dict): A dictionary that contains the product information, it should have the keys 
            "name", "price" and "quantity".
        """
        new_product = product_data.get("name")
        if any(d.get("name") == new_product for d in self.product_list):
            print(f"Error: the product '{new_product}' already exist in database.")
            print("If you want to add more of the product, decrease amount, choose option 3. update product")
            return self.product_list
        self.product_list.append(product_data)
        print("Product successfully added to the database!")
        return self.product_list
    


    def check_specific_product(self, query: str) -> dict:
        """
        This method checks if a specific product exist in the product list, it takes the product name as an argument and searches for it in the product list, if it finds it it will create a table with the product information.
        Args:
            query (str): The name of the product that we want to check.
        """
        for product in self.product_list:
            if query == product["name"]:
                subtotal = float(product["price"]) * int(product["quantity"])
                create_table(product["name"], float(product["price"]), product["quantity"], float(subtotal))
                return self.product_list
        print("Product not found")
        return "Not found"
            


    def check_product_list(self) -> str:
        """This method checks the list of products, it creates a table with the information of all the products in the product list."""
        create_loop_table(self.product_list)
            
    def check_more_expensive(self):
        """This method checks the more expensive product, it searches for the product with the highest price in the product list and prints its name and price."""
        most_expensive = max(self.product_list, key=lambda p: float(p["price"]))
        name = most_expensive["name"]
        price = most_expensive["price"]
        console.print(f"The most expensive product is [bold green]{name}[/bold green] with a price of [bold red]{price}[/bold red].")
        most_stocked = max(self.product_list, key=lambda p: int(p["quantity"]))
        name_stocked = most_stocked["name"]
        quantity_stocked = most_stocked["quantity"]
        console.print(f"The most stocked product is [bold green]{name_stocked}[/bold green] with a quantity of [bold red]{quantity_stocked}[/bold red].")

    def check_total_earnings(self):
        """This method checks the total earnings, it calculates the total earnings from all the products in the product list and prints it."""
        reward = []
        for product in self.product_list:
            subtotal = float(product["price"]) * int(product["quantity"])
            reward.append(subtotal)
        total_earnings = sum(reward)
        console.print(f"The total earnings from all products is [bold red]{total_earnings:.2f}[/bold red].")
        return total_earnings
    
    def delete_product(self, name: str) -> dict:
        """This method deletes a product from the product list, it takes the product name as an argument and removes it from the list if it exists. If it doesn't exist it will print an error message.
        Args:
            name (str): The name of the product that we want to delete.
        """
        for product in self.product_list:
            if name == product["name"]:
                self.product_list.remove(product)
                print("Product deleted successfully!")
                return self.product_list
        return None
            
    def update_product(self, name: str, **product_data: dict) -> dict | None:
        """This method updates a product from the product list, it takes the product name and the new product information as arguments and updates the product information if it exists. If it doesn't exist it will print an error message.
        Args:
            name (str): The name of the product that we want to update.
            product_data (dict): A dictionary that contains the new product information, it should have the keys "name", "price" and "quantity".
        """
        for product in self.product_list:
            if name == product["name"]:
                product.update(product_data)
                return self.product_list
        print("Product not found in database")
        return None