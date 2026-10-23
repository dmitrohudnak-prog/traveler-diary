# diary.py — Щоденник мандрівника

diary = [
    {"day": 1, "text": "Прибув до містечка Вербівка, зупинився на заїжджому дворі."},
    {"day": 2, "text": "Знайшов стару карту в руїнах на околиці міста."},
    {"day": 3, "text": "Місцевий коваль розповів легенду про занедбану шахту."},
]

def print_diary(diary):
    """Виводить усі записи щоденника."""
    print("\n=== Щоденник мандрівника ===")
    if not diary:
        print("Щоденник порожній.")
    for entry in diary:
        print(f"День {entry['day']}: {entry['text']}")
    print()

def get_int_input(prompt):
    """Безпечне введення цілого числа."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Помилка: введи ціле число.")

def add_entry(diary):
    """Додає новий запис."""
    day = get_int_input("Введи номер дня: ")
    text = input("Введи текст запису: ")
    diary.append({"day": day, "text": text})
    print("Запис успішно додано!")

def count_entries(diary):
    """Повертає кількість записів."""
    return len(diary)

def entries_with_word(diary, word):
    """Пошук за словом."""
    print(f"\n--- Результати пошуку для '{word}' ---")
    found = False
    for entry in diary:
        if word.lower() in entry['text'].lower():
            print(f"День {entry['day']}: {entry['text']}")
            found = True
    if not found:
        print("Записів із таким словом не знайдено.")

def main():
    """Головне меню програми."""
    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Переглянути всі записи")
        print("2. Додати новий запис")
        print("3. Пошук за ключовим словом")
        print("4. Показати статистику (кількість записів)")
        print("5. Вийти з програми")
        
        choice = input("Обери дію (1-5): ")
        
        if choice == "1":
            print_diary(diary)
        elif choice == "2":
            add_entry(diary)
        elif choice == "3":
            word = input("Введи слово для пошуку: ")
            entries_with_word(diary, word)
        elif choice == "4":
            print(f"\nВсього записів у щоденнику: {count_entries(diary)}")
        elif choice == "5":
            print("Дякуємо, що користувалися щоденником! Щасливої дороги!")
            break
        else:
            print("Некоректний вибір. Спробуй ще раз.")

if __name__ == "__main__":
    main()
