from abc import ABC, abstractmethod

# Abstract base class for items in the inventory
class InventoryItem(ABC):
    @abstractmethod
    def get_cost(self):
        """Returns the cost of the item."""
        pass

# Class representing a StoreItem
class StoreItem(InventoryItem):
    def __init__(self, item_name, item_cost):
        self.item_name = item_name
        self.__item_cost = item_cost  # Private attribute

    def get_cost(self):
        """Returns the cost of the item."""
        return self.__item_cost

    def __str__(self):
        """String representation of the item."""
        return f"{self.item_name}: ${self.__item_cost:.2f}"

# Class representing a Shopper
class Shopper:
    def __init__(self, shopper_name):
        self.shopper_name = shopper_name
        self.basket = Cart()

    def add_item(self, item):
        """Adds an item to the shopper's cart."""
        self.basket.add_item(item)

    def show_basket(self):
        """Displays the contents of the basket."""
        return self.basket.show_items()

# Class representing a Cart
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Adds an item to the cart."""
        self.items.append(item)

    def remove_item(self, item_name):
        """Removes an item from the cart by name."""
        self.items = [i for i in self.items if i.item_name != item_name]

    def total_amount(self):
        """Calculates the total cost of items in the cart."""
        return sum(item.get_cost() for item in self.items)

    def show_items(self):
        """Returns a list of string representations of items in the cart."""
        item_list = [str(item) for item in self.items]
        return item_list if item_list else ["Basket is empty."]

# Example Usage
if __name__ == "__main__":
    # Create some store items
    item1 = StoreItem("Tablet", 299.99)
    item2 = StoreItem("Smartwatch", 199.99)
    item3 = StoreItem("Bluetooth Speaker", 89.99)
    
    # Create a shopper
    shopper = Shopper("Bob")
    
    # Add items to the shopper's cart
    shopper.add_item(item1)
    shopper.add_item(item2)
    
    # Show basket contents and total amount
    print("Basket Contents:")
    print(shopper.show_basket())
    
    print(f"Total Amount: ${shopper.basket.total_amount():.2f}")

    # Add another item to the basket
    shopper.add_item(item3)

    print("\nBasket Contents after adding Bluetooth Speaker:")
    print(shopper.show_basket())
    
    print(f"Total Amount after adding: ${shopper.basket.total_amount():.2f}")

    # Remove an item from the basket
    shopper.basket.remove_item("Tablet")
    
    print("\nBasket Contents after removing Tablet:")
    print(shopper.show_basket())
    
    print(f"Total Amount after removal: ${shopper.basket.total_amount():.2f}")
