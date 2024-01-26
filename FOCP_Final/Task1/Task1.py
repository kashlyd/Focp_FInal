def calculate_total_price(is_tuesday, num_pizzas, order_type, used_app):
    # Constants
    PIZZA_PRICE = 12.0
    DELIVERY_COST = 2.5
    APP_DISCOUNT = 0.25
    MIN_PIZZAS_FOR_FREE_DELIVERY = 5

    # Calculate discounts and charges
    discount_multiplier = 0.5 if is_tuesday == 'y' else 1.0
    delivery_charge = 0 if num_pizzas >= MIN_PIZZAS_FOR_FREE_DELIVERY or order_type == 'n' else DELIVERY_COST
    app_discount_multiplier = 1 - APP_DISCOUNT if used_app == 'y' else 1.0

    # Total cost calculation
    total_cost = (PIZZA_PRICE * num_pizzas * discount_multiplier + delivery_charge) * app_discount_multiplier

    return round(total_cost, 2)

def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['y', 'n']:
            return response
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    # Gathering validated user inputs
    num_pizzas = get_positive_integer_input("How many pizzas ordered? ")
    order_type = get_yes_no_input("Is delivery required? (Y/N): ")
    is_tuesday = get_yes_no_input("Is it Tuesday? (Y/N): ")
    used_app = get_yes_no_input("Did the customer use the app? (Y/N): ")

    # Calculate and display the total price
    total_price = calculate_total_price(is_tuesday, num_pizzas, order_type, used_app)
    print(f"\nTotal Price: £{total_price}.")

if __name__ == "__main__":
    main()
