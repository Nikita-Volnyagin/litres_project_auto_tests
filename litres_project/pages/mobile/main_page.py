from selene import browser, be
from appium.webdriver.common.appiumby import AppiumBy


class AndroidMainPage:

    def selecting_application_language(self):

        if browser.element((AppiumBy.ID, "ru.litres.android:id/choosebutton")).matching(be.clickable):
            browser.element((AppiumBy.ID, "ru.litres.android:id/choosebutton")).click()
        return self

    def hiding_adult_content(self):

        if browser.element((AppiumBy.ID, "ru.litres.android:id/btnDisableAdultContent")).click():
            browser.element((AppiumBy.ID, "ru.litres.android:id/btnConfirmDisableAdultContent")).click()
        return self


main_page = AndroidMainPage()
