import os
import allure
from litres_project.data.data import User
from litres_project.pages.ui.main_page import main_page


@allure.epic('Authorized')
@allure.label("owner", "shakeawwake")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_authorization_registered_user():
    user = User(
        name='Ксения Глазова',
        email=os.getenv('USER_EMAIL'),
        password=os.getenv('USER_PASSWORD')
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Filling the authorization form"):
        main_page.filling_authorization_form(user)

    with allure.step("Checking that user has been authorized"):
        main_page.user_must_be_authorized(user)


@allure.epic('Authorized')
@allure.label("owner", "shakeawwake")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_authorization_unregistered_user():
    user = User(
        name='test',
        email=os.getenv('UNREGISTERED_USER_EMAIL'),
        password=os.getenv('UNREGISTERED_USER_PASSWORD')
    )

    with allure.step("Open the main page"):
        main_page.open()

    with allure.step("Filling the authorization form"):
        main_page.filling_authorization_form(user)

    with allure.step("Checking that user has not been authorized"):
        main_page.user_must_not_be_authorized()
