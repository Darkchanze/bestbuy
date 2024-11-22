class Product:
    """
    Represents a product that is stored.
    This class handles methods like activation, deactivation, promotions,
    and buy.

    Attributes:
        active (bool): Indicates if the product is active (default = True).
        promotion (Promotion or None): An optional promotion applied to the product.
     """


    def __init__(self, name, price, quantity):
        """
        Initializes a Product instance with name, price, and quantity.

        Args:
            name (str): The name of the product. Must not be empty.
            price (float): The price of the product. Must not be negative.
            quantity (int): The quantity of the product. Must not be negative.

        Attributes:
            active (bool): Indicates whether the product is active. Defaults to True.
            promotion (None): Indicates if a promotion is applied. Defaults to None.

        Raises:
            ValueError: If name is empty, price is invalid, or quantity is invalid.
        """
        self.name = str(name)
        if self.name == "":
            raise ValueError("Name must not be empty")
        try:
            self.price = float(price)
            if self.price < 0:
                raise ValueError("Price must be greater than 0")
        except (ValueError, TypeError):
            print("Invalid price provided.")
        self.set_quantity(quantity)
        self.active = True


    def get_quantity(self):
        """
        Calls the promotion set to this product.

        Returns:
            self.promotion or None: The assigned promotion, or None if no promotion is set.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Setter function for quantity of product.
        If quantity reaches 0, deactivates the product.

        Args:
            quantity (int): The new quantity. Must not be negative.

        Raises:
            ValueError: If the quantity is invalid or negative.
        """
        try:
            self.quantity = int(quantity)
            if self.quantity < 0:
                raise ValueError("Quantity must not be negative")
        except (ValueError, TypeError):
            print("Invalid quantity provided")
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        """
        Getter function for active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active


    def activate(self):
        """
        Activates the product, making it available for purchase.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates the product, making it unavailable for purchase.
        """
        self.active = False


    def show(self):
        """
        Presents the product.

        Returns:
             info (str): A string that presents the product, including name, price, quantity. Promotion if active.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """
       Process of buying a product.

        Args:
            quantity (int): The quantity to purchase. Must be positive and less than
                            or equal to the available quantity.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity is negative or exceeds available stock.
        """
        if quantity > self.quantity:
            raise ValueError("Quantity is too high")
        if quantity < 0:
            raise ValueError("Quantity must not be negative")
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity


    def __str__(self):
        """
        Returns the product's name.

        Returns:
            str: The name of the product.
        """
        return f"{self.name}"