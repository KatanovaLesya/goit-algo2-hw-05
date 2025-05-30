# Домашнє завдання 5: Алгоритми роботи з великими даними

## Опис

Цей проєкт містить реалізацію двох алгоритмів для роботи з великими даними:

### Завдання 1: Перевірка унікальності паролів за допомогою фільтра Блума

- Створено клас `BloomFilter` для ефективної перевірки наявності паролів.
- Функція `check_password_uniqueness` аналізує нові паролі та визначає, чи були вони вже використані.
- Обробляються порожні, некоректні значення.
- Результати відображаються в зручному форматі.

Файли:
`bloom_filter.py` — клас BloomFilter
`password_checker.py` — функція перевірки паролів
`main.py` — приклад використання

### Завдання 2: Порівняння точного підрахунку та HyperLogLog

- Завантаження IP-адрес з лог-файлу `lms-stage-access.log`
- Точний підрахунок унікальних IP за допомогою `set`
- Наближений підрахунок через `HyperLogLog` (з адаптацією `p`)
- Вивід результатів у вигляді таблиці з часом виконання і похибкою

Файли:
`log_analyzer.py` — логіка обробки лог-файлу (має бути в корені проєкту)
`main_hll.py` — запуск підрахунку та порівняння

## Запуск

1] Встановити залежності:

```bash
pip install bitarray datasketch
```

2] Запуск Bloom Filter:

```bash
pip python3 main.py
```

3] Запуск HyperLogLog:

```bash
pip python3 main_hll.py
```

## Структура проєкту

goit-algo2-hw-05/
├── bloom_filter.py
├── password_checker.py
├── log_analyzer.py
├── main.py
├── main_hll.py
├── README.md
├── .gitignore
└── lms-stage-access.log

## Автор

Катанова Леся
