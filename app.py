import sys

def calculate_discount(price, discount, quantity):
    total = price * quantity
    return total - (total * discount / 100)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python app.py <price> <discount> <quantity>")
        sys.exit(1)

    price = float(sys.argv[1])
    discount = float(sys.argv[2])
    quantity = int(sys.argv[3])

    final_price = calculate_discount(price, discount, quantity)

    print(f"Price: {price}")
    print(f"Discount: {discount}%")
    print(f"Quantity: {quantity}")

    if final_price > 0:
        print(f"Final Price: {final_price}")
    else:
        print("Invalid calculation")
