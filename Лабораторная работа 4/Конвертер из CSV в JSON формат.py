# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv" #имя входного csv файла
OUTPUT_FILENAME = "output.json" #имя выходного json файла


def task() -> None: #функция task конвертирует содержимое csv файла в json файл
    with open(INPUT_FILENAME) as f: # TODO считать содержимое csv файла
        l = [line for line in csv.DictReader(f)] #преобразую строки в список

    with open(OUTPUT_FILENAME, "w") as f: #открываю json файл для записи и сохраняю туда данные с отступами для читаемости
        json.dump(l, f, indent=4)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f: #открываю созданный json файл и вывожу его содержимое построчно
        for line in output_f:
            print(line, end="")
