# Задание 5.7
# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

averange_profit = 0.0
companies_count = 0
companies_dict = dict()
with open('task_5_7_file.txt') as read_f:
    for s in read_f:
        name, form, revenue, cost = s.strip('\n').split()
        revenue = float(revenue) if revenue.replace('.', '').isdigit() else 0.0
        cost = float(cost) if cost.replace('.', '').isdigit() else 0.0
        profit = revenue - cost
        companies_dict[name] = profit
        if profit > 0:
            averange_profit += profit
        companies_count += 1

averange_profit_dict = {"averange_profit": averange_profit / companies_count}
json_list =[companies_dict, averange_profit_dict]

with open('task_5_7_file.json', 'w') as write_f:
    json.dump(json_list, write_f)

with open('task_5_7_file.json') as read_f:
    print(f'Объект Json: {json.load(read_f)}')
