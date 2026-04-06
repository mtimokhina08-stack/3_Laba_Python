import json
def load_animals_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            animals = data['animals']
        return animals

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден")
        raise
    except json.JSONDecodeError:
        print(f"Ошибка парсинга JSON")
        raise

def main():
    filename = input("Введите путь к файлу: ")
    animals = load_animals_data(filename)

    birds = list(filter(lambda a: a.get('animal_type') == 'Bird', animals))

    print("\nПТИЦЫ:")
    if not birds:
        print("Птицы не найдены")
    else:
        for bird in birds:
            for key, value in bird.items():
                print(f"{key}: {value}")

    diurnal_count = len(list(filter(lambda a: a.get('active_time') == 'Diurnal', animals)))
    print(f"\nКоличество дневных животных: {diurnal_count}")

    if animals:
        lightest_animal = min(animals, key=lambda a: float(a.get('weight_min', 0)))
        print(f"\nЖивотное с наименьшим весом: {lightest_animal.get('name')}")
        print(f"Вес: {lightest_animal.get('weight_min')} кг")
    else:
        print("\nОшибка: список животных пуст")
main()