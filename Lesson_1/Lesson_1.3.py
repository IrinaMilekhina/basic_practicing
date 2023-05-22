'''
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на
экран отдельной строкой для каждого из чисел в интервале от 1 до 100
'''

list_till = 30    # до какого числа составлять список
word_root = " процент"
exceptions = [11, 12, 13, 14]

# realisation with if
ov_list = [0, 5, 6, 7, 8, 9]    # если число оканчивается на это, то употребляется окончание "ов"
a_list = [2, 3, 4]    # если на это - окончание "а". В остальных случаях окончание нулевое
ov_ending = "ов"
a_ending = "а"

for number in range(list_till + 1):
    ending_check = number % 10
    if ending_check in ov_list or number in exceptions:
        print(str(number) + word_root + ov_ending)
    elif ending_check in a_list:
        print(str(number) + word_root + a_ending)
    else:
        print(str(number) + word_root)

# realisation with dictionary
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

for number in range(list_till + 1):
    ending_check = number % 10
    if number in exceptions:
        print(str(number) + word_root + str(word_ending[0]))
    else:
        print(str(number) + word_root + str(word_ending[ending_check]))
