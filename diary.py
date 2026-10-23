# diary.py — Щоденник мандрівника

# Додали День 3 у початковий список
diary = [
    {"day": 1, "text": "Прибув до містечка Вербівка, зупинився на заїжджому дворі."},
    {"day": 2, "text": "Знайшов стару карту в руїнах на околиці міста."},
    {"day": 3, "text": "Місцевий коваль розповів легенду про занедбану шахту."},
]

def print_diary(diary):
    """Виводить усі записи щоденника."""
    print("\n=== Щоденник мандрівника ===")
    for entry in diary:
        print(f"День {entry['day']}: {entry['text']}")
    print()

def get_int_input(prompt):
    """Безпечне введення цілого числа (з повторним запитом при помилці)."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Помилка: введи ціле число.")

def add_entry(diary):
    """Запитує номер дня і текст нового запису та додає його до щоденника."""
    day = get_int_input("Введи номер дня: ")
    text = input("Введи текст запису: ")
    diary.append({"day": day, "text": text})
    print("Запис додано!")

def count_entries(diary):
    """Повертає загальну кількість записів у щоденнику."""
    return len(diary)

def entries_with_word(diary, word):
    """Шукає і виводить записи, які містять вказане слово."""
    print(f"\n--- Пошук записів зі словом '{word}' ---")
    found = False
    for entry in diary:
        if word.lower() in entry['text'].lower():
            print(f"День {entry['day']}: {entry['text']}")
            found = True
    if not found:
        print("Нічого не знайдено.")

# Основна частина
print_diary(diary)
add_entry(diary)
print_diary(diary)
print(f"Всього записів: {count_entries(diary)}")

# Демонстрація нової функції пошуку
search_word = input("\nВведи слово для пошуку в щоденнику: ")
entries_with_word(diary, search_word)
