from task_1 import Book, Car, Laptop  # Импортируем созданные ранее классы

if __name__ == "__main__":
    # Создание объектов классов
    book = Book("Python Basics", 300)
    car = Car("Toyota", 50, 10)
    laptop = Laptop("Dell", 50)

    # Тестирование методов классов с корректными аргументами
    print(book.read(50))          # Ожидается: 50
    print(book.progress())        # Ожидается: 16.67

    print(car.refuel(20))         # Ожидается: 30.0
    print(car.accelerate(50))     # Ожидается: None
    print(car.speed)              # Ожидается: 50.0

    print(laptop.charge(30))      # Ожидается: 80
    laptop.power_on()             # Ноутбук включен
    print(laptop.is_on)           # Ожидается: True
    laptop.power_off()            # Ноутбук выключен
    print(laptop.is_on)           # Ожидается: False

    # Проверка обработки ошибок через try...except
    try:
        book.read(-10)  # Некорректное количество страниц
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке

    try:
        car.refuel(-5)  # Некорректное количество топлива
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке

    try:
        laptop.charge(-5)  # Некорректное количество заряда
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке

    try:
        laptop.power_on()  # Попытка включить ноутбук с разряженной батареей
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке