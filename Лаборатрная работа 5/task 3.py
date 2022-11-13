import random
def get_unique_list_numbers() -> list[int]:
    list = []
    while len(list) < 15:# TODO написать функцию для получения списка уникальных целых чисел
        number = random.randint(-10,10)
        if number not in list:
            list.append(number)
    return list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
print(len(set(list_unique_numbers)))
