from conf import MODEL
import json
import random
from faker import Faker

model = MODEL


def main():
    dict_ = {}
    pk = random.randint(1, 10)
    for i in range(101):

        dict_[i] = \
            {
                "model": MODEL,
                "pk": pk,
                "fields": {
                    "title": title(),
                    "year": year(),
                    "pages": pages(),
                    "isbn13": isbn13(),
                    "rating": rating(),
                    "price": price(),
                    "author": [
                        author(),

                    ]
                }
            }
        pk = pk + 1
        with open('result.txt', 'w', encoding='utf8') as file:
            json.dump(dict_, file, indent=4, ensure_ascii=False)


def pk():
    return int(random.randint(1, 101))


def title():
    file = open('books.txt', 'r', encoding='utf-8')
    list_ = file.readlines()
    line = random.choice(list_).rstrip()
    return line


def year():
    return random.randint(1990, 2020)


def pages():
    return random.randint(100, 1000)


def isbn13():
    fake_ru = Faker('ru_RU')
    return fake_ru.isbn13()


def rating():
    return round(random.uniform(0, 5.01), 2)


def price():
    return round(random.uniform(0, 100), 2)


def author():
    fake_ru = Faker('ru_RU')
    count = random.randint(1, 3)
    list_ = []
    for i in range(count):
        list_.append(fake_ru.name())
    return list_


if __name__ == "__main__":
    main()

