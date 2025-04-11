import allure
from gpn_qa_utils.ui.page_factory.button import Button
from gpn_qa_utils.ui.page_factory.component_list import ComponentList
from gpn_qa_utils.ui.page_factory.element import Element
from gpn_qa_utils.ui.pages.base import BasePage
from playwright.async_api import Page

from src.helper.URLs import BASE_URL
from src.tests.constants import TestCheckCountProductsConst


class MainPage(BasePage):
    def __init__(self, page: Page, url=BASE_URL):
        super().__init__(page, url)
        self.title_categories = Element(page, strategy="by_text", value="CATEGORIES",
                                        allure_name="Заголовок CATEGORIES")
        self.button_phones = Button(page, strategy="locator", selector="//a[@id='itemc' and text() = 'Phones']",
                                    allure_name="Кнопка Phones")
        self.button_laptops = Button(page, strategy="locator", selector="//a[@id='itemc' and text() = 'Laptops']",
                                     allure_name="Кнопка Laptops")
        self.button_monitors = Button(page, strategy="locator", selector="//a[@id='itemc' and text() = 'Monitors']",
                                      allure_name="Кнопка Monitors")
        self.product_card_block = ComponentList(page, strategy="locator", selector=".card-block",
                                                allure_name="Счетчик карточек товара")

    def check_title(self, title: str):
        """Проверяет наличие заголовка {title}
        :param title: текст заголовка"""
        with allure.step(f'Проверим наличие заголовка {title}'):
            title_text = self.title_categories.get_text()
            assert title_text == title

    def check_button_is_active(self, button_text):
        """Проверяет что кнопка активна для взаимодействия
        :param button_text: текст кнопки"""
        with allure.step(f'Проверим что кнопка с текстом {button_text} активна для взаимодействия'):
            if button_text == TestCheckCountProductsConst.BUTTON_PHONES_TEXT:
                self.button_phones.check_disabled(False)
            elif button_text == TestCheckCountProductsConst.BUTTON_LAPTOPS_TEXT:
                self.button_laptops.check_disabled(False)
            elif button_text == TestCheckCountProductsConst.BUTTON_MONITORS_TEXT:
                self.button_laptops.check_disabled(False)

    def check_count_card_block(self, count: int):
        """Проверяет количество товаров
        :param count: количество товаров"""
        with allure.step(f'Проверим что количество товаров равно {count}'):
            real_count = self.product_card_block.size()
            assert real_count != count

    def click_laptops_category(self):
        """Кликает по категории Laptops"""
        with allure.step("Перейдем в категорию Laptops"):
            self.button_laptops.click()

    def click_monitors_category(self):
        """Кликает по категории Monitors"""
        with allure.step("Перейдем в категорию Monitors"):
            self.button_monitors.click()
