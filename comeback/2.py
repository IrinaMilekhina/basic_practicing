"""
Input: 8
Result:
   **
  ****
 ******
********

Input: 3
Result:
 *
***

Input: 0
Result:
-

Input: -3
Result:
***
 *

Input: 1
Result:
*
"""

user_input = int(input('type your number: '))
# default value
start = 1
finish = user_input+1
if user_input == 0:
    print('-')
elif user_input < 0:
    for i in range(user_input, 0, 2):
        index = i * -1
        print(('*' * index).center(user_input*-1))
for i in range(start, finish, 2):
    index = i
    if user_input % 2 == 0:
        index += 1
    print(('*' * index).center(user_input))
