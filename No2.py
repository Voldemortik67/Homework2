import csv

file = open("purchases.csv", "w", newline="", encoding="utf-8")#Создаём файл purchases.csv
writer = csv.writer(file)
writer.writerow(["Товар", "Цена за штуку", "Количество"])
writer.writerow(["Тетрадь", 2.50, 4])
writer.writerow(["Ручка", 1.20, 3])
writer.writerow(["Папка", 4.00, 2])
writer.writerow(["Маркер", 3.30, 1])
file.close()

file = open("purchases.csv", "r", encoding="utf-8")#Читаем данные из файла
reader = csv.reader(file)
next(reader)  # пропускаем строку с заголовками

total = 0

for row in reader:
    name = row[0]
    price = float(row[1])
    count = int(row[2])

    cost = round(price * count, 2)#Стоимость покупки = цена * количество
    
    print(name, "| цена:", price, "| количество:", count, "| стоимость:", cost)#Выводим информацию о товаре

    total = total + cost

file.close()

print("Общая сумма покупок:", round(total, 2))#Общая сумма