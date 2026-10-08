print("Представление тренера")
trainer_surname = input("Введите вашу фамилию: ")
trainer_name = input("Введите ваше имя: ")
print(f"Добро пожаловать, {trainer_name}! Начинаем принимать зачёт")

athlete_count = int(input("\nСколько спортсменов сдают зачёт: "))
approach_count = int(input("Сколько подходов делает каждый: "))

surnames = []
totals = []
passed_count = 0

for athlete_number in range(1, athlete_count + 1):
    print(f"\n--- Спортсмен {athlete_number} ---")
    surname = input("Фамилия спортсмена: ")
    total = 0

    for approach_number in range(1, approach_count + 1):
        total += int(input(f"Подход {approach_number}: "))

    surnames.append(surname)
    totals.append(total)

    if total >= 30:
        passed_count += 1
        print(f"{surname}: всего {total} - норматив выполнен")
    else:
        print(f"{surname}: всего {total} - норматив не выполнен")

print("\nИтоговая таблица:")
for index in range(len(surnames)):
    print(f"{index + 1}. {surnames[index]} - {totals[index]}")

print(f"\nНорматив выполнили: {passed_count} из {athlete_count}")
print(f"Всего подтягиваний группы: {sum(totals)}")
print(f"\nДо свидания, {trainer_name}!")