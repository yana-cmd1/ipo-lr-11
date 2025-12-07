#Дмитрук Яны
#Вариант 4
print("start code")
import json
import os

print("=" * 50)
print("СОЗДАНИЕ HTML СТРАНИЦЫ")
print("=" * 50)

input("\nНажмите Enter, чтобы начать...")

# пытаемся загрузить данные
try:
    with open('data.json', 'r', encoding='utf-8') as f:
        teachers = json.load(f)
    print("Данные загружены из data.json")
except:
    print("Файл data.json не найден, использую примерные данные")
    teachers = [
        {"id": 1, "name": "Амброжи Наталья Михайловна", "post": "Преподаватель высшей категории"},
        {"id": 2, "name": "Бровка Дионисий Сергеевич", "post": "Преподаватель без категории"},
        {"id": 3, "name": "Касперович Светлана Александровна", "post": "Преподаватель высшей категории"},
        {"id": 4, "name": "Иванов Иван Иванович", "post": "Преподаватель первой категории"},
        {"id": 5, "name": "Петрова Ольга Сергеевна", "post": "Методист"}
    ]

# cоздаем HTML страницу
html = '''<!DOCTYPE html>
<html>
<head>
    <title>Преподаватели МГКЦТ</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(to right, #4CAF50, #2196F3);
            padding: 20px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            max-width: 1000px;
            margin: auto;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th {
            background: #2196F3;
            color: white;
            padding: 15px;
        }
        td {
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }
        tr:hover {
            background: #f5f5f5;
        }
        .link {
            text-align: center;
            margin-top: 30px;
        }
        a {
            background: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎓 Преподаватели МГКЦТ</h1>
        <table>
            <tr>
                <th>№</th>
                <th>ФИО</th>
                <th>Должность</th>
            </tr>'''

# добавляем данные в таблицу
for teacher in teachers:
    html += f'''
            <tr>
                <td>{teacher['id']}</td>
                <td><b>{teacher['name']}</b></td>
                <td>{teacher['post']}</td>
            </tr>'''

# завершаем HTML
html += f'''
        </table>
        <p style="text-align: center;">Всего преподавателей: {len(teachers)}</p>
        <div class="link">
            <a href="https://mgkct.minskedu.gov.by" target="_blank">
                Оригинальный сайт
            </a>
        </div>
    </div>
</body>
</html>'''

# сохраняем файл
with open('index.html', 'w', encoding='utf-8-sig') as f:
    f.write(html)

print(f"\nHTML страница создана: index.html")
print(f"Количество преподавателей: {len(teachers)}")
print(f"Файл находится в: {os.path.abspath('index.html')}")

print("\nКак открыть файл:")
print("1. Найди файл index.html в папке")
print("2. Щелкни по нему два раза")
print("3. Или открой через браузер")

input("\nНажмите Enter для выхода...")
print("end code")