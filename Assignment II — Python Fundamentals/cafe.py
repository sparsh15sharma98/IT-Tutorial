# Name - Sparsh Sharma. Student ID - U3315385, Date - 16.09.2025
# Campus Café Checkout System
# Learning goals: dict (menu), list (cart), set (categories), while/for loops, floats, Booleans, functions

# -----------------------
# Menu dictionary: item -> (price, category)
# -----------------------
menu = {
    "Coffee": (2.50, "Drink"),
    "Tea": (2.00, "Drink"),
    "Juice": (3.00, "Drink"),
    "Muffin": (1.80, "Food"),
    "Sandwich": (4.50, "Food"),
    "Salad": (3.80, "Food")
}

# Cart will store the values of item_name and quantity
cart = []

# -----------------------
# Functions
# -----------------------
def show_menu():
    """Display the café menu."""
    print("\n--- Campus Café Menu ---")
    print(f"{'No.':<4}{'Item':<12}{'Price':>8}{'Category':>12}")
    print("-" * 38)
    for idx, (item, (price, category)) in enumerate(menu.items(), start=1):
        print(f"{idx:<4}{item:<12}${price:>7.2f}{category:>12}")

def add_item(cart):
    """Include the item to the cart."""
    show_menu()
    choice = input("Enter item name to add: ").strip().title()
    if choice in menu:
        try:
            qty = int(input(f"Enter quantity of {choice}: "))
            if qty > 0:
                cart.append((choice, qty))
                print(f"Added {qty}x {choice} to cart.")
            else:
                print("Quantity must be at least 1.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Item not found in the menu.")

def view_cart(cart):
    """Show the items which are available in the cart."""
    if not cart:
        print("\nCart is empty.")
        return
    
    print("\n--- Your Cart ---")
    print(f"{'Qty':<6}{'Item':<12}{'Line Total':>12}")
    print("-" * 32)
    categories = set()
    for item, qty in cart:
        price, category = menu[item]
        line_total = price * qty
        print(f"{qty:<6}{item:<12}${line_total:>10.2f}")
        categories.add(category)
    
    print(f"\nUnique categories in cart: {categories}")

def checkout(cart):
    """Display the receipt and find the totals with tax, discounts, and meal deals."""
    if not cart:
        print("\nCart is empty. Nothing to checkout.")
        return
    
    print("\n--- Receipt ---")
    print(f"{'Qty':<6}{'Item':<12}{'Line Total':>12}")
    print("-" * 32)
    subtotal = 0
    categories = set()

    for item, qty in cart:
        price, category = menu[item]
        line_total = price * qty
        subtotal += line_total
        categories.add(category)
        print(f"{qty:<6}{item:<12}${line_total:>10.2f}")

    tax = 0.10 * subtotal
    
    # Ask for student discount
    discount = 0
    student = input("Are you a student? (y/n): ").strip().lower()
    if student == "y":
        discount = 0.05 * subtotal
    
    # Apply meal deal: $1 off if both food and drink are present
    meal_deal = 0
    if "Food" in categories and "Drink" in categories:
        meal_deal = 1.00
        print("Meal deal applied: $1.00 off")

    total = subtotal + tax - discount - meal_deal

    print("-" * 32)
    print(f"{'Subtotal:':<18}${subtotal:>10.2f}")
    print(f"{'Tax (10%):':<18}${tax:>10.2f}")
    print(f"{'Student Disc:':<18}-${discount:>9.2f}")
    if meal_deal > 0:
        print(f"{'Meal Deal:':<18}-${meal_deal:>9.2f}")
    print("-" * 32)
    print(f"{'TOTAL:':<18}${total:>10.2f}")
    print("-" * 32)

    # Clear cart after checkout
    cart.clear()
    print("Checkout complete. Thank you!")

# -----------------------
# Loop for Main Program 
# -----------------------
def main():
    while True:
        print("\n--- Campus Café POS ---")
        print("1. Show Menu")
        print("2. Add Item")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number (1-5).")
            continue

        if choice == 1:
            show_menu()
        elif choice == 2:
            add_item(cart)
        elif choice == 3:
            view_cart(cart)
        elif choice == 4:
            checkout(cart)
        elif choice == 5:
            print("Exiting! Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1-5.")

# Run to get the output
if __name__ == "__main__":
    main()
