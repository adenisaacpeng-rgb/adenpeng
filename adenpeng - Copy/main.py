# main.py
# ============================================================
#  STATIONERY INVENTORY MANAGEMENT SYSTEM
#  Module : SF43002FP  –  Programming 2
#  Description: Main script that provides an interactive menu
#               to manage a stationery inventory.
# ============================================================

import csv
import os

# Import the StationeryItem class and helper from the companion module
from stationery import StationeryItem, build_item_from_input

# ── Pre-loaded sample data (from Table 1 in the brief) ──────────────────────
inventory: list[StationeryItem] = [
    StationeryItem("Pen", 200, 1.20),
    StationeryItem("Pencil", 250, 0.80),
    StationeryItem("Eraser", 150, 0.50),
    StationeryItem("Glue Stick", 100, 1.10),
    StationeryItem("Writing Book", 300, 1.50),
]

MENU = """
====================================================
       STATIONERY INVENTORY MANAGEMENT SYSTEM
====================================================
  1 – To enter new stationery item
  2 – To edit the stationery item
  3 – To update the stationery item which was sold
  4 – To display all the stationery items
  5 – To save the list of all the stationery items in .CSV file
===================================================="""

CSV_FILENAME = "stationery_inventory.csv"


# ── Helper utilities ─────────────────────────────────────────────────────────

def clear_screen() -> None:
    """Clear the terminal output (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def find_item(name: str) -> StationeryItem | None:
    """
    Search the inventory for an item by name (case-insensitive).
    Returns the StationeryItem object, or None if not found.
    """
    for item in inventory:
        if item.name.lower() == name.lower():
            return item
    return None


def print_table(items: list[StationeryItem]) -> None:
    """
    Display all stationery items in a formatted table.
    Columns: No. | Name | Quantity | Price ($) | Total Price ($)
    """
    if not items:
        print("\n  [!] No items in the inventory yet.\n")
        return

    # Column widths
    w_no, w_name, w_qty, w_price, w_total = 5, 20, 10, 12, 16
    sep = f"  {'─' * w_no}{'─' * w_name}{'─' * w_qty}{'─' * w_price}{'─' * w_total}"

    header = (
        f"  {'No.':<{w_no}}"
        f"{'Name':<{w_name}}"
        f"{'Quantity':>{w_qty}}"
        f"{'Price ($)':>{w_price}}"
        f"{'Total Price ($)':>{w_total}}"
    )

    print(f"\n{sep}")
    print(header)
    print(sep)

    for idx, item in enumerate(items, start=1):
        total = item.calculate_total_price()  # uses the class method
        print(
            f"  {idx:<{w_no}}"
            f"{item.name:<{w_name}}"
            f"{item.quantity:>{w_qty}}"
            f"{item.price:>{w_price}.2f}"
            f"{total:>{w_total}.2f}"
        )

    print(f"{sep}\n")


# ── Option handlers ──────────────────────────────────────────────────────────

def option_add_item() -> None:
    """Option 1 – Prompt user to enter a new stationery item."""
    print("\n  [ ADD NEW STATIONERY ITEM ]")
    try:
        new_item = build_item_from_input()          # defined in stationery.py

        # Check for duplicate names
        if find_item(new_item.name):
            print(f"\n  [!] '{new_item.name}' already exists. Use Option 2 to edit.\n")
            return

        inventory.append(new_item)
        total = new_item.calculate_total_price()    # class method
        print(
            f"\n  [✓] '{new_item.name}' added successfully. "
            f"Total price: ${total:.2f}\n"
        )

    except ValueError as err:
        print(f"\n  [!] Invalid input – {err}\n")


def option_edit_item() -> None:
    """Option 2 – Find an item and allow the user to re-enter its details."""
    print("\n  [ EDIT STATIONERY ITEM ]")
    name = input("  Enter the name of the item to edit: ").strip()
    item = find_item(name)

    if item is None:
        print(f"\n  [!] Error: '{name}' not found in inventory.\n")
        return

    print(f"\n  Item found: {item}")
    print("  Enter new details (press Enter to keep existing value):\n")

    try:
        # Name
        new_name = input(f"  New name [{item.name}]           : ").strip()
        if new_name:
            # Prevent duplicates when renaming
            if new_name.lower() != item.name.lower() and find_item(new_name):
                print(f"\n  [!] '{new_name}' already exists.\n")
                return
            item.name = new_name

        # Quantity
        qty_str = input(f"  New quantity [{item.quantity}]         : ").strip()
        if qty_str:
            qty = int(qty_str)
            if qty < 0:
                raise ValueError("Quantity cannot be negative.")
            item.quantity = qty

        # Price
        price_str = input(f"  New unit price [{item.price:.2f}]    : ").strip()
        if price_str:
            price = float(price_str)
            if price < 0:
                raise ValueError("Price cannot be negative.")
            item.price = price

        total = item.calculate_total_price()
        print(
            f"\n  [✓] Item updated. New total price: ${total:.2f}\n"
        )

    except ValueError as err:
        print(f"\n  [!] Invalid input – {err}\n")


def option_update_sold() -> None:
    """Option 3 – Deduct the sold quantity from an existing item."""
    print("\n  [ UPDATE SOLD STATIONERY ITEM ]")
    name = input("  Enter the name of the item sold: ").strip()
    item = find_item(name)

    if item is None:
        print(f"\n  [!] Error: '{name}' not found in inventory.\n")
        return

    try:
        qty_sold = int(input(f"  Enter quantity sold (current stock: {item.quantity}): "))
        if qty_sold < 0:
            raise ValueError("Sold quantity cannot be negative.")
        if qty_sold > item.quantity:
            raise ValueError(
                f"Sold quantity ({qty_sold}) exceeds available stock ({item.quantity})."
            )

        item.quantity -= qty_sold
        total = item.calculate_total_price()
        print(
            f"\n  [✓] Stock updated. Remaining qty: {item.quantity}, "
            f"New total price: ${total:.2f}\n"
        )

    except ValueError as err:
        print(f"\n  [!] Invalid input – {err}\n")


def option_display_items() -> None:
    """Option 4 – Display all stationery items in a formatted table."""
    print("\n  [ ALL STATIONERY ITEMS ]\n")
    print_table(inventory)


def option_save_csv() -> None:
    """
    Option 5 – Save all stationery items to a CSV file.
    Fields: Name, Quantity, Price ($), Total Price ($)
    """
    if not inventory:
        print("\n  [!] Inventory is empty – nothing to save.\n")
        return

    try:
        fieldnames = ["No.", "Name", "Quantity", "Price ($)", "Total Price ($)"]
        with open(CSV_FILENAME, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for idx, item in enumerate(inventory, start=1):
                writer.writerow(
                    {
                        "No.": idx,
                        "Name": item.name,
                        "Quantity": item.quantity,
                        "Price ($)": f"{item.price:.2f}",
                        "Total Price ($)": f"{item.calculate_total_price():.2f}",
                    }
                )

        print(f"\n  [✓] Inventory saved to '{CSV_FILENAME}' successfully.\n")

    except OSError as err:
        print(f"\n  [!] File error – {err}\n")


# ── Main program loop ────────────────────────────────────────────────────────

def main() -> None:
    """Entry point – display menu and dispatch to the correct option handler."""

    while True:
        print(MENU)

        choice = input("  Enter your option (1-5): ").strip()

        if choice == "1":
            option_add_item()
        elif choice == "2":
            option_edit_item()
        elif choice == "3":
            option_update_sold()
        elif choice == "4":
            option_display_items()
        elif choice == "5":
            option_save_csv()
        else:
            # Invalid option handling (Task 3)
            print(f"\n  [!] Invalid option '{choice}'. Please choose 1 – 5.\n")

        # Ask user if they want to continue (Task 7)
        cont = input("  Continue with the program? (y/n): ").strip().lower()
        if cont != "y":
            print("\n  Thank you for using the Stationery Inventory Management System. Goodbye!\n")
            break

        clear_screen()


# Guard so this file can be imported as a module without running main()
if __name__ == "__main__":
    main()
