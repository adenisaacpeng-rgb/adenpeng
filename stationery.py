# stationery.py
# This module defines the StationeryItem class and helper functions
# used by the main Stationery Inventory Management System script.


class StationeryItem:
    """
    Represents a single stationery item in the inventory.
    Stores name, quantity, unit price, and computes total price.
    """

    def __init__(self, name: str, quantity: int, price: float):
        """Initialise a new StationeryItem."""
        self.name = name
        self.quantity = quantity
        self.price = price  # unit price

    def calculate_total_price(self) -> float:
        """
        Calculate and return the total price for this item.
        Total price = quantity × unit price.
        """
        return round(self.quantity * self.price, 2)

    def to_dict(self) -> dict:
        """Return the item's data as a dictionary (includes total price)."""
        return {
            "Name": self.name,
            "Quantity": self.quantity,
            "Price ($)": self.price,
            "Total Price ($)": self.calculate_total_price(),
        }

    def __repr__(self) -> str:
        return (
            f"StationeryItem(name={self.name!r}, qty={self.quantity}, "
            f"price={self.price}, total={self.calculate_total_price()})"
        )


def build_item_from_input() -> StationeryItem:
    """
    Interactively prompt the user for item details and return
    a validated StationeryItem instance.
    Raises ValueError for invalid numeric input.
    """
    name = input("  Enter item name       : ").strip()
    if not name:
        raise ValueError("Item name cannot be empty.")

    quantity = int(input("  Enter quantity        : "))
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    price = float(input("  Enter unit price ($)  : "))
    if price < 0:
        raise ValueError("Price cannot be negative.")

    return StationeryItem(name, quantity, price)
