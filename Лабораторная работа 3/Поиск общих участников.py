# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, arg = ','):
    list1 = first.split(arg)
    list2 = second.split(arg)
    allpart = list(set(list1).intersection(list2))
    allpart.sort()
    return allpart
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))