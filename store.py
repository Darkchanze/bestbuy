

import products

class Store():
    list_of_products = []

    def __init__(self, initial_products=None):
        if initial_products:
            for product in initial_products:
                self.list_of_products.append(product)


    def add_product(self, product):
        """Adds a product to the store."""
        self.list_of_products.append(product)


    def remove_product(self, product):
        """Removes a product from store."""
        self.list_of_products.remove(product)


    def get_total_quantity(self):
        """Returns how many items are in the store in total
        by getting all quantity´s and summing it up."""
        return sum([item.get_quantity() for item in self.list_of_products])


    def get_all_products(self):
        """Returns all products in the store that are active and give back is_active(True)."""
        return [product for product in self.list_of_products if product.is_active()]
        #return [str(product) for product in self.list_of_products if product.is_active()]     alternative to show the name insted of number


    def order(self, shopping_list):
        """Gets a list of tuples which the item and the quantity.
        Removes the quantity from the product and returns the total price of the order."""
        total = 0.0
        if not isinstance(shopping_list, list):
            raise TypeError("shopping_list has to be a list")
        for item_order in shopping_list:
            if not isinstance(item_order, tuple) and len(tuple) != 2:
                raise ValueError("Order has to be a Tuple with 2 elements.")
            if not isinstance(item_order[0], products.Product) and not isinstance(item_order[1], int):
                raise TypeError("First element has to be a product and second a integer.")
            total += item_order[0].buy(item_order[1])
        return total




bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

store = Store([bose, mac])

"""pixel = products.Product("Google Pixel 7", price=500, quantity=250)
store.add_product(pixel)
#print(store.get_all_products())
#print(bose.show())
print(store.order([(bose, 1),(mac, 2)]))
#print(bose.show())"""
