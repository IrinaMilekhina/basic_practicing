'''
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
'''

seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60

duration = int(input("Put duration in seconds here \n"))

days = duration // seconds_per_day
hours = duration % seconds_per_day // seconds_per_hour
minutes = duration % seconds_per_hour // seconds_per_minute
seconds = duration % seconds_per_minute

print(str(days) + " d. " + str(hours) + " h. " + str(minutes) + " m. " + str(seconds) + " s.")

# second realisation variant using lists
time_list = [60, 60, 24, 24]
word_list = [' s.', ' m.', ' h.', ' d.']
result_list = []

duration = int(input("Put duration in seconds here \n"))

for i, v in enumerate(time_list):
    result_list.append(str(duration % v) + word_list[i])
    duration //= v

len_list = len(result_list) - 1
while len_list >= 0:
    print(result_list[len_list], end=" ")
    len_list -= 1
