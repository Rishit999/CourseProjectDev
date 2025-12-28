import sys

def calculate_discount(price, discount, quantity):
    total = price * quantity
    return total - (total * discount / 100)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("No arguments passed. Using default values.")
        price = 100
        discount = 10
        quantity = 2
    else:
        price = float(sys.argv[1])
        discount = float(sys.argv[2])
        quantity = int(sys.argv[3])

    final_price = calculate_discount(price, discount, quantity)
    print("Final Price:", final_price)
