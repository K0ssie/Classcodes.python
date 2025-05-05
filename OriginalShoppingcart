from tabnanny import check
class ShoppingCart:
    def __init__(self):
        self.items= []

    def add_items(self,item_name:str,qty:int,unit_price:float):
            self.items.append((item_name,qty,unit_price))
    def remove_items (self,item_name:str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break
    def calculate_total(self)-> float:
        total = 0.0
        for name,qty,price in self.items:
            total+= qty * price
        return total
    def summary (self):
        print("cart contents")
        for name,qty,price in self.items:

            print(f"{name}:{qty}:@ Ksh {price:.3f}each")
        print(f"total: Ksh{self.calculate_total():.2f}\n")

    def checkout(cart):
        cart.summary()
        print(f"Final_amount:Ksh{cart.calculate_total():.2f}\n")

if __name__== "__main__":
    cart: ShoppingCart = ShoppingCart()

    cart.add_items("Kiwi",50,79.2)
    cart.add_items("Papaya",30,40.3)
    cart.add_items("Guava",20,20.1)

    print(">>> Regular cart <<<")

    cart.checkout()
