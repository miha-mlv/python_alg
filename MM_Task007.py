def load_catalog(filename):
    """Загружает книги: id -> (название, цена, количество)."""
    catalog = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split(";")
                if len(parts) != 4:
                    print(f"Строка {line_number}: должно быть 4 поля. Строка пропущена.")
                    continue

                try:
                    book_id = int(parts[0])
                    price = int(parts[2])
                    quantity = int(parts[3])
                except ValueError:
                    print(
                        f"Строка {line_number}: ID, цена и количество должны быть "
                        "целыми числами. Строка пропущена."
                    )
                    continue

                title = parts[1].strip()

                if book_id < 1:
                    print(f"Строка {line_number}: ID должен быть не меньше 1. Строка пропущена.")
                    continue
                if book_id in catalog:
                    print(f"Строка {line_number}: ID {book_id} уже есть. Строка пропущена.")
                    continue
                if price <= 0:
                    print(f"Строка {line_number}: цена должна быть больше 0. Строка пропущена.")
                    continue
                if quantity < 0:
                    print(f"Строка {line_number}: количество не может быть отрицательным. Строка пропущена.")
                    continue
                if not title:
                    print(f"Строка {line_number}: название пустое. Строка пропущена.")
                    continue

                catalog[book_id] = (title, price, quantity)

    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создан пустой каталог.")
        return {}
    except (OSError, UnicodeError) as error:
        print(f"Не удалось прочитать файл {filename}: {error}")
        return {}

    print(f"Файл {filename} загружен. Книг в каталоге: {len(catalog)}")
    return catalog


def save_catalog(filename, catalog):
    """Сохраняет каталог. Возвращает True при успешной записи."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for book_id in sorted(catalog):
                title, price, quantity = catalog[book_id]
                file.write(f"{book_id};{title};{price};{quantity}\n")
    except OSError as error:
        print(f"Не удалось записать файл {filename}: {error}")
        return False

    print(f"Каталог сохранён в файл {filename}.")
    return True


def print_catalog(catalog):
    if not catalog:
        print("Каталог пуст.")
        return

    print("\nКаталог:")
    for book_id in sorted(catalog):
        title, price, quantity = catalog[book_id]
        if quantity == 0:
            print(f"{book_id}. {title} - {price} руб., нет в наличии")
        else:
            print(f"{book_id}. {title} - {price} руб., остаток: {quantity}")


def add_book(catalog):
    try:
        book_id = int(input("ID новой книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id < 1:
        print("ID должен быть не меньше 1.")
        return False
    if book_id in catalog:
        print("Книга с таким ID уже есть в каталоге.")
        return False

    title = input("Название: ").strip()
    if not title:
        print("Название не должно быть пустым.")
        return False
    if ";" in title:
        print("Название не должно содержать точку с запятой.")
        return False

    try:
        price = int(input("Цена: "))
    except ValueError:
        print("Цена должна быть целым числом.")
        return False

    if price <= 0:
        print("Цена должна быть больше 0.")
        return False

    try:
        quantity = int(input("Количество: "))
    except ValueError:
        print("Количество должно быть целым числом.")
        return False

    if quantity < 0:
        print("Количество не может быть отрицательным.")
        return False

    catalog[book_id] = (title, price, quantity)
    print(f"Книга «{title}» добавлена.")
    return True


def delete_book(catalog):
    try:
        book_id = int(input("ID книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print("Книги с таким ID нет в каталоге.")
        return False

    title, price, quantity = catalog[book_id]
    del catalog[book_id]
    print(f"Книга «{title}» удалена.")
    return True


def change_price(catalog):
    try:
        book_id = int(input("ID книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print("Книги с таким ID нет в каталоге.")
        return False

    try:
        new_price = int(input("Новая цена: "))
    except ValueError:
        print("Цена должна быть целым числом.")
        return False

    if new_price <= 0:
        print("Цена должна быть больше 0.")
        return False

    title, price, quantity = catalog[book_id]
    catalog[book_id] = (title, new_price, quantity)
    print(f"Цена книги «{title}» изменена на {new_price} руб.")
    return True


def change_quantity(catalog):
    try:
        book_id = int(input("ID книги: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print("Книги с таким ID нет в каталоге.")
        return False

    try:
        new_quantity = int(input("Новое количество: "))
    except ValueError:
        print("Количество должно быть целым числом.")
        return False

    if new_quantity < 0:
        print("Количество не может быть отрицательным.")
        return False

    title, price, quantity = catalog[book_id]
    catalog[book_id] = (title, price, new_quantity)
    print(f"Количество книги «{title}» изменено на {new_quantity}.")
    return True


def main():
    filename = "catalog.txt"
    catalog = load_catalog(filename)

    while True:
        print("\nМеню:")
        print("1 — показать каталог")
        print("2 — добавить книгу")
        print("3 — удалить книгу")
        print("4 — изменить цену")
        print("5 — изменить количество")
        print("0 — сохранить и выйти")

        try:
            choice = int(input("Выберите пункт: "))
        except ValueError:
            print("Пункт меню должен быть целым числом.")
            continue

        if choice == 1:
            print_catalog(catalog)
        elif choice == 2:
            add_book(catalog)
        elif choice == 3:
            delete_book(catalog)
        elif choice == 4:
            change_price(catalog)
        elif choice == 5:
            change_quantity(catalog)
        elif choice == 0:
            if save_catalog(filename, catalog):
                print("До свидания!")
                break
            print("Каталог не сохранён. Исправьте причину ошибки и повторите сохранение.")
        else:
            print("Такого пункта нет. Выберите число от 0 до 5.")


if __name__ == "__main__":
    main()
