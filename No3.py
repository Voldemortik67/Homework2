import json

profile = {"name": "Алексей", "group": "КБ-101", "skills": ["Python", "Excel"], "notifications": True}#Создаём профиль

file = open("participant.json", "w", encoding="utf-8")#Сохраняем в participant.json (ensure_ascii=False - чтобы были русские буквы)
json.dump(profile, file, ensure_ascii=False, indent=4)
file.close()

file = open("participant.json", "r", encoding="utf-8")#Читаем обратно
data = json.load(file)
file.close()

data["skills"].append("CSV")#Добавляем навык и выключаем уведомления
data["notifications"] = False

file = open("participant.json", "w", encoding="utf-8")#Сохраняем в тот же файл
json.dump(data, file, ensure_ascii=False, indent=4)
file.close()

file = open("participant.json", "r", encoding="utf-8")#Читаем ещё раз и выводим
result = json.load(file)
file.close()

print("Имя:", result["name"])
print("Группа:", result["group"])
print("Навыки:", result["skills"])
print("Уведомления включены:", result["notifications"])