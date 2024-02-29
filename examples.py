def hello_world():
    print('Hello world!')


print(type(hello_world))

# мы можем хранить функцию в переменной
hello = hello_world
hello()


# определять ф-цию внутри другой ф-ции
def wrapper_function():
    def hello_world():
        print('Hello world from wrapper_function!')

    hello_world()


wrapper_function()


# передавать функции в качестве аргументов и возвращать их из других функций
def higher_order(func):
    print('Получена функция {} в качестве аргумента'.format(func))
    func()
    return func


higher_order(hello_world)


# пример декоратора
def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')

    return wrapper


@decorator_function
def hello_world():
    print('Hello world!')


hello_world()


# @ является синтаксическим сахаром для hello_world = decorator_function(hello_world)

def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')


fetch_webpage()


# Используем аргументы и возвращаем значения
def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)


# Декораторы с аргументами
def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


@benchmark(iters=10)
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)

"""
Доработать код создав функции и 1 декоратор (на данный момент это просто практика, 
можешь выбрать любой)
Задание со здездочкой:
https://tproger.ru/translations/demystifying-decorators-in-python
разобраться с двумя последними блоками статьи
Декораторы с аргументами, Объекты-декораторы
"""