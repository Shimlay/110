import json
import random
from faker import Faker
from conf import MODEL_NAME


def pk_gen(start=1):
    """
    Функция создает значение pk и последовательно увеличивает его
    """
    i = start
    while True:
        yield i
        i += 1


def title_gen() -> None:
    """
    Функция случайным образом передает одну строку из файла
    """

    with open('books.txt', 'r') as f:
        lines = f.readlines()

    title = random.choice(lines)

    return title


def year_gen():
    """Функция генерирует год"""
    year = random.randint(1500, 2023)
    return year


def pages_gen():
    """Функция генерирует значение количества страниц"""
    pages = random.randint(10, 1000)
    return pages


def isbn_gen():
    """Функция генерирует isbn"""
    fake = Faker()
    Faker.seed(0)
    isbn13 = fake.isbn13()
    return isbn13


def rating_gen():
    """Функция генерирует значение рейтинга"""
    rating = random.randint(1, 5)
    return rating


def price_gen():
    """Функция генерирует значение цены"""
    price = round(random.uniform(100, 1000), 2)
    return price


def author_gen():
    """Функция генерирует авторов"""
    fake = Faker()
    author_num = random.randint(1, 3)
    authors_list = []
    for i in range(author_num):
        authors_list.append(fake.name())
    return authors_list


def book_gen(start_pk=1) -> dict:
    """Функция генерирует книги по шаблону и позволяет задать стартовое значение pk"""
    pk = pk_gen(start=start_pk)
    while True:
        yield {
            "model": MODEL_NAME,
            "pk": next(pk),
            "fields": {
                "title": title_gen(),
                "year": year_gen(),
                "pages": pages_gen(),
                "isbn13": isbn_gen(),
                "rating": rating_gen(),
                "price": price_gen(),
                "author": author_gen()
            }
        }


def main():
    """Функция генерирует список с книгами с книгами и сериализует """
    books = []
    g = book_gen()
    for i in range(100):
        books.append(next(g))
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
