import dataclasses


@dataclasses.dataclass
class Book:
    name: str
    author: str
    price: str
    url: str


@dataclasses.dataclass
class User:
    name: str
    email: str
    password: str



book = Book(
        name='Стоя под радугой',
        author='Фэнни Флэгг',
        url='fenni-flegg/stoya-pod-radugoy-8685881/',
        price=''
    )

book2 = Book(
        name='Жареные зеленые помидоры в кафе «Полустанок»',
        author='Фэнни Флэгг',
        url='fenni-flegg/zharenye-zelenye-pomidory-v-kafe-polustanok-130519/',
        price='379 ₽'
    )