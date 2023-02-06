# 5.  Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('05.Homework_05.txt', 'w') as my_file:
    set_numbers = my_file.write('10 20 30 40 50')

with open('05.Homework_05.txt', 'r') as new_file:
    my_list = new_file.readline()
    a = list(map(int, str(my_list).split()))
    total = 0
    for i in a:
        total += i
    print(f'Сумма чисел в файле "05.Homework_05.txt" составляет: {total}')
