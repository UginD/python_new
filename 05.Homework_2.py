# 2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


with open('05.Homework_2.txt', 'r', encoding='utf-8') as my_file:
    content = my_file.readlines()
    len_str = len(content)
    print(f'Количество строк в файле: {len_str}')
    count = 0
    for i in content:
        b = i.split()
        sum_words = len(b)
        count += 1
        print(f'Количество слов в строке {count}: {sum_words}')

