'''
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на
экран отдельной строкой для каждого из чисел в интервале от 1 до 100
'''

list_till = 100    # до какого числа составлять список
word_root = " процент"
number_list = []
idx = 0
# ты мне разрешила делать через словарь)
word_ending = {
    0: "ов",
    1: "",
    2: "а",
    3: "а",
    4: "а",
    5: "ов",
    6: "ов",
    7: "ов",
    8: "ов",
    9: "ов"
}

for idx in range(list_till):
    number_list.append(idx+1)

for idx in range(len(number_list)):
    tmp = number_list[idx] % 10
    print(str(number_list[idx]) + word_root + str(word_ending[tmp]))
