organizer = input("Введите ваше имя: ").strip()
print(f"Здравствуйте, {organizer}! Открываем зрительское голосование")

films = ["дюна", "аватар", "матрица", "интерстеллар", "шрек"]
program = set(films)

print("Фильмы в программе фестиваля:", ", ".join(films))

votes = {}
for film in films:
    votes[film] = 0

viewers = set()
liked_by_everyone = set(films)
liked_by_anyone = set()

while True:
    name = input('\nИмя зрителя (или "стоп", чтобы закончить): ').strip()
    normalized_name = name.lower()
    if normalized_name == "стоп":
        break
    if normalized_name in viewers:
        print(f"{name}, вы уже голосовали, второй голос не засчитан")
        continue
    answer = input("Какие фильмы вам понравились (через запятую): ")
    selected_films = set()
    for title in answer.split(","):
        title = title.strip().lower()
        if title:
            selected_films.add(title)
    valid_films = set()
    for film in selected_films:
        if film in program:
            valid_films.add(film)
            votes[film] += 1
        else:
            print(f"Фильма «{film}» нет в программе, голос не засчитан")
    viewers.add(normalized_name)
    liked_by_everyone = liked_by_everyone & valid_films
    liked_by_anyone = liked_by_anyone | valid_films
    print(f"Спасибо, {name}! Засчитано голосов: {len(valid_films)}")

print("\nИтоги голосования")
print(f"Проголосовало зрителей: {len(viewers)}")

winner = films[0]
for film in films:
    print(f"{film} - {votes[film]}")
    if votes[film] > votes[winner]:
        winner = film

if votes[winner] > 0:
    print(f"Победитель: {winner} ({votes[winner]})")
else:
    print("Победитель не определён: ни один фильм не получил голосов")

if not viewers:
    liked_by_everyone = set()

everyone_list = []
nobody_list = []
liked_by_nobody = program - liked_by_anyone

for film in films:
    if film in liked_by_everyone:
        everyone_list.append(film)
    if film in liked_by_nobody:
        nobody_list.append(film)

if everyone_list:
    print("Понравились всем:", ", ".join(everyone_list))
else:
    print("Понравились всем: таких фильмов нет")

if nobody_list:
    print("Не выбрал никто:", ", ".join(nobody_list))
else:
    print("Не выбрал никто: таких фильмов нет")

print(f"\nДо свидания, {organizer}!")