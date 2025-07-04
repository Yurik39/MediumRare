import allure
from gpn_qa_utils.ui.page_factory.button import Button
from gpn_qa_utils.ui.page_factory.component_list import ComponentList
from gpn_qa_utils.ui.page_factory.element import Element
from gpn_qa_utils.ui.page_factory.input import Input
from gpn_qa_utils.ui.pages.base import BasePage
from playwright.async_api import Page

from src.helper.URLs import BASE_URL, PRODUCT_URL
from src.tests.constants import TestCheckCountProductsConst, TestCheckTextSecondProductConst


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
                                                allure_name="Карточка товара")
        self.product_card_block_image = ComponentList(page, strategy="locator", selector=".card-img-top",
                                                      allure_name="Изображение карточки товара")
        self.button_add_to_cart = Button(page, strategy="by_text", value="Add to cart",
                                         allure_name="Кнопка Add to cart")
        self.button_cart = Button(page, strategy="locator", selector="//a[@class='nav-link' and text() = 'Cart']",
                                  allure_name="Кнопка Cart")
        self.product_name_on_product_page = Element(page, strategy="locator", selector="//h2[@class='name']",
                                                    allure_name="Наименование товара на странице продукта")
        self.cart_product_table = Element(page, strategy="locator", selector='.table',
                                          allure_name='Таблица товаров в корзине')
        self.button_delete_product_from_cart = Button(page, strategy="by_text", value="Delete",
                                                      allure_name="Кнопка Delete")
        self.button_place_order = Button(page, strategy="by_role", role="button", value="Place Order",
                                         allure_name="Кнопка Place Order")
        self.modal_title_place_order = ComponentList(self.page, strategy="locator",
                                                     selector=f'.modal-title:has-text("Place order")',
                                                     allure_name=f'Заголовок модального окна Place order')
        self.input_field_name = Input(page, strategy="locator", selector="//input[@id='name']",
                                      allure_name="Поле ввода Name")
        self.input_field_country = Input(page, strategy="locator", selector="//input[@id='country']",
                                         allure_name="Поле ввода Country")
        self.input_field_city = Input(page, strategy="locator", selector="//input[@id='city']",
                                      allure_name="Поле ввода City")
        self.input_field_card = Input(page, strategy="locator", selector="//input[@id='card']",
                                      allure_name="Поле ввода Credit card")
        self.input_field_month = Input(page, strategy="locator", selector="//input[@id='month']",
                                       allure_name="Поле ввода Month")
        self.input_field_year = Input(page, strategy="locator", selector="//input[@id='year']",
                                      allure_name="Поле ввода Year")
        self.button_purchase = Button(page, strategy="by_role", role="button", value="Purchase",
                                      allure_name="Кнопка Purchase")
        self.purchase_info_panel = Element(page, strategy="locator", selector='.sweet-alert',
                                           allure_name='Информационная панель о покупке')

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

    def card_block_count_text_repeat(self, product_name, repeated_text):
        """Считает количество повторений слова в карточке продукта {product_model}
        :param product_name: имя продукта в карточке
        :param repeated_text: повторяющийся текст"""
        with allure.step(f'Проверим повторение текста {repeated_text} в описании товара {product_name}'):
            product_card = ComponentList(self.page, strategy="locator",
                                         selector=f'.card-block:has-text("{product_name}")',
                                         allure_name=f'Карточка продукта {product_name}')
            text = product_card.get_text()
            count_word_repeat = text.count(repeated_text)
            assert count_word_repeat == TestCheckTextSecondProductConst.COUNT_REPEATED_TEXT

    def click_on_card_block_by_index(self, index: int):
        """Кликает по карточке продукта с индексом {index}
        :param index: индекс карточки продукта"""
        with allure.step(f'Кликнем по карточке продукта с индексом {index}'):
            self.product_card_block_image.item(item_number=index).check_disabled(False)
            self.product_card_block_image.item(item_number=index).click()

    def check_product_expected_url(self, product_index: str):
        """Проверяет соответствие текущего и ожидаемого URL продукта
        :param product_index: индекс продукта"""
        current_url = self.browser.get_current_url()
        expected_url = f'{BASE_URL}{PRODUCT_URL}{product_index}'
        assert current_url == expected_url

    def click_button_add_to_cart(self):
        """Кликает по кнопке Add to cart"""
        self.button_add_to_cart.check_disabled(False)
        self.button_add_to_cart.click()

    def click_button_cart(self):
        """Кликает по кнопке перехода в корзину"""
        self.button_cart.check_disabled(False)
        self.button_cart.click()

    def check_expected_url(self, expected_url: str):
        """Проверяет соответствие текущего и ожидаемого URL
        :param expected_url: ожидаемый URL"""
        current_url = self.browser.get_current_url()
        expected_url = f'{BASE_URL}{expected_url}'
        assert current_url == expected_url

    def check_have_product_in_cart(self, product_name):
        """Проверяет наличие товара в таблице корзины
        :param product_name: наименование продукта"""
        self.cart_product_table.contains_text(product_name)

    def click_button_delete_from_cart(self):
        """Кликает по кнопке Delete в таблице корзины"""
        self.button_delete_product_from_cart.click()

    def check_not_have_product_in_cart(self, product_name):
        """Проверяет отсутствие товара в таблице корзины
        :param product_name: наименование продукта"""
        self.cart_product_table.not_have_text(product_name)

    def click_button_place_order(self):
        """Кликает по кнопке Place order"""
        self.button_place_order.click()

    def check_visible_modal_window(self):
        """Проверяет отображение модального окна Place order"""
        self.modal_title_place_order.check_visible(False)

    def input_place_order_field(self, name, country, city, credit_card, month, year):
        """Заполняет поля ввода в модальном окне Place order
        :param name: Имя покупателя
        :param country: Страна
        :param city: Город
        :param credit_card: номер кредитной карты
        :param month: Месяц
        :param year: Год"""
        self.input_field_name.fill(name)
        self.input_field_country.fill(country)
        self.input_field_city.fill(city)
        self.input_field_card.fill(credit_card)
        self.input_field_month.fill(month)
        self.input_field_year.fill(year)

    def click_purchase_button(self, purchase_accepted_text, name):
        """Кликает по кнопке Purschase, проверяет отображение текста {purchase_accepted_text} и соответсвие поля {name}
        :param purchase_accepted_text: Текст успешной покупки
        :param name: Имя покупателя"""
        self.button_purchase.click()
        self.purchase_info_panel.contains_text(purchase_accepted_text)
        self.purchase_info_panel.contains_text(f'Name: {name}')
