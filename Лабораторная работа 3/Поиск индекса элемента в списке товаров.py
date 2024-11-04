# TODO Напишите функцию для поиска индекса товара
def index(list, item):
    for i, j in enumerate(list): #перебираю элементы списка с их индексами
        if j == item: #если элемент совпадает с искомым товаром,то возвращаю его индекс
            return i

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
