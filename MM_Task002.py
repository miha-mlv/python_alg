full_name = input("Введите ваш ФИО: ")
surname, name, patronymic = full_name.split()
product_list = [
    input("Введите первый товар: "),
    input("Введите второй товар: "),
    input("Введите третий товар: ") 
]
print()

print("Ваш список: ", product_list)
print("Товаров в списке: ", len(product_list))
print()

product_list.append("стакан")
print("Список после добавления подарка: ", product_list)
product_list.sort()
print("Отсортированный список: ", product_list)
print()

initials = f"{name[0].upper()}.{patronymic[0].upper()}."
print(f"До свидания, {initials} {surname}!")
