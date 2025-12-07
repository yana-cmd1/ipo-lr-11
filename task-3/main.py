import json
#Дмитрук Яны
#Вариант 4
print("start code")
print("=" * 50)
print("СОХРАНЕНИЕ ДАННЫХ В JSON ФАЙЛ")
print("=" * 50)

input("\nНажмите Enter, чтобы начать...")

# примерные данные (в реальности будут с сайта)
teachers = [
    {"id": 1, "name": "Амброжи Наталья Михайловна", "post": "Преподаватель высшей категории"},
    {"id": 2, "name": "Бровка Дионисий Сергеевич", "post": "Преподаватель без категории"},
    {"id": 3, "name": "Касперович Светлана Александровна", "post": "Преподаватель высшей категории"},
    {"id": 4, "name": "Иванов Иван Иванович", "post": "Преподаватель первой категории"},
    {"id": 5, "name": "Петрова Ольга Сергеевна", "post": "Методист"}
]

# выводим на экран
print("\nСобранные данные:")
print("-" * 50)
for teacher in teachers:
    print(f"{teacher['id']}. Teacher: {teacher['name']}; Post: {teacher['post']};")

# сохраняем в файлл
filename = "data.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(teachers, f, ensure_ascii=False, indent=2)

print("-" * 50)
print(f"\nДанные сохранены в файл: {filename}")
print(f"Всего записей: {len(teachers)}")

# показываем содержимое файла
print("\nСодержимое файла:")
print("-" * 30)
with open(filename, 'r', encoding='utf-8') as f:
    print(f.read())

input("\nНажмите Enter для выхода...")
print("end code")