import allure
from litres_project.pages.ui.book_page import book_page
from litres_project.pages.ui.cart_page import cart_page
from litres_project.data.data import book


@allure.epic('Remove book from cart')
@allure.label("owner", "shakeawwake")
@allure.feature("Checking whether a book has been removed from cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_removing_book_from_cart():
    with allure.step("Open the book page"):
        book_page.open(book)

    with allure.step("Adding the selected book to the cart"):
        book_page.adding_book_to_cart()

    with allure.step("Open the cart page"):
        cart_page.open()

    with allure.step("Removing the selected book from cart"):
        cart_page.removing_book_to_cart()

    with allure.step("Checking that the book has been removed from cart"):
        cart_page.book_must_be_removed_from_cart()


@allure.epic('Remove book from cart')
@allure.label("owner", "shakeawwake")
@allure.feature("Checking whether a book has been removed from cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_removing_book_from_cart_and_adding_to_favorites():
    with allure.step("Open the book page"):
        book_page.open(book)

    with allure.step("Adding the selected book to the cart"):
        book_page.adding_book_to_cart()

    with allure.step("Open the cart page"):
        cart_page.open()

    with allure.step("Removing the selected book from cart and adding book to favorites"):
        cart_page.removing_book_to_cart_and_adding_to_favorites()

    with allure.step("Checking that the book has been removed from cart"):
        cart_page.book_must_be_removed_from_cart()

    with allure.step("Checking that the book has been added to favorites"):
        book_page.book_must_be_added_to_favorites(book)
