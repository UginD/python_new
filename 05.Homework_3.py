# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.


with open('05.Homework_3.txt', 'r', encoding='utf-8') as my_file:
    b = []
    d = []
    for i in my_file:
        a = i.split()
        if float(a[1]) < 20000.0:
            d.append(a[0])
        b.append(a[1])
    c = round(sum([float(x) for x in b]) / len(b), 2)
    print(f'Сотрудники с окладом менее 20 тыс.:\n{d}')
    print(f'Средний доход сотрудников составляет: {c}')