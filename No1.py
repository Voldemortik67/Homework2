file = open("diary.txt", "w", encoding="utf-8")#Создаём файл и записываем три исходные записи
file.write("Сегодня мы работали с файлами Python.\n")
file.write("Научились сохранять текст.\n")
file.write("Узнали, как читать данные обратно.\n")
file.close()

# 2. Дописываем четвёртую запись в конец файла (режим "a")
file = open("diary.txt", "a", encoding="utf-8")
file.write("Следующее занятие – CSV и JSON\n")
file.close()

# 3. Читаем файл и выводим все записи
file = open("diary.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

for line in lines:
    print(line.strip())

# 4. Количество записей
print("Количество записей:", len(lines))