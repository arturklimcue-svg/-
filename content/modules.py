# -*- coding: utf-8 -*-
"""Контент всех модулей курса Python."""

MODULES = [
    {
        "id": 0,
        "title": "Вводный модуль",
        "theory": """# Вводный модуль

## Что такое Python?
Python — интерпретируемый язык программирования высокого уровня, созданный Гвидо ван Россумом в 1991 году.

## Преимущества Python:
- Простой и читаемый синтаксис
- Кроссплатформенность
- Огромное количество библиотек
- Широко используется: веб, данные, AI, автоматизация

## Установка
Скачайте Python с python.org. При установке отметьте **Add Python to PATH**.

## Первая программа
```python
print("Hello, World!")
```

## Типы данных (базовые)
| Тип | Пример |
|-----|--------|
| int | 42 |
| float | 3.14 |
| str | "привет" |
| bool | True / False |

## Переменные
```python
name = "Артём"
age = 20
pi = 3.14
```

Имя переменной: буквы, цифры, `_`; не может начинаться с цифры; чувствительно к регистру.""",
        "examples": [
            {
                "code": 'print("Hello, World!")\nprint("Привет, Python!")',
                "explain": "Функция print() выводит текст на экран."
            },
            {
                "code": 'name = "Артём"\nage = 20\nprint(name, age)',
                "explain": "Создаём переменные и выводим их."
            },
            {
                "code": 'x = 10\ny = 3\nprint(x + y, x - y, x * y, x / y)\nprint(x // y, x % y, x ** 2)',
                "explain": "Арифметические операции: +, -, *, /, // (целочисленное), % (остаток), ** (степень)."
            }
        ],
        "quiz": [
            {"q": "Кто создал Python?", "options": ["Деннис Ритчи", "Гвидо ван Россум", "Джеймс Гослинг", "Бьёрн Страуструп"], "correct": 1},
            {"q": "Какой тип данных у значения 3.14?", "options": ["int", "str", "float", "bool"], "correct": 2},
            {"q": "Какой оператор вычисляет остаток от деления?", "options": ["/", "//", "%", "**"], "correct": 2},
            {"q": "Какое имя переменной НЕВЕРНО?", "options": ["my_var", "2name", "_temp", "Name"], "correct": 1},
            {"q": "Что выведет print(7 // 2)?", "options": ["3.5", "3", "4", "1"], "correct": 1}
        ]
    },
    {
        "id": 1,
        "title": "Практика GIT. Базовые структуры данных",
        "theory": """# Практика GIT и базовые структуры данных

## Git — система контроля версий
Git отслеживает изменения в файлах и позволяет вернуться к любому моменту истории.

## Основные команды Git:
```bash
git init              # инициализация репозитория
git add .             # добавить файлы в индекс
git commit -m "msg"   # зафиксировать изменения
git push              # отправить на удалённый сервер
git pull              # забрать изменения
git status            # состояние репозитория
git log               # история коммитов
```

## Базовые структуры данных

### Список (list) — упорядоченная, изменяемая коллекция
```python
fruits = ["яблоко", "банан", "вишня"]
fruits.append("апельсин")
print(fruits[0])  # яблоко
```

### Кортеж (tuple) — упорядоченная, НЕИЗМЕНЯЕМАЯ
```python
point = (10, 20)
```

### Множество (set) — без дубликатов
```python
nums = {1, 2, 3, 3}  # {1, 2, 3}
```

### Словарь (dict) — пары ключ-значение
```python
person = {"name": "Анна", "age": 25}
print(person["name"])
```""",
        "examples": [
            {
                "code": 'fruits = ["яблоко", "банан"]\nfruits.append("вишня")\nfruits[0] = "груша"\nprint(fruits)\nprint(len(fruits))',
                "explain": "Список: добавление append(), изменение по индексу, длина len()."
            },
            {
                "code": 'point = (3, 4)\n# point[0] = 10  # Ошибка! Кортеж нельзя менять\nx, y = point\nprint(x, y)',
                "explain": "Кортеж неизменяем. Можно распаковать в переменные."
            },
            {
                "code": 'scores = {"математика": 5, "физика": 4}\nscores["информатика"] = 5\nprint(scores.get("химия", "нет оценки"))\nfor k, v in scores.items():\n    print(k, v)',
                "explain": "Словарь: добавление, get() с значением по умолчанию, перебор items()."
            },
            {
                "code": 'unique = {1, 2, 2, 3, 3, 3}\nprint(unique)\nunique.add(4)\nprint(2 in unique)',
                "explain": "Множество автоматически убирает дубликаты. Оператор in проверяет наличие."
            }
        ],
        "quiz": [
            {"q": "Какая структура данных неизменяема?", "options": ["list", "dict", "tuple", "set"], "correct": 2},
            {"q": "Как добавить элемент в список?", "options": ["list.add()", "list.append()", "list.insert_end()", "list.push()"], "correct": 1},
            {"q": "Что выведет d = {'a': 1}; print(d.get('b', 0))?", "options": ["None", "Ошибка", "0", "'b'"], "correct": 2},
            {"q": "Какая коммитит изменения в Git?", "options": ["git add", "git push", "git commit", "git pull"], "correct": 2},
            {"q": "Что выведет {1, 2, 2, 3}?", "options": ["[1, 2, 2, 3]", "{1, 2, 3}", "{1, 1, 2, 3}", "Ошибка"], "correct": 1}
        ]
    },
    {
        "id": 2,
        "title": "Основные операторы",
        "theory": """# Основные операторы

## Операторы сравнения
| Оператор | Значение |
|----------|----------|
| == | равно |
| != | не равно |
| > | больше |
| < | меньше |
| >= | больше или равно |
| <= | меньше или равно |

## Логические операторы
- `and` — И (оба True)
- `or` — ИЛИ (хотя бы одно True)
- `not` — НЕ (инвертирует)

## Операторы присваивания
```python
x = 5
x += 2   # x = x + 2
x -= 1   # x = x - 1
x *= 3   # x = x * 3
x /= 2   # x = x / 2
```

## Условия if / elif / else
```python
age = 18
if age >= 18:
    print("Совершеннолетний")
elif age >= 16:
    print("16+")
else:
    print("Меньше 16")
```

## Циклы
```python
for i in range(5):   # 0 1 2 3 4
    print(i)

while x > 0:
    x -= 1
```

## Управляющие операторы
- `break` — выйти из цикла
- `continue` — пропустить итерацию
- `pass` — пустое тело""",
        "examples": [
            {
                "code": 'x = 10\nif x > 5 and x < 20:\n    print("x в диапазоне (5, 20)")',
                "explain": "Логическое И: оба условия должны быть истинны."
            },
            {
                "code": 'for i in range(1, 6):\n    if i == 3:\n        continue\n    print(i)',
                "explain": "continue пропускает третью итерацию: выведет 1 2 4 5."
            },
            {
                "code": 'for i in range(10):\n    if i == 5:\n        break\n    print(i)',
                "explain": "break полностью прерывает цикл при i == 5."
            },
            {
                "code": 'n = 7\nif n % 2 == 0:\n    print("Чётное")\nelse:\n    print("Нечётное")',
                "explain": "Остаток от деления на 2 определяет чётность."
            }
        ],
        "quiz": [
            {"q": "Что вернёт выражение 5 > 3 and 2 > 4?", "options": ["True", "False", "None", "Ошибка"], "correct": 1},
            {"q": "Чему равно x после: x = 5; x += 3?", "options": ["2", "5", "8", "3"], "correct": 2},
            {"q": "Что делает break в цикле?", "options": ["Пропускает итерацию", "Прерывает цикл", "Завершает программу", "Ничего"], "correct": 1},
            {"q": "range(3) генерирует...", "options": ["1 2 3", "0 1 2", "0 1 2 3", "3"], "correct": 1},
            {"q": "Какой оператор означает «не равно»?", "options": ["=", "==", "!=", "<>="], "correct": 2}
        ]
    },
    {
        "id": 3,
        "title": "Подробнее о функциях",
        "theory": """# Подробнее о функциях

## Определение функции
```python
def greet(name):
    return f"Привет, {name}!"
```

## Параметры
```python
def power(base, exp=2):      # exp по умолчанию = 2
    return base ** exp

def total(*args):            # произвольное число аргументов
    return sum(args)

def info(**kwargs):          # именованные аргументы
    print(kwargs)
```

## return vs print
- `return` — возвращает значение в вызывающий код
- `print` — только выводит на экран

## Область видимости
- **Локальная** — внутри функции
- **Глобальная** — на уровне модуля
- `global x` — доступ к глобальной переменной

## Lambda-функции
```python
square = lambda x: x ** 2
print(square(5))  # 25
```

## Декораторы
```python
def decorator(fn):
    def wrapper(*args):
        print("Вызов функции")
        return fn(*args)
    return wrapper

@decorator
def say_hi():
    print("Hi!")
```

## Рекурсия
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```""",
        "examples": [
            {
                "code": 'def greet(name, age=18):\n    return f"{name}, тебе {age} лет"\n\nprint(greet("Анна"))\nprint(greet("Борис", 30))',
                "explain": "Параметр по умолчанию age=18, но его можно переопределить."
            },
            {
                "code": 'def calc(*numbers, op="+"):\n    if op == "+":\n        return sum(numbers)\n    if op == "*":\n        result = 1\n        for n in numbers:\n            result *= n\n        return result\n\nprint(calc(1, 2, 3))\nprint(calc(2, 3, 4, op="*"))',
                "explain": "*args собирает позиционные аргументы в кортеж."
            },
            {
                "code": 'fact = lambda n: 1 if n <= 1 else n * fact(n - 1)\nprint(fact(5))',
                "explain": "Lambda с рекурсией — вычисляет факториал."
            },
            {
                "code": 'def cache(fn):\n    store = {}\n    def wrapper(x):\n        if x not in store:\n            store[x] = fn(x)\n        return store[x]\n    return wrapper\n\n@cache\ndef slow_square(x):\n    return x * x\n\nprint(slow_square(4))\nprint(slow_square(4))',
                "explain": "Декоратор кеширует результаты функции."
            }
        ],
        "quiz": [
            {"q": "Что возвращает функция без return?", "options": ["0", "None", "False", "Ошибка"], "correct": 1},
            {"q": "Что делает *args?", "options": ["Перемножает аргументы", "Собирает аргументы в кортеж", "Умножает на звёздочку", "Ничего"], "correct": 1},
            {"q": "Что такое lambda?", "options": ["Переменная", "Анонимная функция", "Цикл", "Класс"], "correct": 1},
            {"q": "Какой ключевое слово позволяет обратиться к глобальной переменной?", "options": ["local", "global", "outer", "static"], "correct": 1},
            {"q": "Что выведет: def f(x=1): return x; print(f())?", "options": ["0", "1", "None", "Ошибка"], "correct": 1}
        ]
    },
    {
        "id": 4,
        "title": "Модули и пакеты",
        "theory": """# Модули и пакеты

## Модуль
Модуль — это файл с Python-кодом (.py). Любая переменная/функция/класс доступна как атрибут.

```python
import math
print(math.sqrt(16))  # 4.0

from random import randint
print(randint(1, 10))

import os as operating_system
```

## Создание своего модуля
```python
# mymodule.py
def hello():
    return "Hello from module!"

PI = 3.14159
```
```python
# main.py
import mymodule
print(mymodule.PI)
```

## Пакет
Пакет — директория с `__init__.py`:
```
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

## Полезные стандартные модули
- `math` — математика
- `random` — случайные числа
- `os` — работа с ОС
- `sys` — системные параметры
- `datetime` — дата и время
- `json` — работа с JSON
- `re` — регулярные выражения

## pip
```bash
pip install requests
pip list
pip uninstall requests
```""",
        "examples": [
            {
                "code": 'import math\n\nprint(math.pi)\nprint(math.sqrt(144))\nprint(math.ceil(4.1), math.floor(4.9))',
                "explain": "Модуль math: число π, квадратный корень, округление вверх/вниз."
            },
            {
                "code": 'from random import randint, choice\n\nprint(randint(1, 100))\nprint(choice(["яблоко", "груша", "вишня"]))',
                "explain": "Импорт конкретных функций из модуля random."
            },
            {
                "code": 'import datetime\n\nnow = datetime.datetime.now()\nprint(now.strftime("%d.%m.%Y %H:%M"))',
                "explain": "Модуль datetime: текущая дата и форматирование."
            },
            {
                "code": 'import json\n\ndata = {"name": "Анна", "age": 25}\ns = json.dumps(data, ensure_ascii=False)\nprint(s)\nback = json.loads(s)\nprint(back["age"])',
                "explain": "json.dumps() → строка, json.loads() → объект Python."
            }
        ],
        "quiz": [
            {"q": "Как импортировать только функцию sqrt из math?", "options": ["import sqrt from math", "from math import sqrt", "from sqrt import math", "math.sqrt()"], "correct": 1},
            {"q": "Что нужно в директории пакета?", "options": ["main.py", "__init__.py", "setup.py", "package.json"], "correct": 1},
            {"q": "Какая команда устанавливает пакет?", "options": ["python install X", "pip install X", "get X", "apt install X"], "correct": 1},
            {"q": "Что делает json.dumps()?", "options": ["Распарсивает JSON", "Преобразует объект в строку JSON", "Удаляет JSON", "Читает файл"], "correct": 1},
            {"q": "Какое расширение у модуля Python?", "options": [".txt", ".mod", ".py", ".pyc"], "correct": 2}
        ]
    },
    {
        "id": 5,
        "title": "Пространство имен",
        "theory": """# Пространство имён (Namespaces)

## Что это?
Пространство имён — это структура, которая хранит имена переменных и связывает их со значениями.

## Уровни пространства имён
1. **Built-in** — встроенные функции (`print`, `len`, `int`)
2. **Global** — имена на уровне модуля
3. **Local** — имена внутри функции

## Порядок поиска (LEGB)
Python ищет имя по цепочке:
**L**ocal → **E**nclosing → **G**lobal → **B**uilt-in

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()  # local
```

## Функции — объекты первого класса
```python
def foo():
    return 42

bar = foo      # копия ссылки
print(bar())   # 42
```

## Замыкания (closures)
```python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
```

`nonlocal` — обращение к переменной изEnclosing-области.""",
        "examples": [
            {
                "code": 'x = "global"\n\ndef f():\n    x = "local"\n    print(x)\n\nf()\nprint(x)',
                "explain": "Внутри функции создаётся ЛОКАЛЬНАЯ x, глобальная не меняется."
            },
            {
                "code": 'def outer():\n    msg = "привет"\n    def inner():\n        print(msg)\n    inner()\n\nouter()',
                "explain": "Inner-функция видит переменную из Enclosing-области."
            },
            {
                "code": 'def make_adder(n):\n    def adder(x):\n        return x + n\n    return adder\n\nadd5 = make_adder(5)\nprint(add5(10))  # 15',
                "explain": "Замыкание: adder запоминает n из внешней функции."
            },
            {
                "code": 'def make_counter():\n    count = 0\n    def inc():\n        nonlocal count\n        count += 1\n        return count\n    return inc\n\nc = make_counter()\nprint(c(), c(), c())  # 1 2 3',
                "explain": "nonlocal позволяет менять переменную Enclosing-области."
            }
        ],
        "quiz": [
            {"q": "Какой порядок поиска имён (LEGB)?", "options": ["Global→Local→Built-in→Enclosing", "Local→Enclosing→Global→Built-in", "Built-in→Global→Local→Enclosing", "Local→Global→Enclosing→Built-in"], "correct": 1},
            {"q": "Что делает nonlocal?", "options": ["Создаёт глобальную переменную", "Обращается к переменной Enclosing-области", "Удаляет переменную", "Импортирует модуль"], "correct": 1},
            {"q": "Замыкание — это...", "options": ["Цикл", "Функция, помнящая окружение", "Класс", "Ошибка"], "correct": 1},
            {"q": "Где ищется имя в первую очередь?", "options": ["Global", "Built-in", "Local", "Enclosing"], "correct": 2},
            {"q": "Функция как значение можно...", "options": ["Только вызывать", "Присвоить переменной", "Удалить", "Умножить"], "correct": 1}
        ]
    },
    {
        "id": 6,
        "title": "Классы и объекты",
        "theory": """# Классы и объекты (ООП)

## Класс — шаблон для создания объектов
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name}: гав!"

rex = Dog("Рекс", 3)
print(rex.bark())
```

## Методы
- `__init__` — конструктор (инициализация)
- `__str__` — строковое представление
- `__repr__` — для отладки
- `__eq__` — сравнение ==

## Атрибуты класса vs экземпляра
```python
class Cat:
    species = "кошка"      # атрибут класса (общий)

    def __init__(self, name):
        self.name = name   # атрибут экземпляра
```

## Инкапсуляция
```python
class Bank:
    def __init__(self):
        self.__balance = 0   # «приватный»

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
```

## Магические методы
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)
```""",
        "examples": [
            {
                "code": 'class Dog:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n    def bark(self):\n        return f"{self.name}: гав!"\n\nrex = Dog("Рекс", 3)\nprint(rex.name, rex.age)\nprint(rex.bark())',
                "explain": "Класс Dog, конструктор __init__, метод bark()."
            },
            {
                "code": 'class Counter:\n    count = 0\n\n    def __init__(self):\n        Counter.count += 1\n\na = Counter()\nb = Counter()\nprint(Counter.count)  # 2',
                "explain": "Атрибут класса count хранится один на все экземпляры."
            },
            {
                "code": 'class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n\n    def __str__(self):\n        return f"({self.x}, {self.y})"\n\n    def __add__(self, other):\n        return Point(self.x + other.x, self.y + other.y)\n\np = Point(1, 2) + Point(3, 4)\nprint(p)  # (4, 6)',
                "explain": "Магические методы __str__ и __add__ делают объект удобным."
            },
            {
                "code": 'class Employee:\n    def __init__(self, name, salary):\n        self.name = name\n        self.__salary = salary\n\n    def get_salary(self):\n        return self.__salary\n\ne = Employee("Иван", 50000)\nprint(e.get_salary())\n# print(e.__salary)  # AttributeError',
                "explain": "__salary — «приватный» атрибут, доступ только через метод."
            }
        ],
        "quiz": [
            {"q": "Как называется метод инициализации объекта?", "options": ["__new__", "__init__", "__start__", "init"], "correct": 1},
            {"q": "self в методе класса — это...", "options": ["Класс", "Экземпляр", "Модуль", "Функция"], "correct": 1},
            {"q": "Что делает __str__?", "options": ["Создаёт строку", "Возвращает человекочитаемое представление", "Копирует объект", "Удаляет объект"], "correct": 1},
            {"q": "Двойное подчёркивание в имени атрибута означает...", "options": ["Глобальный", "Приватный (name mangling)", "Статический", "Временный"], "correct": 1},
            {"q": "Атрибут класса хранится...", "options": ["В каждом объекте", "Один на класс", "В функции", "Нигде"], "correct": 1}
        ]
    },
    {
        "id": 7,
        "title": "Наследование классов",
        "theory": """# Наследование классов

## Базовый синтаксис
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):          # Dog наследует Animal
    def speak(self):        # переопределение
        return "Гав!"

class Puppy(Dog):           # множественное: class C(A, B)
    pass
```

## super()
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # вызов конструктора родителя
        self.breed = breed
```

## Проверка типов
```python
isinstance(dog, Dog)    # True
issubclass(Dog, Animal) # True
```

## Абстрактные классы (abc)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```
Нельзя создать экземпляр Shape — только наследников с реализацией area().

## МИКСИН — класс-набор поведения для встраивания""",
        "examples": [
            {
                "code": 'class Animal:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return "..."\n\nclass Cat(Animal):\n    def speak(self):\n        return "Мяу!"\n\nc = Cat("Барсик")\nprint(c.name, "->", c.speak())',
                "explain": "Cat наследует __init__ и переопредел speak()."
            },
            {
                "code": 'class Dog(Animal):\n    def __init__(self, name, breed):\n        super().__init__(name)\n        self.breed = breed\n\n    def info(self):\n        return f"{self.name} — {self.breed}"\n\nd = Dog("Шарик", "дворняга")\nprint(d.info())',
                "explain": "super().__init__() вызывает конструктор родителя."
            },
            {
                "code": 'class A:\n    def hello(self):\n        return "A"\n\nclass B:\n    def hello(self):\n        return "B"\n\nclass C(A, B):\n    pass\n\nprint(C().hello())  # A — MRO: C → A → B',
                "explain": "Множественное наследование, порядок MRO."
            },
            {
                "code": 'from abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self):\n        pass\n\nclass Circle(Shape):\n    def __init__(self, r):\n        self.r = r\n    def area(self):\n        return 3.14 * self.r ** 2\n\nprint(Circle(5).area())',
                "explain": "Абстрактный базовый класс задаёт интерфейс."
            }
        ],
        "quiz": [
            {"q": "Что делает super()?", "options": ["Создаёт объект", "Обращается к родительскому классу", "Удаляет класс", "Проверяет тип"], "correct": 1},
            {"q": "class Dog(Animal) означает...", "options": ["Dog — родитель", "Animal наследует Dog", "Dog наследует Animal", "Ничего"], "correct": 2},
            {"q": "issubclass(Dog, Animal) вернёт...", "options": ["False", "True", "None", "Ошибка"], "correct": 1},
            {"q": "Абстрактный класс нельзя...", "options": ["Наследовать", "Создать экземпляр", "Импортировать", "Описать"], "correct": 1},
            {"q": "Что такое MRO?", "options": ["Метод родителя", "Method Resolution Order", "Модель объектов", "Ошибка"], "correct": 1}
        ]
    },
    {
        "id": 8,
        "title": "Работа с файлами и форматированный вывод",
        "theory": """# Работа с файлами и форматированный вывод

## Чтение и запись
```python
# Запись
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Привет\\n")
    f.writelines(["строка1\\n", "строка2\\n"])

# Чтение
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()        # весь файл
    lines = f.readlines()     # список строк
```

## Режимы открытия
| Режим | Описание |
|-------|----------|
| r | чтение (по умолчанию) |
| w | запись (перезаписывает!) |
| a | дозапись в конец |
| rb/wb | бинарный режим |

## with — гарантирует закрытие файла

## JSON, CSV
```python
import json, csv
```

## Форматированный вывод

### f-строки (рекомендуется)
```python
name = "Анна"
print(f"Привет, {name}! {2+2=}")
print(f"{3.14159:.2f}")   # 3.14
print(f"{'лево':<10}|")   # выравнивание
```

### format()
```python
"{0} {1}".format("a", "b")
```

### %
```python
"%s %d" % ("a", 42)
```""",
        "examples": [
            {
                "code": 'with open("example.txt", "w", encoding="utf-8") as f:\n    f.write("Строка 1\\n")\n    f.write("Строка 2\\n")\n\nwith open("example.txt", "r", encoding="utf-8") as f:\n    print(f.read())',
                "explain": "with автоматически закрывает файл."
            },
            {
                "code": 'with open("log.txt", "a", encoding="utf-8") as f:\n    f.write("Новая запись\\n")',
                "explain": "Режим 'a' — дозапись в конец файла."
            },
            {
                "code": 'import json\n\ndata = {"курс": "Python", "модули": 23}\nwith open("data.json", "w", encoding="utf-8") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n\nwith open("data.json", "r", encoding="utf-8") as f:\n    loaded = json.load(f)\nprint(loaded["курс"])',
                "explain": "json.dump → в файл, json.load ← из файла."
            },
            {
                "code": 'name = "Мир"\npi = 3.14159\nn = 42\n\nprint(f"Привет, {name}!")\nprint(f"Pi = {pi:.2f}")\nprint(f"Число: {n:05d}")\nprint(f"{n=}")\nprint("Привет, {}!".format(name))\nprint("%s = %d" % ("n", n))',
                "explain": "f-строки, format() и %-форматирование."
            }
        ],
        "quiz": [
            {"q": "Какой режим открывает файл на ПЕРЕЗАПИСЬ?", "options": ["r", "a", "w", "x+"], "correct": 2},
            {"q": "Что делает with open(...)?", "options": ["Читает файл", "Автоматически закрывает файл", "Удаляет файл", "Копирует файл"], "correct": 1},
            {"q": "Как в f-строке вывести число с 2 знаками после точки?", "options": ["{x:2}", "{x:.2f}", "{x,2}", "{x!r2}"], "correct": 1},
            {"q": "json.dump() записывает...", "options": ["В строку", "В файл", "В список", "В консоль"], "correct": 1},
            {"q": "Режим 'a' открывает файл...", "options": ["На чтение", "На дозапись", "Создаёт новый", "Удаляет"], "correct": 1}
        ]
    },
    {
        "id": 10,
        "title": "Инструменты функционального программирования",
        "theory": """# Функциональное программирование

## map, filter, reduce
```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, nums))     # [1, 4, 9, 16, 25]
evens   = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
total   = reduce(lambda a, b: a + b, nums)     # 15
```

## Генераторы
```python
squares = (x**2 for x in range(10))  # не вычисляет сразу

def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

## sorted с key
```python
words = ["banana", "pie", "kiwi"]
sorted(words, key=len)
sorted(words, key=str.lower, reverse=True)
```

## zip, enumerate
```python
list(zip([1,2], ["a","b"]))   # [(1,'a'), (2,'b')]
list(enumerate("abc"))        # [(0,'a'), (1,'b'), (2,'c')]
```

## any / all
```python
any([False, True])  # True
all([True, True])   # True
```

## Компрессии списков
```python
[x**2 for x in range(10) if x % 2 == 0]
```""",
        "examples": [
            {
                "code": 'nums = [1, 2, 3, 4, 5, 6]\n\nprint(list(map(lambda x: x * 2, nums)))\nprint(list(filter(lambda x: x % 2 == 0, nums)))',
                "explain": "map применяет функцию к каждому элементу, filter оставляет подходящие."
            },
            {
                "code": 'from functools import reduce\n\nnums = [1, 2, 3, 4]\nprint(reduce(lambda a, b: a + b, nums))  # 10\nprint(reduce(lambda a, b: a * b, nums))  # 24',
                "explain": "reduce сворачивает последовательность в одно значение."
            },
            {
                "code": 'def fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a + b\n\nprint(list(fib(10)))',
                "explain": "Генератор yield — ленивая вычисляемая последовательность."
            },
            {
                "code": 'people = [("Анна", 30), ("Борис", 25), ("Вера", 35)]\n\nprint(sorted(people, key=lambda p: p[1]))\nprint(list(zip(["a", "b"], [1, 2])))\nprint(list(enumerate("abc", start=1)))',
                "explain": "sorted + key, zip — параллельный перебор, enumerate — с индексом."
            },
            {
                "code": 'nums = range(10)\n\neven_squares = [x**2 for x in nums if x % 2 == 0]\nprint(even_squares)\n\nmatrix = [[1, 2], [3, 4]]\nflat = [n for row in matrix for n in row]\nprint(flat)',
                "explain": "Генераторы списков — компактная альтернатива map/filter."
            }
        ],
        "quiz": [
            {"q": "Что делает filter()?", "options": ["Преобразует элементы", "Фильтрует элементы", "Сортирует", "Удаляет"], "correct": 1},
            {"q": "Что такое генератор?", "options": ["Список", "Функция с yield — ленивые значения", "Кортеж", "Словарь"], "correct": 1},
            {"q": "reduce(lambda a,b: a+b, [1,2,3]) вернёт...", "options": [6, "[1,2,3]", 1, 3], "correct": 0},
            {"q": "zip([1,2], ['a','b']) даёт...", "options": ["[[1,'a'],[2,'b']]", "[(1,'a'),(2,'b')]", "{1:'a',2:'b'}", "(1,2,'a','b')"], "correct": 1},
            {"q": "any([False, False]) вернёт...", "options": ["True", "False", "None", "0"], "correct": 1}
        ]
    },
    {
        "id": 11,
        "title": "Мультипоточность",
        "theory": """# Мультипоточность (Threading)

## Зачем?
Параллельное выполнение задач, особенно **I/O-bound** (файлы, сеть, ввод-вывод).

## GIL — Global Interpreter Lock
Python (CPython) выполняет **один поток Python-кода** за раз. GIL не даёт ускорить CPU-задачи потоками — для этого нужен `multiprocessing`.

## threading
```python
import threading

def worker(n):
    print(f"Поток {n}")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()   # дождаться завершения
```

## Синхронизация
- `Lock` — взаимное исключение
- `Queue` — потокобезопасная очередь
- `Event` — сигнал между потоками

```python
lock = threading.Lock()
with lock:
    # критическая секция
    pass
```

## concurrent.futures (высокоуровнево)
```python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(fetch, urls))
```""",
        "examples": [
            {
                "code": 'import threading\nimport time\n\ndef task(name):\n    print(f"Старт {name}")\n    time.sleep(1)\n    print(f"Конец {name}")\n\nt1 = threading.Thread(target=task, args=("A",))\nt2 = threading.Thread(target=task, args=("B",))\nt1.start(); t2.start()\nt1.join(); t2.join()\nprint("Готово")',
                "explain": "Два потока работают одновременно (sleep 1с каждый, суммарно ~1с)."
            },
            {
                "code": 'import threading\n\ncounter = 0\nlock = threading.Lock()\n\ndef inc():\n    global counter\n    for _ in range(100000):\n        with lock:\n            counter += 1\n\nt = [threading.Thread(target=inc) for _ in range(4)]\nfor x in t: x.start()\nfor x in t: x.join()\nprint(counter)  # 400000',
                "explain": "Lock защищает критическую секцию от гонок данных."
            },
            {
                "code": 'from concurrent.futures import ThreadPoolExecutor\nimport time\n\ndef fetch(i):\n    time.sleep(1)\n    return i * i\n\nwith ThreadPoolExecutor(max_workers=5) as pool:\n    results = list(pool.map(fetch, range(5)))\nprint(results)',
                "explain": "ThreadPoolExecutor — удобный пул потоков, map возвращает результаты."
            },
            {
                "code": 'from queue import Queue\nfrom threading import Thread\n\nq = Queue()\n\ndef producer():\n    for i in range(5):\n        q.put(i)\n    q.put(None)\n\ndef consumer():\n    while True:\n        item = q.get()\n        if item is None:\n            break\n        print("Получено:", item)\n\nThread(target=producer).start()\nThread(target=consumer).start()',
                "explain": "Очередь Queue — потокобезопасный обмен данными."
            }
        ],
        "quiz": [
            {"q": "Что такое GIL?", "options": ["Библиотека", "Глобальная блокировка интерпретатора", "Тип потока", "Функция"], "correct": 1},
            {"q": "Потоки лучше подходят для...", "options": ["CPU-задач", "I/O-задач", "Математики", "Рендеринга"], "correct": 1},
            {"q": "Что делает join()?", "options": ["Запускает поток", "Ждёт завершения потока", "Удаляет поток", "Паузит поток"], "correct": 1},
            {"q": "Для чего Lock?", "options": ["Ускорение", "Защита критической секции", "Создание потоков", "Логирование"], "correct": 1},
            {"q": "Какой класс из concurrent.futures создаёт пул потоков?", "options": ["ThreadExecutor", "ThreadPoolExecutor", "Pool", "ExecutorPool"], "correct": 1}
        ]
    },
    {
        "id": 12,
        "title": "Многопроцессность",
        "theory": """# Многопроцессность (Multiprocessing)

## Зачем?
Обход GIL: каждый процесс = **свой интерпретатор** и свой GIL. Подходит для **CPU-bound** задач (вычисления, обработка данных).

## multiprocessing
```python
from multiprocessing import Process

def worker(n):
    print(f"Процесс {n}")

ps = [Process(target=worker, args=(i,)) for i in range(3)]
for p in ps:
    p.start()
for p in ps:
    p.join()
```

## Пул процессов
```python
from multiprocessing import Pool

with Pool(4) as pool:
    results = pool.map(cube, numbers)
```

## Передача данных
- `Queue` — очередь между процессами
- `Value` / `Array` — разделяемая память
- `Pipe` — двусторонний канал

## Важно
Код процессов должен работать в Windows под `if __name__ == "__main__":`

## Сравнение
| | threading | multiprocessing |
|---|---|---|
| GIL | блокирует | обойдён |
| Память | общая | отдельная |
| CPU-bound | медленно | быстро |
| I/O-bound | хорошо | хорошо |""",
        "examples": [
            {
                "code": 'from multiprocessing import Process, current_process\nimport time\n\ndef work(n):\n    print(f"Процесс {n}: {current_process().name}")\n    time.sleep(1)\n\nif __name__ == "__main__":\n    ps = [Process(target=work, args=(i,)) for i in range(3)]\n    for p in ps: p.start()\n    for p in ps: p.join()',
                "explain": "Каждый worker выполняется в отдельном процессе."
            },
            {
                "code": 'from multiprocessing import Pool\nimport math\n\ndef is_prime(n):\n    if n < 2: return False\n    for i in range(2, int(math.sqrt(n)) + 1):\n        if n % i == 0:\n            return False\n    return True\n\nif __name__ == "__main__":\n    with Pool(4) as pool:\n        res = pool.map(is_prime, range(100))\n    print(sum(res), "простых чисел до 100")',
                "explain": "Pool.map распределяет задачи по ядрам CPU."
            },
            {
                "code": 'from multiprocessing import Process, Queue\n\ndef producer(q):\n    for i in range(5):\n        q.put(i * i)\n\nif __name__ == "__main__":\n    q = Queue()\n    p = Process(target=producer, args=(q,))\n    p.start()\n    results = [q.get() for _ in range(5)]\n    p.join()\n    print(results)',
                "explain": "Queue передаёт данные между процессами."
            }
        ],
        "quiz": [
            {"q": "Главное преимущество multiprocessing?", "options": ["Проще писать", "Обходит GIL", "Меньше памяти", "Быстрее стартует"], "correct": 1},
            {"q": "Для каких задач лучше multiprocessing?", "options": ["I/O-bound", "CPU-bound", "GUI", "Логирования"], "correct": 1},
            {"q": "Зачем нужен if __name__ == '__main__' в Windows?", "options": ["Для красоты", "Чтобы не порождать бесконечные процессы", "Для скорости", "Не нужен"], "correct": 1},
            {"q": "Что делает Pool(4)?", "options": ["4 потока", "4 процесса в пуле", "4 файла", "4 очереди"], "correct": 1},
            {"q": "Процессы делят...", "options": ["Всю память", "Ничего (изоляция)", "GIL", "Стек"], "correct": 1}
        ]
    },
    {
        "id": 13,
        "title": "Стандартные и сторонние библиотеки Python",
        "theory": """# Стандартные и сторонние библиотеки

## Стандартная библиотека (идёт с Python)
| Модуль | Назначение |
|--------|-----------|
| os, sys | ОС и параметры интерпретатора |
| math, cmath | математика |
| random | случайные числа |
| datetime, time | дата/время |
| json, csv, xml | данные |
| re | регулярные выражения |
| pathlib | объектная работа с путями |
| collections | deque, defaultdict, Counter |
| itertools | комбинаторика итераторов |
| functools | reduce, lru_cache, partial |
| logging | логирование |
| unittest / pytest | тесты |
| threading / multiprocessing | параллелизм |
| sqlite3 | встроенная БД |

## pathlib (современный способ путей)
```python
from pathlib import Path
p = Path("data") / "file.txt"
p.write_text("hi")
```

## collections
```python
from collections import Counter, defaultdict, deque
Counter("abracadabra")       # подсчёт
defaultdict(list)            # dict со значением по умолчанию
deque([1,2,3])               # двусторонняя очередь
```

## Сторонние библиотеки (pip)
- `requests` — HTTP
- `numpy`, `pandas` — данные
- `flask`, `django` — веб
- `pytest` — тесты
- `pydantic` — валидация
- `pillow` — изображения""",
        "examples": [
            {
                "code": 'from pathlib import Path\n\np = Path("demo.txt")\np.write_text("Привет из pathlib!", encoding="utf-8")\nprint(p.exists(), p.read_text(encoding="utf-8"))\nprint(p.suffix, p.stem)',
                "explain": "pathlib.Path — объектные пути: запись, чтение, свойства."
            },
            {
                "code": 'from collections import Counter, defaultdict, deque\n\nprint(Counter("banana"))\n\nd = defaultdict(list)\nd["fruits"].append("apple")\nd["veg"].append("carrot")\nprint(dict(d))\n\nq = deque([1, 2, 3])\nq.appendleft(0)\nprint(q)',
                "explain": "Counter — подсчёт, defaultdict — dict с дефолтом, deque — очередь с двух сторон."
            },
            {
                "code": 'from itertools import combinations, chain, islice\n\nprint(list(combinations([1, 2, 3], 2)))\nprint(list(chain([1], [2, 3])))\nprint(list(islice((x for x in range(100)), 5)))',
                "explain": "itertools: комбинации, соединение, взятие среза из генератора."
            },
            {
                "code": 'from functools import lru_cache\nimport time\n\n@lru_cache(maxsize=None)\ndef fib(n):\n    if n < 2: return n\n    return fib(n-1) + fib(n-2)\n\nt = time.time()\nprint(fib(50), f"{time.time()-t:.3f}с")',
                "explain": "lru_cache мемоизирует результаты — fib считается мгновенно."
            },
            {
                "code": 'import logging\n\nlogging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")\nlogging.info("Запуск")\nlogging.warning("Мало места")\nlogging.error("Ошибка подключения")',
                "explain": "logging — уровни INFO/WARNING/ERROR вместо print для отладки."
            }
        ],
        "quiz": [
            {"q": "Какой модуль — современная замена os.path?", "options": ["files", "pathlib", "paths", "dirpath"], "correct": 1},
            {"q": "Counter из collections нужен для...", "options": ["Сортировки", "Подсчёта частот", "Сжатия", "Шифрования"], "correct": 1},
            {"q": "Что делает lru_cache?", "options": ["Логирует", "Кеширует результаты функции", "Чистит память", "Ускоряет import"], "correct": 1},
            {"q": "Какой уровень логирования самый серьёзный?", "options": ["DEBUG", "INFO", "WARNING", "ERROR/CRITICAL"], "correct": 3},
            {"q": "Чем deque отличается от list?", "options": ["Ничем", "Быстрый append/appendleft с двух сторон", "Только строки", "Неизменяемый"], "correct": 1}
        ]
    },
    {
        "id": 14,
        "title": "Поддержка цикла разработки",
        "theory": """# Инструменты цикла разработки

## Жизненный цикл
1. Написал код
2. Написал тесты
3. Запустил тесты
4. Залогировал / отладил
5. Закоммитил в Git
6. Отправил на сервер (CI/CD)

## Тестирование — pytest
```python
# test_calc.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```
```bash
pytest -v
```

### Разметка
```python
import pytest

@pytest.mark.parametrize("a,b,expected", [(1,2,3), (0,0,0)])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.skip(reason="не работает")
def test_skip(): ...
```

## Логирование уровней
DEBUG → INFO → WARNING → ERROR → CRITICAL

## Виртуальное окружение
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
source .venv/bin/activate
pip install -r requirements.txt
```

## Статический анализ
- `flake8` / `ruff` — стиль
- `mypy` — типизация
- `black` — автоформатирование

## CI/CD (GitHub Actions)
Тесты и линт запускаются автоматически на каждый push.""",
        "examples": [
            {
                "code": 'def divide(a, b):\n    if b == 0:\n        raise ValueError("Деление на ноль")\n    return a / b\n\n# tests\ndef test_divide():\n    assert divide(10, 2) == 5\n\ndef test_divide_zero():\n    try:\n        divide(1, 0)\n        assert False\n    except ValueError:\n        assert True',
                "explain": "Юнит-тесты проверяют корректность и обработку ошибок."
            },
            {
                "code": 'import pytest\n\ndef is_even(n):\n    return n % 2 == 0\n\n@pytest.mark.parametrize("n,expected", [(2, True), (3, False), (0, True), (-4, True)])\ndef test_is_even(n, expected):\n    assert is_even(n) == expected',
                "explain": "parametrize прогоняет одну функцию теста по многим данным."
            },
            {
                "code": 'import logging\n\nlogging.basicConfig(\n    filename="app.log",\n    level=logging.DEBUG,\n    format="%(asctime)s %(levelname)s %(message)s",\n)\n\nlogging.debug("Отладка")\nlogging.info("Работает")\nlogging.error("Сбой!")',
                "explain": "Логирование в файл с меткой времени — стандарт индустрии."
            },
            {
                "code": 'from dataclasses import dataclass\nfrom typing import Optional\n\n@dataclass\nclass Config:\n    host: str = "localhost"\n    port: int = 8080\n    debug: Optional[bool] = None\n\nc = Config(host="0.0.0.0")\nprint(c)',
                "explain": "dataclass — быстро создавать структуры данных с типами (годится для mypy)."
            }
        ],
        "quiz": [
            {"q": "Что делает pytest?", "options": ["Собирает проект", "Запускает тесты", "Логирует", "Форматирует код"], "correct": 1},
            {"q": "Зачем venv (виртуальное окружение)?", "options": ["Ускоряет Python", "Изолирует зависимости проекта", "Компилирует код", "Шифрует"], "correct": 1},
            {"q": "Самый строгий уровень логирования?", "options": ["DEBUG", "INFO", "WARNING", "CRITICAL"], "correct": 3},
            {"q": "Что проверяет mypy?", "options": ["Стиль", "Типы", "Производительность", "Безопасность"], "correct": 1},
            {"q": "assert в тесте — это...", "options": ["Переменная", "Проверка условия", "Цикл", "Класс"], "correct": 1}
        ]
    },
    {
        "id": "15_1",
        "title": "Основы асинхронного программирования",
        "theory": """# Основы асинхронного программирования

## Синхрон vs Асинхрон
- **Синхрон** — ждём каждую операцию по очереди
- **Асинхрон** (async/await) — при ожидании I/O отдаём управление другим корутинам

## async / await
```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)   # неблокирующее ожидание
    return "данные"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

## Запуск нескольких задач параллельно
```python
async def main():
    results = await asyncio.gather(
        task1(), task2(), task3()
    )
```
Время ≈ времени самого медленного, а НЕ суммы.

## create_task
```python
task = asyncio.create_task(worker())
await asyncio.sleep(0.5)
task.cancel()
```

## Когда использовать
- Сеть (запросы, сокеты, WebSocket)
- Параллельная обработка множества задач
- Боты, чат-серверы

## Event loop
`asyncio.run()` создаёт и крутит цикл событий до завершения главной корутины.""",
        "examples": [
            {
                "code": 'import asyncio\n\nasync def say(who, delay):\n    await asyncio.sleep(delay)\n    print(who)\n\nasync def main():\n    await asyncio.gather(\n        say("Первый", 1),\n        say("Второй", 0.5),\n        say("Третий", 0.7),\n    )\n\nasyncio.run(main())',
                "explain": "gather запускает задачи одновременно — итог ~1с, а не 2.2с."
            },
            {
                "code": 'import asyncio\n\nasync def counter(n):\n    for i in range(n):\n        print(i)\n        await asyncio.sleep(0.3)\n\nasync def main():\n    task = asyncio.create_task(counter(5))\n    await asyncio.sleep(1)\n    task.cancel()\n    try:\n        await task\n    except asyncio.CancelledError:\n        print("Отменено")\n\nasyncio.run(main())',
                "explain": "create_task запускает фоновую задачу, cancel() отменяет её."
            },
            {
                "code": 'import asyncio\n\nasync def fetch(i):\n    await asyncio.sleep(0.5)\n    return f"Результат {i}"\n\nasync def main():\n    tasks = [asyncio.create_task(fetch(i)) for i in range(5)]\n    done = await asyncio.gather(*tasks)\n    print(done)\n\nasyncio.run(main())',
                "explain": "Пул задач: 5 запросов за ~0.5с вместо 2.5с."
            },
            {
                "code": 'import asyncio\n\nasync def worker(sem):\n    async with sem:\n        print("Старт")\n        await asyncio.sleep(1)\n        print("Конец")\n\nasync def main():\n    sem = asyncio.Semaphore(2)   # не более 2 одновременно\n    await asyncio.gather(*[worker(sem) for _ in range(6)])\n\nasyncio.run(main())',
                "explain": "Semaphore ограничивает число одновременных задач."
            }
        ],
        "quiz": [
            {"q": "Что делает await?", "options": ["Блокирует весь поток", "Ждёт завершения корутины, отдавая управление", "Завершает программу", "Создаёт поток"], "correct": 1},
            {"q": "asyncio.gather(...) выполняет задачи...", "options": ["По очереди", "Параллельно (в event loop)", "В отдельных процессах", "В случайном порядке"], "correct": 1},
            {"q": "Кто создаёт event loop в простейшем случае?", "options": ["threading", "asyncio.run()", "main()", "GIL"], "correct": 1},
            {"q": "Что такое корутина?", "options": ["Обычная функция", "Прерываемая async-функция", "Класс", "Модуль"], "correct": 1},
            {"q": "Семафор нужен для...", "options": ["Логов", "Ограничения числа одновременных задач", "Сортировки", "Шифрования"], "correct": 1}
        ]
    },
    {
        "id": "15_2",
        "title": "Асинхронное программирование на базе aiogram",
        "theory": """# Асинхронный Telegram-бот на aiogram

## aiogram 3.x
Асинхронный фреймворк для Telegram Bot API, построенный на asyncio.

## Установка
```bash
pip install aiogram
```

## Структура бота
```python
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command

BOT_TOKEN = "TOKEN"

async def cmd_start(message):
    await message.answer("Привет!")

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.message.register(cmd_start, CommandStart())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
```

## Роутеры (Router)
Делят обработку по модулям — аналог Blueprint.

## Работа с DB внутри хендлера
```python
async def get_user(user_id):
    async with aiosqlite.connect("db.sqlite") as db:
        ...
```
Любая I/O-операция — асинхронная, бот не «зависает».

## Ключевые принципы aiogram
- Все хендлеры — `async def`
- Ответы — `await message.answer(...)`
- Фильтры — `F.text`, `F.photo`, команды""",
        "examples": [
            {
                "code": 'import asyncio\nfrom aiogram import Bot, Dispatcher\nfrom aiogram.filters import CommandStart\nfrom aiogram.types import Message\n\nBOT_TOKEN = "YOUR_TOKEN"\n\nasync def cmd_start(message: Message):\n    await message.answer(f"Привет, {message.from_user.full_name}!")\n\nasync def main():\n    bot = Bot(BOT_TOKEN)\n    dp = Dispatcher()\n    dp.message.register(cmd_start, CommandStart())\n    await dp.start_polling(bot)\n\nif __name__ == "__main__":\n    asyncio.run(main())',
                "explain": "Минимальный бот: /start отвечает приветствием."
            },
            {
                "code": 'from aiogram import F\nfrom aiogram.types import Message\n\nasync def echo_text(message: Message):\n    await message.answer(f"Вы написали: {message.text}")\n\nasync def only_photos(message: Message, bot):\n    await message.answer_photo(\n        message.photo[-1].file_id,\n        caption="Красивое фото!"\n    )\n\n# регистрация:\n# dp.message.register(echo_text, F.text)\n# dp.message.register(only_photos, F.photo)',
                "explain": "Фильтры F.text / F.photo пропускают только нужные типы сообщений."
            },
            {
                "code": 'import asyncio\nfrom aiogram import Bot\nfrom aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery\nfrom aiogram.utils.keyboard import InlineKeyboardBuilder\n\nasync def send_with_buttons(bot, chat_id):\n    kb = InlineKeyboardBuilder()\n    kb.button(text="✅ Да", callback_data="yes")\n    kb.button(text="❌ Нет", callback_data="no")\n    await bot.send_message(chat_id, "Вопрос?", reply_markup=kb.as_markup())\n\nasync def on_callback(query: CallbackQuery):\n    await query.answer()\n    await query.message.edit_text(f"Ответ: {query.data}")',
                "explain": "Инлайн-кнопки и callback-обработчики."
            },
            {
                "code": 'import asyncio\n\nasync def periodic_task(bot, chat_id):\n    while True:\n        await bot.send_message(chat_id, "Напоминание!")\n        await asyncio.sleep(3600)   # раз в час\n\n# запуск фоном:\n# asyncio.create_task(periodic_task(bot, CHAT_ID))',
                "explain": "Фоновая asyncio-задача для рассылок/напоминаний."
            }
        ],
        "quiz": [
            {"q": "aiogram построен на...", "options": ["Flask", "asyncio", "Django", " threading"], "correct": 1},
            {"q": "Хендлеры в aiogram должны быть...", "options": ["def", "async def", "class", "lambda"], "correct": 1},
            {"q": "Что делает dp.start_polling(bot)?", "options": ["Отправляет сообщения", "Запускает приём обновлений", "Удаляет бота", "Тестирует API"], "correct": 1},
            {"q": "F.text в aiogram — это...", "options": ["Переменная", "Фильтр по типу сообщения", "Функция", "Ошибка"], "correct": 1},
            {"q": "Как дождаться ответа API без блокировки?", "options": ["time.sleep()", "await ...", "while True", "thread.join()"], "correct": 1}
        ]
    },
    {
        "id": 16,
        "title": "Библиотека для работы с базами данных",
        "theory": """# Работа с базами данных

## Варианты
- `sqlite3` — встроенная файловая БД
- `SQLAlchemy` (синхронный ORM)
- `aiosqlite` / `asyncpg` — асинхронные драйверы

## sqlite3
```python
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)')
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Анна", 25))
conn.commit()
rows = cur.execute("SELECT * FROM users").fetchall()
conn.close()
```

## SQLAlchemy ORM
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)

with Session(engine) as s:
    s.add(User(name="Иван"))
    s.commit()
```

## Параметризованные запросы
ВСЕГДА `?` / `:name` — защита от SQL-инъекций.""",
        "examples": [
            {
                "code": 'import sqlite3\n\nconn = sqlite3.connect(":memory:")\ncur = conn.cursor()\ncur.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT)")\nfor name in ["Анна", "Борис", "Вера"]:\n    cur.execute("INSERT INTO t (name) VALUES (?)", (name,))\nconn.commit()\nprint(cur.execute("SELECT * FROM t").fetchall())\nconn.close()',
                "explain": "Базовый CRUD на sqlite3, ? — плейсхолдер значения."
            },
            {
                "code": 'import sqlite3\n\nconn = sqlite3.connect(":memory:")\ncur = conn.cursor()\ncur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INT)")\ndata = [("Анна", 25), ("Борис", 30)]\ncur.executemany("INSERT INTO users (name, age) VALUES (?, ?)", data)\nconn.commit()\n\nfor row in cur.execute("SELECT name, age FROM users WHERE age > ?", (26,)):\n    print(row)\nconn.close()',
                "explain": "executemany — пакетная вставка; WHERE с параметром."
            },
            {
                "code": 'from sqlalchemy import create_engine, Column, Integer, String, select\nfrom sqlalchemy.orm import declarative_base, Session\n\nBase = declarative_base()\n\nclass Product(Base):\n    __tablename__ = "products"\n    id = Column(Integer, primary_key=True)\n    name = Column(String, nullable=False)\n    price = Column(Integer)\n\nengine = create_engine("sqlite:///:memory:")\nBase.metadata.create_all(engine)\n\nwith Session(engine) as s:\n    s.add_all([Product(name="Мышка", price=500), Product(name="Клавиатура", price=1500)])\n    s.commit()\n    cheap = s.scalars(select(Product).where(Product.price < 1000)).all()\n    for p in cheap:\n        print(p.name, p.price)',
                "explain": "SQLAlchemy ORM: модели, сессии, запросы без сырого SQL."
            },
            {
                "code": 'import sqlite3\n\ndef get_user(cur, user_id):\n    # НЕПРАВИЛЬНО (инъекция!):\n    # cur.execute(f"SELECT * FROM users WHERE id = {user_id}")\n\n    # ПРАВИЛЬНО:\n    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))\n    return cur.fetchone()',
                "explain": "Всегда параметризованные запросы — защита от SQL-инъекций."
            }
        ],
        "quiz": [
            {"q": "Какой способ защищает от SQL-инъекций?", "options": ["f-строки в SQL", "Параметризованные запросы", "Конкатенация", "eval()"], "correct": 1},
            {"q": "Что делает conn.commit()?", "options": ["Удаляет данные", "Сохраняет транзакцию", "Откатывает", "Закрывает БД"], "correct": 1},
            {"q": "ORM — это...", "options": ["Язык запросов", "Маппинг объектов на таблицы", "СУБД", "Протокол"], "correct": 1},
            {"q": "Для чего CREATE TABLE?", "options": ["Удалить таблицу", "Создать таблицу", "Очистить", "Скопировать"], "correct": 1},
            {"q": "Сервер нужен для sqlite?", "options": ["Да", "Нет — файловая БД", "Только в Linux", "Только с SQLAlchemy"], "correct": 1}
        ]
    },
    {
        "id": 17,
        "title": "Нейронные сети и машинное зрение",
        "theory": """# Нейронные сети и машинное зрение

## Основы нейросетей
Нейросеть — модель, состоящая из слоёв нейронов, обучаемая на данных.

**Нейрон** = взвешенные входы → сумма → функция активации → выход.

## Типы задач
- **Классификация** — к какому классу относится объект
- **Регрессия** — предсказание числа
- **Детекция** — найти и определить объекты на картинке
- **Сегментация** — выделить пиксели объектов

## Ключевые понятия
- **Epoch** — один полный проход по обучающим данным
- **Batch** — подвыборка за один шаг
- **Loss** — ошибка, которую минимизируем
- **Optimizer** (SGD, Adam) — обновляет веса

## Стек
| Библиотека | Роль |
|-----------|------|
| NumPy | матрицы |
| TensorFlow / PyTorch | фреймворки DL |
| Keras | высокоуровневый API |
| OpenCV | компьютерное зрение |
| scikit-learn | классическое ML |

## CNN (свёрточная нейросеть)
Для изображений: свёрточные слои → пуллинг → полносвязные → softmax.

## Transfer Learning
Берём предобученную сеть (ResNet, YOLO) и дообучаем на своих данных.""",
        "examples": [
            {
                "code": 'import numpy as np\n\nx = np.array([[1.0, 2.0], [3.0, 4.0]])\nw = np.array([[0.5], [-0.5]])\nb = np.array([[0.1]])\n\nz = x @ w + b          # линейное преобразование\nout = 1 / (1 + np.exp(-z))  # sigmoid\nprint(out)',
                "explain": "Минимальный «нейрон»: w·x + b → активация."
            },
            {
                "code": 'from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.metrics import accuracy_score\n\ndata = load_iris()\nX_train, X_test, y_train, y_test = train_test_split(\n    data.data, data.target, test_size=0.2, random_state=42\n)\nclf = KNeighborsClassifier(n_neighbors=3)\nclf.fit(X_train, y_train)\npred = clf.predict(X_test)\nprint("Accuracy:", accuracy_score(y_test, pred))',
                "explain": "Классическое ML: split → fit → predict → оценка."
            },
            {
                "code": '# Keras: простейшая сеть для MNIST (фрагмент)\n"""from tensorflow import keras\nfrom tensorflow.keras import layers\n\nmodel = keras.Sequential([\n    layers.Flatten(input_shape=(28, 28)),\n    layers.Dense(128, activation="relu"),\n    layers.Dropout(0.2),\n    layers.Dense(10, activation="softmax"),\n])\nmodel.compile(optimizer="adam",\n              loss="sparse_categorical_crossentropy",\n              metrics=["accuracy"])\nmodel.fit(x_train, y_train, epochs=5)\n"""',
                "explain": "Структура Keras-модели: вход → скрытый слой → выход на 10 классов."
            },
            {
                "code": '# OpenCV: загрузка и обработка изображения\n"""import cv2\n\nimg = cv2.imread("photo.jpg")\ngray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\nedges = cv2.Canny(gray, 100, 200)\ncv2.imshow("edges", edges)\ncv2.waitKey(0)\ncv2.destroyAllWindows()\n"""',
                "explain": "OpenCV: чтение, перевод в оттенки серого, детекция границ Canny."
            }
        ],
        "quiz": [
            {"q": "Что такое epoch в обучении?", "options": ["Один нейрон", "Один полный проход по данным", "Один слой", "Ошибочное предсказание"], "correct": 1},
            {"q": "Для каких задач лучше CNN?", "options": ["Текст", "Изображения", "Звук", "Базы данных"], "correct": 1},
            {"q": "Что делает softmax?", "options": ["Удаляет слой", "Преобразует выходы в вероятности классов", "Обучает сеть", "Читает файл"], "correct": 1},
            {"q": "Loss — это...", "options": ["Прибыль", "Функция ошибки модели", "Тип данных", "Оптимизатор"], "correct": 1},
            {"q": "Transfer Learning — это...", "options": ["Перенос файлов", "Использование предобученной сети", "Копирование данных", "Экспорт модели"], "correct": 1}
        ]
    },
    {
        "id": 18,
        "title": "Библиотеки для работы с сетью",
        "theory": """# Библиотеки для работы с сетью

## requests — HTTP-клиент
```python
import requests

r = requests.get("https://api.github.com/users/python")
print(r.status_code, r.json())

requests.post(url, json={"a": 1}, headers={...}, timeout=10)
```

## Обработка ошибок
```python
try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()
except requests.RequestException as e:
    print(e)
```

## aiohttp — асинхронные запросы
```python
import aiohttp, asyncio

async def get(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            return await r.json()
```

## Веб-сокеты
```python
import websocket  # pip install websocket-client
```

## Полезное
- `httpx` — requests + async
- `urllib` — стандартная библиотека
- `socket` — низкоуровневые сокеты

## REST API
| Метод | Действие |
|-------|----------|
| GET | получить |
| POST | создать |
| PUT/PATCH | обновить |
| DELETE | удалить |""",
        "examples": [
            {
                "code": 'import requests\n\nr = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)\nprint(r.status_code)\ndata = r.json()\nprint(data["title"][:50])',
                "explain": "GET-запрос: status_code и разбор JSON."
            },
            {
                "code": 'import requests\n\npayload = {"title": "foo", "body": "bar", "userId": 1}\nr = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)\nprint(r.status_code, r.json()["id"])',
                "explain": "POST с телом json= — requests сам сериализует и ставит Content-Type."
            },
            {
                "code": 'import requests\n\ntry:\n    r = requests.get("https://httpbin.org/status/500", timeout=5)\n    r.raise_for_status()\nexcept requests.exceptions.HTTPError as e:\n    print("HTTP ошибка:", e)\nexcept requests.exceptions.Timeout:\n    print("Таймаут")\nexcept requests.exceptions.RequestException as e:\n    print("Ошибка запроса:", e)',
                "explain": "Корректная обработка сетевых исключений."
            },
            {
                "code": 'import asyncio\nimport aiohttp\n\nasync def fetch(session, url):\n    async with session.get(url) as r:\n        return r.status\n\nasync def main():\n    urls = ["https://example.com"] * 5\n    async with aiohttp.ClientSession() as session:\n        results = await asyncio.gather(*[fetch(session, u) for u in urls])\n    print(results)\n\nasyncio.run(main())',
                "explain": "aiohttp — параллельные асинхронные HTTP-запросы."
            }
        ],
        "quiz": [
            {"q": "Что вернёт r.status_code при успехе?", "options": ["200/201...", "404", "500", "None"], "correct": 0},
            {"q": "Что делает raise_for_status()?", "options": ["Повышает уровень лога", "Выбрасывает исключение при 4xx/5xx", "Перезапрашивает", "Закрывает сессию"], "correct": 1},
            {"q": "Асинхронный HTTP-клиент?", "options": ["requests", "aiohttp", "sqlite3", "json"], "correct": 1},
            {"q": "Метод POST в REST используется для...", "options": ["Получения", "Создания ресурса", "Удаления", "Проверки"], "correct": 1},
            {"q": "timeout в requests нужен чтобы...", "options": ["Ускорить запрос", "Ограничить время ожидания", "Сжать данные", "Шифровать"], "correct": 1}
        ]
    },
    {
        "id": 19,
        "title": "Библиотека для работы с документами и автоматизацией",
        "theory": """# Работа с документами и автоматизация

## python-docx — Word
```python
from docx import Document
doc = Document()
doc.add_heading("Отчёт", 0)
doc.add_paragraph("Текст абзаца")
doc.add_table(rows=2, cols=2)
doc.save("report.docx")
```

## openpyxl — Excel
```python
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws["A1"] = "Имя"
ws.append(["Анна", 25])
wb.save("data.xlsx")
```

## PyPDF2 / pypdf — PDF
```python
from pypdf import PdfReader
reader = PdfReader("doc.pdf")
print(len(reader.pages))
text = reader.pages[0].extract_text()
```

## Автоматизация ОС
```python
import shutil, os, glob

shutil.copy("a.txt", "backup/")
for f in glob.glob("*.log"):
    os.remove(f)
```

## Other
- `Pillow` — изображения
- `python-pptx` — PowerPoint
- `schedule` — планировщик задач""",
        "examples": [
            {
                "code": 'from docx import Document\n\ndoc = Document()\ndoc.add_heading("Учебный отчёт", level=1)\ndoc.add_paragraph("Модуль 19: работа с документами.")\ntable = doc.add_table(rows=1, cols=2)\ntable.rows[0].cells[0].text = "Модуль"\ntable.rows[0].cells[1].text = "Статус"\ndoc.save("report.docx")\nprint("Сохранено")',
                "explain": "Создание Word-документа: заголовок, абзац, таблица."
            },
            {
                "code": 'from openpyxl import Workbook\nfrom openpyxl.styles import Font\n\nwb = Workbook()\nws = wb.active\nws.title = "Оценки"\nws["A1"] = "Ученик"\nws["B1"] = "Балл"\nws["A1"].font = Font(bold=True)\nws.append(["Анна", 5])\nws.append(["Борис", 4])\nwb.save("grades.xlsx")',
                "explain": "Excel: заголовки, стиль, добавление строк."
            },
            {
                "code": 'from pypdf import PdfReader\n\nreader = PdfReader("document.pdf")\nprint("Страниц:", len(reader.pages))\nfor page in reader.pages:\n    print(page.extract_text())',
                "explain": "Чтение текста из PDF постранично."
            },
            {
                "code": 'import glob, os, shutil\nfrom datetime import datetime\n\nos.makedirs("backup", exist_ok=True)\nfor f in glob.glob("*.py"):\n    shutil.copy(f, "backup/")\nprint("Бэкап:", datetime.now())\n\nfor f in glob.glob("tmp_*.txt"):\n    os.remove(f)',
                "explain": "Автоматизация: копирование файлов и очистка временных."
            }
        ],
        "quiz": [
            {"q": "Какой библиотекой читать Excel?", "options": ["python-docx", "openpyxl", "pypdf", "Pillow"], "correct": 1},
            {"q": "docx — это формат...", "options": ["Excel", "Word", "PDF", "PowerPoint"], "correct": 1},
            {"q": "Что делает shutil.copy()?", "options": ["Удаляет", "Копирует файл", "Переименовывает", "Читает"], "correct": 1},
            {"q": "extract_text() используется для...", "options": ["PDF", "Excel", "Word", "Изображений"], "correct": 0},
            {"q": "glob.glob('*.log') возвращает...", "options": ["Строку", "Список путей", "Число", "Словарь"], "correct": 1}
        ]
    },
    {
        "id": 20,
        "title": "Django. Представления",
        "theory": """# Django: представления (views)

## Что такое Django?
Полноценный веб-фреймворк: ORM, админка, шаблоны, безопасность.

## Проект
```bash
pip install django
django-admin startproject mysite
cd mysite
python manage.py startapp blog
```

## URL → View → Response
```python
# mysite/urls.py
from django.urls import path, include
urlpatterns = [path("", include("blog.urls"))]

# blog/urls.py
from . import views
urlpatterns = [path("", views.index, name="index")]

# blog/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет из Django!")
```

## Типы представлений
1. **FBV** — функции
2. **CBV** — классы (ListView, DetailView, CreateView...)

## HttpResponse vs JsonResponse
```python
from django.http import JsonResponse
def api(request):
    return JsonResponse({"ok": True})
```

## Шаблоны
```html
<!-- blog/templates/blog/index.html -->
<h1>{{ title }}</h1>
{% for post in posts %}
  <p>{{ post.text }}</p>
{% endfor %}
```
```python
from django.shortcuts import render
def index(request):
    return render(request, "blog/index.html", {"title": "Главная"})
```

## Админка
```python
# blog/admin.py
from .models import Post
admin.site.register(Post)
```
`python manage.py createsuperuser` → /admin""",
        "examples": [
            {
                "code": 'from django.http import HttpResponse\n\ndef hello(request):\n    return HttpResponse("<h1>Привет, Django!</h1>")\n\n# blog/urls.py\n# from . import views\n# urlpatterns = [path("hello/", views.hello)]',
                "explain": "Самое простое представление — FBV, возвращает HttpResponse."
            },
            {
                "code": 'from django.http import JsonResponse\n\ndef api_posts(request):\n    data = [\n        {"id": 1, "title": "Пост 1"},\n        {"id": 2, "title": "Пост 2"},\n    ]\n    return JsonResponse({"posts": data}, json_dumps_params={"ensure_ascii": False})',
                "explain": "JSON API endpoint через JsonResponse."
            },
            {
                "code": 'from django.shortcuts import render, get_object_or_404\nfrom .models import Post\n\ndef post_list(request):\n    posts = Post.objects.all()\n    return render(request, "blog/list.html", {"posts": posts})\n\ndef post_detail(request, pk):\n    post = get_object_or_404(Post, pk=pk)\n    return render(request, "blog/detail.html", {"post": post})',
                "explain": "CBV-подход: выборка из ORM + рендер шаблона, get_object_or_404."
            },
            {
                "code": 'from django.views.generic import ListView\nfrom .models import Post\n\nclass PostListView(ListView):\n    model = Post\n    template_name = "blog/list.html"\n    context_object_name = "posts"\n    paginate_by = 10',
                "explain": "CBV ListView — готовая выборка, пагинация, контекст."
            }
        ],
        "quiz": [
            {"q": "Что возвращает обычное view в Django?", "options": ["str", "HttpResponse / JsonResponse", "html-файл", "None"], "correct": 1},
            {"q": "CBV — это...", "options": ["Content View", "Class-Based View", "Cache View", "Code View"], "correct": 1},
            {"q": "Файл urls.py отвечает за...", "options": ["Шаблоны", "Маршрутизацию URL", "Модели", "Стили"], "correct": 1},
            {"q": "get_object_or_404 при отсутствии объекта вернёт...", "options": ["None", "[]", "404 страницу", "500"], "correct": 2},
            {"q": "Для чего render(request, template, context)?", "options": ["Удаляет страницу", "Рендерит HTML-шаблон с данными", "Создаёт БД", "Тестирует"], "correct": 1}
        ]
    },
    {
        "id": 21,
        "title": "Django в Python. Дополнительно",
        "theory": """# Django: дополнительные возможности

## Модели и миграции
```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```
```bash
python manage.py makemigrations
python manage.py migrate
```

## Админка с настройками
```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    search_fields = ("title",)
```

## Формы
```python
from django import forms
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
```

## middleware, auth, static
- `django.contrib.auth` — пользователи
- `static/` — CSS/JS (`{% static 'style.css' %}`)
- `settings.py` — INSTALLED_APPS, DATABASES, SECRET_KEY

## Полезные пакеты
- `django-debug-toolbar`
- `django-filter`
- `DRF` (Django REST Framework)""",
        "examples": [
            {
                "code": 'from django.db import models\n\nclass Category(models.Model):\n    name = models.CharField(max_length=100, unique=True)\n\n    class Meta:\n        verbose_name = "Категория"\n        ordering = ["name"]\n\n    def __str__(self):\n        return self.name\n\nclass Article(models.Model):\n    title = models.CharField(max_length=200)\n    body = models.TextField()\n    category = models.ForeignKey(Category, on_delete=models.CASCADE)\n    views = models.PositiveIntegerField(default=0)\n\n    def __str__(self):\n        return self.title',
                "explain": "Модели: CharField, TextField, ForeignKey с CASCADE."
            },
            {
                "code": 'from django import forms\nfrom .models import Article\n\nclass ArticleForm(forms.ModelForm):\n    class Meta:\n        model = Article\n        fields = ["title", "body", "category"]\n        widgets = {\n            "title": forms.TextInput(attrs={"placeholder": "Заголовок"}),\n            "body": forms.Textarea(attrs={"rows": 6}),\n        }\n\n# view:\n# if request.method == "POST":\n#     form = ArticleForm(request.POST)\n#     if form.is_valid():\n#         form.save()\n# else:\n#     form = ArticleForm()',
                "explain": "ModelForm — быстрое создание формы из модели + валидация."
            },
            {
                "code": 'from django.contrib.auth.decorators import login_required\nfrom django.shortcuts import render\n\n@login_required\ndef dashboard(request):\n    return render(request, "app/dashboard.html", {\n        "user": request.user,\n    })',
                "explain": "@login_required — только для авторизованных."
            },
            {
                "code": 'from rest_framework import serializers, viewsets\nfrom .models import Article\n\nclass ArticleSerializer(serializers.ModelSerializer):\n    class Meta:\n        model = Article\n        fields = ["id", "title", "body", "views"]\n\nclass ArticleViewSet(viewsets.ModelViewSet):\n    queryset = Article.objects.all()\n    serializer_class = ArticleSerializer',
                "explain": "Django REST Framework — готовый CRUD API из модели."
            }
        ],
        "quiz": [
            {"q": "Что создаёт makemigrations?", "options": ["БД", "Файлы миграций", "Админку", "Шаблоны"], "correct": 1},
            {"q": "on_delete=models.CASCADE означает...", "options": ["Запрет удаления", "Удаление дочерних записей", "Копирование", "Архивацию"], "correct": 1},
            {"q": "Что делает @login_required?", "options": ["Создаёт пользователя", "Требует авторизацию", "Выход", "Регистрацию"], "correct": 1},
            {"q": "ModelForm автоматически...", "options": ["Рисует UI", "Генерирует валидацию из модели", "Создаёт БД", "Тестирует"], "correct": 1},
            {"q": "DRF нужен для...", "options": ["HTML-шаблонов", "REST API", "CSS", "Логов"], "correct": 1}
        ]
    },
    {
        "id": 22,
        "title": "Дипломная работа",
        "theory": """# Дипломная работа

## Как выбрать тему
1. Интересна тебе и/или рынку труда
2. Реально реализовать за отведённый срок
3. Есть объяснимая проблема, которую решает проект
4. Достаточно глубина: не «CRUD-шоп», а суть

## Типовые темы
- Telegram-бот с полезным сервисом
- Веб-приложение (Django/Flask) с API
- Система аналитики / дашборд
- CV/ML-проект (детектор, рекомендатель)
- Инструмент автоматизации DevOps

## Структура работы
1. **Введение** — актуальность, цель, задачи
2. **Обзор технологий** — что и зачем выбрано
3. **Анализ предметной области** — сущности, процессы
4. **Проектирование** — архитектура, ER-диаграмма, API
5. **Реализация** — код, ключевые решения
6. **Тестирование** — юнит-тесты, нагрузка
7. **Заключение** — результаты, перспективы
8. **Список литературы**

## Требования к коду
- README: как запустить
- requirements.txt / pyproject.toml
- Тесты (pytest)
- CI (GitHub Actions)
- Без секретов в репозитории!

## Защита
- 5–10 минут демо: проблема → решение → результат
- Подготовь ответы: «почему выбрали стек», «как масштабировать», «слабые места»""",
        "examples": [
            {
                "code": '# Структура дипломного проекта (пример)\n"""diploma/\n├── README.md\n├── requirements.txt\n├── .env.example\n├── app/\n│   ├── __init__.py\n│   ├── main.py\n│   ├── models.py\n│   ├── api/\n│   ├── services/\n│   └── static/\n├── tests/\n│   ├── test_api.py\n│   └── test_services.py\n├── docker-compose.yml\n└── .github/workflows/ci.yml\n"""',
                "explain": "Рекомендуемая структура: разделение слоёв, тесты, CI, Docker."
            },
            {
                "code": '"""Пример README для диплома:\n# Название проекта\n\n## Запуск\n```bash\npython -m venv .venv\nsource .venv/bin/activate\npip install -r requirements.txt\ncp .env.example .env\nuvicorn app.main:app --reload\n```\n\n## Тесты\n```bash\npytest -v\n```\n"""',
                "explain": "README с инструкцией запуска — обязательное требование."
            },
            {
                "code": '# Пример юнит-теста для диплома\nimport pytest\nfrom app.services.calc import calculate_discount\n\n@pytest.mark.parametrize("price,percent,expected", [\n    (1000, 10, 900),\n    (500, 0, 500),\n    (200, 50, 100),\n])\ndef test_calculate_discount(price, percent, expected):\n    assert calculate_discount(price, percent) == expected\n\ndef test_invalid_percent():\n    with pytest.raises(ValueError):\n        calculate_discount(100, 150)',
                "explain": "Покрытие граничных случаев — хорошо для защиты."
            },
            {
                "code": '# .env.example — секреты НЕ в git\n"""FLASK_SECRET_KEY=change-me\nDATABASE_URL=sqlite:///local.db\nTELEGRAM_TOKEN=\nAPI_KEY=\n"""',
                "explain": ".env.example показывает нужные переменные без реальных секретов."
            }
        ],
        "quiz": [
            {"q": "Секреты (токены) в репозитории...", "options": ["Обязательны", "Нельзя хранить в открытом виде", "Нужно в README", "Только в main"], "correct": 1},
            {"q": "Что обязательно в хорошем проекте?", "options": ["Только код", "README + requirements + тесты", "1000 файлов", "Коммерческая лицензия"], "correct": 1},
            {"q": "Структура диплома начинается с...", "options": ["Кода", "Введения", "Тестов", "Библиографии"], "correct": 1},
            {"q": "Демо на защите должно показывать...", "options": ["Весь код", "Проблему → решение → результат", "Только слайды", "Логи сервера"], "correct": 1},
            {"q": ".env.example содержит...", "options": ["Реальные ключи", "Имена переменных-заглушек", "Тесты", "SQL"], "correct": 1}
        ]
    },
    {
        "id": 23,
        "title": "Основы Git и GitHub",
        "theory": """# Основы Git и GitHub

## Git vs GitHub
- **Git** — локальная система контроля версий
- **GitHub** — облачный хостинг репозиториев

## Основной цикл
```bash
git init                      # новый репозиторий
git clone <url>               # клонировать существующий
git status                    # состояние
git add file.py | git add .   # в индекс (staging)
git commit -m "описание"      # зафиксировать
git push origin main          # отправить
git pull                      # забрать
```

## История и откаты
```bash
git log --oneline
git diff                      # что изменено
git reset --hard <commit>     # откат (опасно)
git revert <commit>           # безопасный откат новым коммитом
```

## Ветки
```bash
git branch feature           # создать
git checkout feature         # переключиться
git checkout -b feature      # создать и переключиться
git merge feature            # слить в текущую
git push -u origin feature
```

## .gitignore
```
__pycache__/
*.env
.venv/
*.log
```

## Remote
```bash
git remote add origin <url>
git remote -v
```

## Полезное
- `git stash` — спрятать изменения
- PR (Pull Request) — ревью перед слиянием
- fork — копия чужого репозитория""",
        "examples": [
            {
                "code": 'git init\ngit add .\ngit commit -m "Первый коммит"\ngit branch -M main\ngit remote add origin https://github.com/user/repo.git\ngit push -u origin main',
                "explain": "Полный набор команд для публикации нового проекта."
            },
            {
                "code": 'git checkout -b feature/login\ngit add login.py\ngit commit -m "Добавлена авторизация"\ngit push -u origin feature/login\n# ... на GitHub создать PR, после ревью:\ngit checkout main\ngit pull\ngit merge feature/login',
                "explain": "Работа в ветке: создание, push, PR, merge."
            },
            {
                "code": 'git status\ngit diff\ngit log --oneline -5\ngit stash\ngit stash pop',
                "explain": "Просмотр состояния и временное прятание изменений."
            },
            {
                "code": '# .gitignore\n"""__pycache__/\n*.py[cod]\n.venv/\nvenv/\n.env\n*.log\n.DS_Store\n.idea/\n.vscode/\n"""\n\n# gitignore НЕ работает для уже закоммиченных файлов:\n# git rm -r --cached .env\ngit commit -m "Убрал секреты из индекса"',
                "explain": ".gitignore + git rm --cached — вычистить попавшие секреты."
            }
        ],
        "quiz": [
            {"q": "Что делает git add?", "options": ["Коммитит", "Добавляет изменения в индекс", "Отправляет на GitHub", "Создаёт ветку"], "correct": 1},
            {"q": "Чем Git отличается от GitHub?", "options": ["Ничем", "Git — локально, GitHub — облачный хостинг", "GitHub — локально", "Git работает только с Python"], "correct": 1},
            {"q": "git clone делает...", "options": ["Копию репозитория к себе", "Новый коммит", "Ветку", "Тег"], "correct": 0},
            {"q": "Безопасный откат чужого коммита — это...", "options": ["git reset --hard", "git revert", "git drop", "rm -rf"], "correct": 1},
            {"q": "Что такое pull request?", "options": ["Запрос на удаление", "Предложение слить ветку с ревью", "Скачивание", "Ошибка"], "correct": 1}
        ]
    },
]

# Совместимость: id может быть int или str
for _m in MODULES:
    _m["id"] = str(_m["id"])

# Разделы официальной документации (docs.python.org/3)
DOCS = {
    "0": "https://docs.python.org/3/tutorial/index.html",
    "1": "https://docs.python.org/3/tutorial/datastructures.html",
    "2": "https://docs.python.org/3/reference/compound_stmts.html",
    "3": "https://docs.python.org/3/tutorial/controlflow.html",
    "4": "https://docs.python.org/3/tutorial/modules.html",
    "5": "https://docs.python.org/3/reference/executionmodel.html",
    "6": "https://docs.python.org/3/tutorial/classes.html",
    "7": "https://docs.python.org/3/tutorial/classes.html",
    "8": "https://docs.python.org/3/tutorial/inputoutput.html",
    "10": "https://docs.python.org/3/howto/functional.html",
    "11": "https://docs.python.org/3/library/threading.html",
    "12": "https://docs.python.org/3/library/multiprocessing.html",
    "13": "https://docs.python.org/3/library/index.html",
    "14": "https://docs.python.org/3/library/unittest.html",
    "15_1": "https://docs.python.org/3/library/asyncio.html",
    "15_2": "https://docs.python.org/3/library/asyncio.html",
    "16": "https://docs.python.org/3/library/sqlite3.html",
    "17": "https://docs.python.org/3/tutorial/classes.html",
    "18": "https://docs.python.org/3/library/urllib.html",
    "19": "https://docs.python.org/3/tutorial/stdlib2.html",
    "20": "https://docs.djangoproject.com/en/stable/topics/http/views/",
    "21": "https://docs.djangoproject.com/en/stable/",
    "22": "https://docs.python.org/3/tutorial/index.html",
    "23": "https://git-scm.com/doc",
}

# Описание раздела документации для каждого модуля
DOC_LABELS = {
    "0": "Официальный учебник Python (Tutorial)",
    "1": "Структуры данных — вход в data structures",
    "2": "Составные операторы (if/while/for)",
    "3": "Управляющие конструкции и функции",
    "4": "Модули и пакеты (import system)",
    "5": "Модель исполнения и пространства имён",
    "6": "Классы — официальный туториал",
    "7": "Классы: наследование",
    "8": "Ввод-вывод и форматирование",
    "10": "Функциональное программирование (HOW-TO)",
    "11": "Модуль threading",
    "12": "Модуль multiprocessing",
    "13": "Справочник стандартной библиотеки",
    "14": "Модуль unittest (тестирование)",
    "15_1": "Модуль asyncio (асинхронный код)",
    "15_2": "Модуль asyncio (применение)",
    "16": "Модуль sqlite3 (встроенная БД)",
    "17": "ООП в туториале (основа для ML)",
    "18": "Модуль urllib (работа с сетью)",
    "19": "Тур по стандартной библиотеке, часть II",
    "20": "Django: представления (views)",
    "21": "Документация Django",
    "22": "Учебник Python — рекомендации",
    "23": "Официальная документация Git",
}

for _m in MODULES:
    _id = str(_m["id"])
    _m["doc_url"] = DOCS.get(_id, "https://docs.python.org/3/")
    _m["doc_label"] = DOC_LABELS.get(_id, "Документация Python")
