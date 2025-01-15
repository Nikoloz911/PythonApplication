class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.products = [] 

    def add_product(self, product):
        self.products.append(product)

    def get_total(self):
        total = sum(product.price for product in self.products)
        return total

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        for product in self.products:
            print(product)
        print(f"Total Price: ${self.get_total()}")
