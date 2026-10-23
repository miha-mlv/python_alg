
prices = {
    "хлеб": 50,
    "молоко": 90,
    "сыр": 400,
    "яблоки": 120,
    "кофе": 350
}

def ask_cashier_name():
    return input("Введите имя кассира: ").strip()

def greet_cashier(name):
    print(f"Здравствуйте, {name}! Касса открыта")

def print_menu(prices):
    print("Товары в продаже:")
    for product, price in prices.items():
        print(f"    {product} - {price} руб.")

def ask_product():
    return input(f"\nТовар (или \"оплата\", чтобы перейти к оплате): ").strip().lower()

def ask_quantity(product):
    return int(input(f"Сколько \"{product}\"? "))

def item_cost(price, quantity):
    return price*quantity

def print_added(product, quantity, cost):
    print(f"Добавлено: {product} × {quantity} = {cost} руб.")

def collect_purchases(prices):
    cart = []
    while True:
        product = ask_product()
        if product == "оплата":
            break

        if product not in prices:
            print(f"Товара \"{product}\" нет в продаже")
            continue

        quantity = ask_quantity(product=product)
        cost = item_cost(price=prices[product], quantity=quantity)
        cart.append((product, quantity, cost))
        print_added(product=product, quantity=quantity, cost=cost)

    return cart

def ask_for_card():
    answer = input("\nЕсть карта магазина? (да/нет): ").strip().lower()
    return answer == "да"


def print_receipt(cart):
    print("\n--- Чек ---")
    total = 0

    for number, (product, quantity, cost) in enumerate(cart, start=1):
        print(f"{number}. {product} × {quantity} = {cost} руб.")
        total += cost

    print(f"Сумма: {total} руб.")
    return total


def apply_discount(total, card=False):
    if card:
        discount = total // 10
    elif total >= 1000:
        discount = total // 20
    else:
        discount = 0

    return discount, total - discount


def print_payment_summary(discount, amount_to_pay, cart):
    print(f"Скидка: {discount} руб.")
    print(f"К оплате: {amount_to_pay} руб.")

    different_products = set()
    for product, quantity, cost in cart:
        different_products.add(product)

    print(f"Разных товаров в чеке: {len(different_products)}")


def say_goodbye(name):
    print(f"\nСпасибо за работу, {name}!")


def checkout(prices):
    cashier = ask_cashier_name()
    greet_cashier(cashier)
    print_menu(prices)

    cart = collect_purchases(prices)

    has_card = ask_for_card()
    total = print_receipt(cart)
    discount, amount_to_pay = apply_discount(total, card=has_card)
    print_payment_summary(discount, amount_to_pay, cart)
    
    say_goodbye(cashier)


def main():
    checkout(prices)


main()