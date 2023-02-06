# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и
# считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_interpreter = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'}
test = []

with open('05.Homework_04.txt', 'r', encoding='utf-8') as my_file:
    a = my_file.readlines()
    for i in a:
        b = i.split()  # список элементов = каждая строка
        for j in b:
            if j in my_interpreter:
                b[b.index(j)] = my_interpreter[j]
        c = ' '.join(b)
        test.append(c + '\n')
    with open('05.Homework_04_2.txt', 'w', encoding='utf-8') as f:
        x = f.writelines(test)
