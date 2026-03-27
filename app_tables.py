from rich.console import Console
from rich.table import Table

def create_table(product: str, price: float, quantity: int, subtotal: float) -> Table:
    table = Table(title=f"{product}")

    table.add_column("Product Name", justify="center", style="cyan", no_wrap=True)
    table.add_column("Price", justify="center", style="magenta")
    table.add_column("Quantity", justify="center", style="green")
    table.add_column("Subtotal", justify="center", style="blue")

    table.add_row(product, f"{price:.2f}", str(quantity), f"{subtotal:.2f}")
    
    console = Console()
    console.print(table)
    return "Table created"

def create_loop_table(product_list: dict) -> Table:
    table = Table(title=f"Products")

    table.add_column("Product Name", justify="center", style="cyan", no_wrap=True)
    table.add_column("Price", justify="center", style="magenta")
    table.add_column("Quantity", justify="center", style="green")
    table.add_column("Subtotal", justify="center", style="blue")

    for product in product_list:
        product_name = product["name"]
        price = float(product["price"])
        quantity = int(product["quantity"])
        subtotal = price * quantity
        table.add_row(product_name, f"{price:.2f}", str(quantity), f"{subtotal:.2f}")
    
    console = Console()
    console.print(table)
    return "Table created"

