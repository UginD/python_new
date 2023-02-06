# 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий
#  - название предмета и
#  - общее количество занятий по нему.
#  Вывести его на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


new_dict = {}
with open('05.Homework_06.txt', 'r', encoding='utf-8') as my_file:
    a = my_file.readlines()
    for i in a:
        b = i.replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('—', '')
        num = sum([int(x) for x in b.split() if x.isdigit()])
        c = b.split(':')
        my_dict = {c[0]: num}
        new_dict.update(my_dict)
    print(new_dict)
