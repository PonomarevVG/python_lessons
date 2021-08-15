# Задание 5.5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

print('Вводите последовательно числа, которые будут записываться в файл task_5_5_file.txt .'
      'Ввод пустой строки будет означать окончание записи')
line = ''
with open('task_5_5_file.txt', 'w') as write_f:
    while True:
        s = input('Введите число для записи в файл: ')
        if s == '':
            break
        line += s + ' '
    print(line.strip('\n'), file=write_f)

sum = 0.0
with open('task_5_5_file.txt') as read_f:
    values = read_f.readline().split(' ')

for value in values:
    sum += float(value) if value.replace('.', '').isdigit() else 0.0
print(f'Сумма чисел в файле = {sum}')
