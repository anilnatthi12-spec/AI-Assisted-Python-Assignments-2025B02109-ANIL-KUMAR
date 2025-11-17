def student_discount(price):
    return price * 0.9 if price > 1000 else price * 0.95

def regular_discount(price):
    return price * 0.85 if price > 2000 else price

def discount(price, category):
    discount_fn = {
        "student": student_discount,
        "regular": regular_discount
    }
    return discount_fn.get(category, regular_discount)(price)

# Take input from user
try:
    price = float(input("Enter the price: "))
    category = input("Enter the category (student/regular): ").strip().lower()
    final_price = discount(price, category)
    print(f"Discounted price: {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value for price.")