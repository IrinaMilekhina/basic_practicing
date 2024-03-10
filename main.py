"""
Домашнее задание:
1. Прочитать данные из текстового файла
2. Проанализировать данные. Подсчитать сколько слов в тексте, сколько раз встречается каждое слово
3. Сформировать словарь с результатом анализа вида
{"word": times[int]}
4. Сериализовать словаpь в json формат
5. Записать результат в json файл
6. Создать минимум 1 тест на написанный код


В начале пиши просто работающий код и не забывай делать коммиты на каждую логическую область
Затем почисти свой код, подумай над функциями, помни про DRY (коммиты!)
Дополни код комментарийми (коммиты!)

После выполнения тебе необходимо на гите создать pull request и дать мне ссылку
"""
import string
import json
import os


def text_analysis(txt_file_path: str):
    '''
    Makes analysis on unique words repeating in a chosen .txt file
    :param txt_file_path: relative file path needed (root - current folder)
    :return: dictionary in format {unique_word_1 (str): number of repetition (int)}
    '''
    try:
        initial_file_path = os.path.abspath(txt_file_path)
        word_repeating = {}
        with open(initial_file_path, 'r', encoding='utf-8') as text:
            for line in text:
                for punc_mark in string.punctuation:
                    if punc_mark in line:
                        line = line.replace(punc_mark, '').replace('—', '')
                content = line.lower().split()
                for word in content:
                    if word not in word_repeating:
                        word_repeating[word] = 1
                    else:
                        word_repeating[word] += 1
        return word_repeating
    except FileNotFoundError as error:
        return f'{error} try to check file name or relative path'


root_dir = r'/home/im/thetribalme/basic_practicing'


print(text_analysis('test.txt'))
# def text_analysis(txt_file_path: str, json_file_name: str = None):
#     initial_file_path = os.path.abspath(txt_file_path)
#     word_count = 0
#     word_repeating = {}
#     if json_file_name is None:
#         json_file_name = os.path.basename(initial_file_path).strip('.txt')
#     result_file_name = f'{json_file_name}.json'
#     print(result_file_name)
#
# text_analysis('fairytales/in-text.txt', 'nomnom')
    # with open(initial_file_path, 'r', encoding='utf-8') as text:
    #     for line in text:
    #         for punc_mark in string.punctuation:
    #             if punc_mark in line:
    #                 line = line.replace(punc_mark, '').replace('—', '')
    #         content = line.lower().split()
    #         for word in content:
    #             word_count += 1
    #             if word not in word_repeating:
    #                 word_repeating[word] = 1
    #             else:
    #                 word_repeating[word] += 1
    # print(f"Words in total: {word_count}")
    # with open(json_file_name, 'w', encoding='utf-8') as tale_analysis:
    #     json.dump(word_repeating, tale_analysis)



# file_name = "in_text.txt"
# json_file_name = 'tale_analysis.json'
#
# with open(file_name, 'r', encoding='utf-8') as tale:
#     for line in tale:
#         for punc_mark in string.punctuation:
#             if punc_mark in line:
#                 line = line.replace(punc_mark, '').replace('—', '')
#         content = line.lower().split()
#         for word in content:
#             word_count += 1
#             if word not in word_repeating:
#                 word_repeating[word] = 1
#             else:
#                 word_repeating[word] += 1
# print(f"Words in total: {word_count}")
# with open(json_file_name, 'w', encoding='utf-8') as tale_analysis:
#     json.dump(word_repeating, tale_analysis)
#
# # testing
# try:
#     with open(json_file_name, 'r') as test:
#         print("Result file exists")
# except FileNotFoundError:
#     print("Result file doesn't exist")
