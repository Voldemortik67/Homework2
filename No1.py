file = open("diary.txt", "w", encoding="utf-8")#Создаём файл и записываем три исходные записи
file.write("Сегодня мы работали с файлами Python.\n")
file.write("Научились сохранять текст.\n")
file.write("Узнали, как читать данные обратно.\n")
file.close()

file = open("diary.txt", "a", encoding="utf-8")#Дописываем четвёртую запись в конец файла (режим "a")
file.write("Следующее занятие – CSV и JSON\n")
file.close()

file = open("diary.txt", "r", encoding="utf-8")#Читаем файл и выводим все записи
lines = file.readlines()
file.close()

for line in lines:
    print(line.strip())

print("Количество записей:", len(lines))#Количество записей