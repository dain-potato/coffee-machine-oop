# Coffee Machine OOP

## Description
This project simulates a coffee machine using Object-Oriented Programming (OOP). It allows users to select drinks, process payments, and checks the machine's resources. It consists of various classes that handle menu items, resource management, and transactions.

## Classes

### 1. `MenuItem`
Represents a drink available in the coffee machine.

**Attributes:**
- `name`: The name of the drink (e.g., "latte").
- `cost`: The price of the drink (e.g., 1.5).
- `ingredients`: A dictionary containing the ingredients and their amounts required to make the drink (e.g., `{"water": 100, "coffee": 16}`).

### 2. `Menu`
Handles the available drinks and their details.

**Methods:**
- `get_items()`: Returns the available drink names as a concatenated string (e.g., "latte/espresso/cappuccino").
- `find_drink(order_name)`: Searches for a drink by name and returns the corresponding `MenuItem` object or `None` if the drink is unavailable.

### 3. `CoffeeMaker`
Manages the coffee machine's resources (water, milk, coffee).

**Methods:**
- `report()`: Prints the current resource levels (e.g., Water: 300ml, Milk: 200ml, Coffee: 100g).
- `is_resource_sufficient(drink)`: Checks if there are enough ingredients to make the chosen drink. Returns `True` or `False`.
- `make_coffee(order)`: Deducts the required ingredients from the machine's resources to make the drink.

### 4. `MoneyMachine`
Handles financial transactions for the coffee machine.

**Methods:**
- `report()`: Prints the current profit (e.g., Money: $0).
- `make_payment(cost)`: Processes the payment for a drink. Returns `True` if the payment is accepted or `False` if insufficient funds are provided.

## Exercise Information
- This project is part of the exercises from the **100 Days of Code: The Complete Python Pro Bootcamp** on Udemy.

## How to Run
1. Clone this repository.
2. Run the program using Python:
   ```bash
   python coffee_machine.py
