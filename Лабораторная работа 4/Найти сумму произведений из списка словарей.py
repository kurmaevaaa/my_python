# TODO решите задачу
import json # импортирую модуль json для работы с json данными
def task() -> float: #функция task возвращает число с плавающей точкой
    f = "input.json"
    with open(f) as f: #открываю файл и загружаю его содержимое
        json_data = json.load(f)
    sumv = sum([item["score"] * item["weight"] for item in json_data])  # вычисляю сумму произведений значений "score" и "weight" для каждого элемента в json данных
    return round(sumv, 3) #округляю результат до трех знаков после запятой и возвращаю его
print(task())