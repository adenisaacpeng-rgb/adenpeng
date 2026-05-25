# 📦 Stationery Inventory Management System

> **Module:** SF43002FP – Programming 2  
> **Language:** Python 3.10+  
> **No external packages required**

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [File Structure](#2-file-structure)
3. [Requirements](#3-requirements)
4. [How to Run](#4-how-to-run)
5. [Menu Options](#5-menu-options)
   - [Option 1 – Add New Item](#option-1--add-new-stationery-item)
   - [Option 2 – Edit Item](#option-2--edit-stationery-item)
   - [Option 3 – Update Sold Stock](#option-3--update-sold-stock)
   - [Option 4 – Display All Items](#option-4--display-all-items)
   - [Option 5 – Save to CSV](#option-5--save-to-csv)
6. [Error Handling](#6-error-handling)
7. [Code Structure](#7-code-structure)
8. [Sample Output](#8-sample-output)
9. [Pre-loaded Data](#9-pre-loaded-data)

---

## 1. Project Overview

The **Stationery Inventory Management System** is a command-line Python application built for **StationeryTrack Pte Ltd**. It allows users to:

- Add, edit, and track stationery stock
- Automatically calculate total prices per item
- Update stock levels after sales
- Export the full inventory to a `.csv` file

The system is split across **two Python scripts** following Object-Oriented Programming (OOP) principles.

---

## 2. File Structure

```
stationery_inventory/
│
├── main.py           # Main script – menu system and all option handlers
├── stationery.py     # StationeryItem class and input helper function
└── README.md         # This user guide
```

| File | Role |
|---|---|
| `main.py` | Entry point. Runs the interactive menu and handles all 5 options. |
| `stationery.py` | Defines the `StationeryItem` class with `calculate_total_price()` and the `build_item_from_input()` helper. |

---

## 3. Requirements

| Requirement | Detail |
|---|---|
| Python version | **3.10 or higher** |
| External packages | **None** – uses only built-in `csv` and `os` modules |
| Operating system | Windows, macOS, or Linux |

---

## 4. How to Run

### Step 1 – Open a terminal

Navigate to the project folder:

```bash
cd stationery_inventory
```

### Step 2 – Run the main script

```bash
python main.py
```

> On some systems you may need to use `python3` instead of `python`.

### Step 3 – Use the menu

The program will display the interactive menu:

```
====================================================
       STATIONERY INVENTORY MANAGEMENT SYSTEM
====================================================
  1 – To enter new stationery item
  2 – To edit the stationery item
  3 – To update the stationery item which was sold
  4 – To display all the stationery items
  5 – To save the list of all the stationery items in .CSV file
====================================================
  Enter your option (1-5):
```

Type a number (`1`–`5`) and press **Enter**.

### Step 4 – Continue or exit

After every action, the program asks:

```
  Continue with the program? (y/n):
```

- Type `y` → clears the screen and returns to the main menu  
- Type `n` → exits the program gracefully

---

## 5. Menu Options

### Option 1 – Add New Stationery Item

Prompts you to enter the details of a **brand-new** item.

**Steps:**
1. Choose option `1`
2. Enter the item **name** (e.g. `Ruler`)
3. Enter the **quantity** (e.g. `120`)
4. Enter the **unit price** in dollars (e.g. `0.90`)

**Example interaction:**
```
  [ ADD NEW STATIONERY ITEM ]
  Enter item name       : Ruler
  Enter quantity        : 120
  Enter unit price ($)  : 0.90

  [✓] 'Ruler' added successfully. Total price: $108.00
```

> **Notes:**
> - The total price is calculated automatically: `quantity × unit price`
> - Duplicate item names are not allowed
> - Quantity and price cannot be negative

---

### Option 2 – Edit Stationery Item

Find an existing item by name and update any of its fields.

**Steps:**
1. Choose option `2`
2. Enter the **exact name** of the item to edit (case-insensitive)
3. For each field, enter a new value **or press Enter to keep the existing one**

**Example interaction:**
```
  [ EDIT STATIONERY ITEM ]
  Enter the name of the item to edit: pen

  Item found: StationeryItem(name='Pen', qty=200, price=1.2, total=240.0)
  Enter new details (press Enter to keep existing value):

  New name [Pen]           :
  New quantity [200]       : 180
  New unit price [1.20]    : 1.50

  [✓] Item updated. New total price: $270.00
```

> **Notes:**
> - The search is **case-insensitive** (`pen`, `PEN`, and `Pen` all match)
> - If the item is **not found**, an error message is shown and no changes are made
> - Renaming to an already-existing name is not allowed

---

### Option 3 – Update Sold Stock

Deduct a quantity from an existing item after a sale.

**Steps:**
1. Choose option `3`
2. Enter the **name** of the item sold
3. Enter the **quantity sold**

**Example interaction:**
```
  [ UPDATE SOLD STATIONERY ITEM ]
  Enter the name of the item sold: Pencil
  Enter quantity sold (current stock: 250): 50

  [✓] Stock updated. Remaining qty: 200, New total price: $160.00
```

> **Notes:**
> - If the quantity sold **exceeds** current stock, an error is shown
> - Negative sold quantities are rejected
> - The total price is automatically recalculated after the deduction

---

### Option 4 – Display All Items

Shows the complete inventory in a formatted table.

**Example output:**
```
  [ ALL STATIONERY ITEMS ]

  ─────────────────────────────────────────────────────────────
  No.  Name                  Quantity   Price ($)  Total Price ($)
  ─────────────────────────────────────────────────────────────
  1    Pen                        200        1.20           240.00
  2    Pencil                     250        0.80           200.00
  3    Eraser                     150        0.50            75.00
  4    Glue Stick                 100        1.10           110.00
  5    Writing Book               300        1.50           450.00
  ─────────────────────────────────────────────────────────────
```

> **Note:** The **Total Price** column is calculated live using `calculate_total_price()` from the `StationeryItem` class.

---

### Option 5 – Save to CSV

Exports the full inventory to a **CSV file** named `stationery_inventory.csv` in the same folder.

**Example interaction:**
```
  [✓] Inventory saved to 'stationery_inventory.csv' successfully.
```

**CSV file contents example:**
```
No.,Name,Quantity,Price ($),Total Price ($)
1,Pen,200,1.20,240.00
2,Pencil,250,0.80,200.00
3,Eraser,150,0.50,75.00
4,Glue Stick,100,1.10,110.00
5,Writing Book,300,1.50,450.00
```

> **Note:** You can open this file in **Microsoft Excel**, **Google Sheets**, or any spreadsheet application.

---

## 6. Error Handling

The program uses `try/except` blocks to catch and handle invalid input gracefully.

| Situation | What happens |
|---|---|
| Non-numeric quantity or price | Error message shown; no changes made |
| Negative quantity or price | Error message shown; input rejected |
| Item name not found (Options 2 & 3) | Error message shown; operation cancelled |
| Sold quantity exceeds stock | Error message shown; stock unchanged |
| Empty item name | Error message shown; item not added |
| Duplicate item name | Error message shown; item not added |
| Invalid menu option (not 1–5) | `[!] Invalid option` message shown |
| File write error (Option 5) | OS error message shown |

**Example error messages:**
```
  [!] Invalid input – Quantity cannot be negative.
  [!] Error: 'Stapler' not found in inventory.
  [!] Invalid option '9'. Please choose 1 – 5.
  [!] Invalid input – Sold quantity (999) exceeds available stock (200).
```

---

## 7. Code Structure

### `stationery.py`

```
StationeryItem (class)
├── __init__(name, quantity, price)     → Initialise item attributes
├── calculate_total_price()             → Returns quantity × price (rounded to 2 dp)
├── to_dict()                           → Returns item data as a dictionary
└── __repr__()                          → String representation for debugging

build_item_from_input() (function)
└── Prompts user → validates → returns a new StationeryItem
```

### `main.py`

```
inventory (list)                        → Stores all StationeryItem objects

Helpers
├── clear_screen()                      → Clears terminal (cross-platform)
├── find_item(name)                     → Case-insensitive search; returns item or None
└── print_table(items)                  → Prints formatted table of all items

Option handlers
├── option_add_item()                   → Option 1 logic
├── option_edit_item()                  → Option 2 logic
├── option_update_sold()                → Option 3 logic
├── option_display_items()              → Option 4 logic
└── option_save_csv()                   → Option 5 logic

main()                                  → Main loop: show menu → dispatch → continue/exit
```

---

## 8. Sample Output

### Full session example

```
====================================================
       STATIONERY INVENTORY MANAGEMENT SYSTEM
====================================================
  1 – To enter new stationery item
  2 – To edit the stationery item
  3 – To update the stationery item which was sold
  4 – To display all the stationery items
  5 – To save the list of all the stationery items in .CSV file
====================================================
  Enter your option (1-5): 1

  [ ADD NEW STATIONERY ITEM ]
  Enter item name       : Marker
  Enter quantity        : 80
  Enter unit price ($)  : 2.50

  [✓] 'Marker' added successfully. Total price: $200.00

  Continue with the program? (y/n): y

  Enter your option (1-5): 4

  [ ALL STATIONERY ITEMS ]

  ─────────────────────────────────────────────────────────────────
  No.  Name                  Quantity   Price ($)  Total Price ($)
  ─────────────────────────────────────────────────────────────────
  1    Pen                        200        1.20           240.00
  2    Pencil                     250        0.80           200.00
  3    Eraser                     150        0.50            75.00
  4    Glue Stick                 100        1.10           110.00
  5    Writing Book               300        1.50           450.00
  6    Marker                      80        2.50           200.00
  ─────────────────────────────────────────────────────────────────

  Continue with the program? (y/n): n

  Thank you for using the Stationery Inventory Management System. Goodbye!
```

---

## 9. Pre-loaded Data

The system comes with **5 sample items** already loaded on startup (from Table 1 of the project brief):

| No. | Name | Quantity | Price ($) | Total Price ($) |
|---|---|---|---|---|
| 1 | Pen | 200 | 1.20 | 240.00 |
| 2 | Pencil | 250 | 0.80 | 200.00 |
| 3 | Eraser | 150 | 0.50 | 75.00 |
| 4 | Glue Stick | 100 | 1.10 | 110.00 |
| 5 | Writing Book | 300 | 1.50 | 450.00 |

> These are defined in `main.py` at the top of the file and are available immediately when the program starts.

---

*© 2025 DataMax Pte Ltd – SF43002FP Programming 2 Project*
