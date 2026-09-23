user_last_name = input("Введите вашу фамилию: ")
user_first_name = input("Введите ваше имя: ")
print(f"Добро пожаловать, {user_first_name}! Начинаем приём заявок\n")

total_student = 0
approved_student = 0

while(True):
    student_last_name = input("Фамилия абитуриента (или \"завершить\", чтобы закончить приём): ")
    if(student_last_name == "завершить"):
        print("\n")
        break
    student_score = int(input("Балл абитуриента: "))
    has_olympiad = input("Есть ли диплом олимпиады? (да/нет): ")
    if(student_score >= 220):
        print(f"{student_last_name}: заявка одобрена\n")
        total_student+=1
        approved_student+=1
    elif(has_olympiad == "да" and student_score>=180):
        print(f"{student_last_name}: заявка одобрена\n")
        total_student+=1
        approved_student+=1
    else:
        print(f"{student_last_name}: заявка отклонена\n")
        total_student+=1

print(f"Рассмотрено абитуриентов: {total_student}")
print(f"Зачислено: {approved_student}")
print(f"\nДо свидания, {user_first_name}!")
