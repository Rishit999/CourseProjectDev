def calculate_discount(price, discount):
    return price - (price * discount / 100)

def get_product_details():
    name = input("Enter Product Name: ")
    pid = input("Enter Product ID: ")
    price = float(input("Enter Price: "))
    discount = float(input("Enter Discount %: "))

    final_price = calculate_discount(price, discount)

    return {
        "name": name,
        "pid": pid,
        "price": price,
        "discount": discount,
        "final_price": final_price
    }

def display_product(product):
    print("\nProduct Details")
    print("Name:", product["name"])
    print("ID:", product["pid"])
    print("Final Price:", product["final_price"])

if __name__ == "__main__":
    product = get_product_details()
    display_product(product)