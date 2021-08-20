# Задание 5.4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translations = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task_5_4_file_english.txt') as read_f:
    with open('task_5_4_file_russian.txt', 'w') as write_f:
        for s in read_f:
            cypher, nums = s.strip('\n').split('-')
            print(f'{translations[cypher] if cypher in translations else "Неизвестное число"}-{nums}', file=write_f)

print(f'Файл с переводом:')
with open('task_5_4_file_russian.txt') as read_f:
    for s in read_f:
        print(s.strip('\n'))