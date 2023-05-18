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

# тут бы я фиганула f-string, но по курсу мы еще не знаем этого
# в методичке говорится, что константы прнято печатать в верхнем регистре. Значит ли это, что лучше делать
# SECONDS_PER_DAY и тд? И часто ли так делают на работе?
