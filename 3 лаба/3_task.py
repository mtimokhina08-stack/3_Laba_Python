import csv
from docxtpl import DocxTemplate

def load_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append({
                'year': int(row[0]),
                'name': row[1],
                'gender': row[2],
                'time': row[4],
                'city': row[5]
            })
    return data


def group_data(data):
    result = {}
    for item in data:
        year = item['year']
        city = item['city']

        # Проверяем существует ли год
        if year not in result:
            result[year] = {}

        # Проверяем существует ли город
        if city not in result[year]:
            result[year][city] = {'male': None, 'female': None}

        # Теперь можно заполнять данные
        if item['gender'] == 'Male':
            result[year][city]['male'] = {'name': item['name'], 'time': item['time']}
    return dict(sorted(result.items()))

def create_report(grouped_data):
    doc = DocxTemplate('template.docx')
    doc.render({'data': grouped_data})
    doc.save('marathon_report.docx')


def main():
    try:
        data = load_data('data_marathon.csv')
    except FileNotFoundError:
        print("Файл не найден")
    grouped = group_data(data)
    create_report(grouped)
    print("Документ создан")
main()