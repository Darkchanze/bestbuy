from Classes import Store, Product


def start(store, product_list):
    """
    Prints the user_interface in a loop. Handles the user input and sends
    him to the required function, while handling errors.

    Args:
        store: The store instance to perform operations on.
        product_list (list): A list of all products available in the store.
    """
    while True:
        store_functions ={1: list_all_products_in_store,
                          2: show_total_amount_in_store,
                          3: make_an_order,}
        print("   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        try:
            user_choice = int(input("Please choose a number: "))
            if not (1 <= user_choice <= 4):
                raise ValueError()
            if user_choice == 4:
                print("Have a nice day!")
                break
            elif user_choice == 3:
                store_functions[user_choice](store, product_list)
            else:
                store_functions[user_choice](store)
        except ValueError:
            print("Enter a number between 1 and 4.")
        print()


def list_all_products_in_store(store):
    """
    Lists all products available in the store, including their price and quantity.

    Args:
        store: The store instance containing the products.
    """
    list_of_products = store.get_all_products()
    print("------")
    for i, product in enumerate(list_of_products, 1):
        print(f"{i}. {product}, Price: {product.quantity}, Quantity: {product.quantity}")            # why does it function .quantity
    print("------")                  #product.get_quantity()                                                   self note


def show_total_amount_in_store(store):
    """
    Prints the total amount of items available at the store.

    Args:
        store: The store instance to access (get_total_quantity()) the total quantity.
    """
    print(f"Total of {store.get_total_quantity()} in store.")


def make_an_order(store, product_list):
    """
    Allows the user to select products and quantities, adds them to an order,
    and then shows the total price.

    Args:
        store: The store instance to place the order.
        product_list (list): A list of all products available in the store.
    """
    order_list = []
    list_all_products_in_store(store)
    print("When you want to finish order, enter empty text.")
    while True:
        order_tuple = get_item_and_quantity(product_list)
        if order_tuple == "break":
            break
        elif isinstance(order_tuple, tuple) and len(order_tuple) == 2:
            order_list.append(order_tuple)
            print("Product added to list!")
    order_price = store.order(order_list)
    print(f"Order made! Total payment: ${order_price}")


def get_item_and_quantity(product_list):
    """
    Asks the user to select a product and specify a quantity, validating the input.

    Args:
        product_list (list): A list of all products available in the store.

    Returns:
        tuple: A tuple containing the selected product and the specified quantity.
        str: Returns "break" if the user wants to end the order process.
    """
    # Get product number
    product_number = input("Which product number do you want?")
    if product_number == "":
        return "break"
    try:
        product_number = int(product_number)
        if product_number > len(product_list):
            print("Invalid input. Pick a number from the list.")
            return
        index = product_number - 1
        ordered_product = product_list[index]
    except ValueError:
        print("Invalid input.")
        return
    # Get quantity
    quantity = input("Which amount do you want?")
    if quantity == "":
        return "break"
    try:
        quantity = int(quantity)
        if quantity > ordered_product.get_quantity():
            print(f"Just {ordered_product.get_quantity()} left in stock. Product was not added.")
            return
    except ValueError:
        print("Invalid input.")
        return
    return (ordered_product, quantity)


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    store = Store(product_list)
    start(store, product_list)


if __name__ == "__main__":
    main()

