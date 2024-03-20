# ______________________________________________________________________________________
# Задачи 1-3. Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях
# слов длиннее 6 символов для каждого файла (для файлов в формате JSON и XML)


# Создаем функцию открытия файла JSON, возвращаем список новостей
def open_json_file(file):
    import json
    with open(file, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    data_list = data.get('rss').get('channel').get('items')
    news = []
    for i in data_list:
        news_description = i.get('description')
        news.append(news_description)
    return news

# Создаем функцию открытия файла XML, возвращаем список новостей
def open_xml_file(file):
    import xml.etree.ElementTree as ET
    tree = ET.parse(file)
    root = tree.getroot()
    common_list = root.findall('channel/item/description')
    news = []
    for row in common_list:
        news.append(row.text)
    return news

# Создаем функцию печати 10 наиболее часто встречающихся слов длиной более 6 символов
def print_most_popular_words(news):
    news_list_descriptions = []

    for i in news:
        s = i.split()
        news_list_descriptions += s

    # Создаем список слов длиной более 6 символов, встречающихся в новостях (включая повторяющиеся)
    words_list = []

    for i in news_list_descriptions:
        if len(i) > 6:
            words_list.append(i)

    # Создаем список уникальных слов длиной более 6 символов (преобразуя список во множество)
    unique_words = set(words_list)

    # Cоздаем словарь, где ключ - название слова, а значение - количество его упоминаний в тексте (метод count)
    result_list = {}

    for word in unique_words:
        result_list[word] = words_list.count(word)

    # Создаем итоговый список списков из словаря, в котором сортируем слова по количеству упоминаний от наиболее часто упоминаемых до наиболее редко упоминаемых)
    result_list = sorted(list(result_list.items()), key=lambda x: x[1], reverse=True)

    # Выводим на печать 10 первых элементов отсортированного списка списков
    print('Список из 10 наиболее популярных слов, встречающихся в списке новостей: ')

    for i in result_list[:10]:
        print(f'Слово:       {i[0]}\n'
              f'Встречается: {i[1]} раз\n'
              f'_______________________')

# Вызываем созданные функции, тестируем их работоспособность
print_most_popular_words(open_json_file('newsafr.json'))
print_most_popular_words(open_xml_file('newsafr.xml'))

