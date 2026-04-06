import csv

def load_data(filename):
    countries = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            countries.append({
                'country': row['Country'],
                'health_care': float(row['Health Care']),
                'income': float(row['Income']),
                'inflation': float(row['Inflation']),
                'life_expectancy': float(row['Life Expectancy'])
            })
    return countries


def filter_by_income(countries, min_income, max_income):
    return list(filter(lambda c: min_income <= c['income'] <= max_income, countries))


def sort_by_inflation(countries):
    return sorted(countries, key=lambda c: c['inflation'])


def save_to_csv(countries, filename):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Country', 'Health Care', 'Income', 'Inflation', 'Life Expectancy'])
        for c in countries:
            writer.writerow([c['country'], c['health_care'], c['income'], c['inflation'], c['life_expectancy']])


def main():
    try:
        filename = input("Введите путь к файлу: ")
        countries = load_data(filename)

        try:
            min_inc = float(input("Введите минимальный доход: "))
            max_inc = float(input("Введите максимальный доход: "))
        except ValueError:
            print("Ошибка: введите числа")

        filtered = filter_by_income(countries, min_inc, max_inc)
        save_to_csv(filtered, 'filtered_by_income.csv')
        print(f"Сохранено {len(filtered)} стран в filtered_by_income.csv")

        sorted_countries = sort_by_inflation(countries)
        save_to_csv(sorted_countries, 'sorted_by_inflation.csv')
        print(f"Сохранено {len(sorted_countries)} стран в sorted_by_inflation.csv")

    except FileNotFoundError:
        print("Файл не найден")

main()