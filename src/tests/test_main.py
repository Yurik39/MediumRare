import allure

from src.helper.URLs import CART_URL
from src.tests.constants import TestCheckCountProductsConst, TestCheckTextSecondProductConst, \
    TestAddAndRemoveProductsFromCartConst


@allure.feature("Главная страница")
class TestMain:

    @allure.title("Проверка количества товаров")
    def test_check_count_products(self, main_page):
        main_page.open()
        main_page.check_title(TestCheckCountProductsConst.TITLE_CATEGORIES)
        main_page.check_button_is_active(TestCheckCountProductsConst.BUTTON_PHONES_TEXT)
        main_page.check_count_card_block(TestCheckCountProductsConst.MAX_COUNT_CARD_BLOCK_ON_PAGE)
        main_page.check_button_is_active(TestCheckCountProductsConst.BUTTON_LAPTOPS_TEXT)
        main_page.click_laptops_category()
        main_page.check_count_card_block(TestCheckCountProductsConst.COUNT_LAPTOPS_CARD_BLOCK)
        main_page.check_button_is_active(TestCheckCountProductsConst.BUTTON_MONITORS_TEXT)
        main_page.click_monitors_category()
        main_page.check_count_card_block(TestCheckCountProductsConst.COUNT_MONITORS_CARD_BLOCK)

    @allure.title("Проверка соответствия описания вторых товаров")
    def test_check_text_second_product(self, main_page):
        main_page.open()
        main_page.card_block_count_text_repeat(TestCheckTextSecondProductConst.PRODUCT_NAME_NOKIA,
                                               TestCheckTextSecondProductConst.REPEATED_TEXT_NOKIA)
        main_page.check_button_is_active(TestCheckCountProductsConst.BUTTON_LAPTOPS_TEXT)
        main_page.click_laptops_category()
        main_page.card_block_count_text_repeat(TestCheckTextSecondProductConst.PRODUCT_NAME_SONY_VAIO_I5,
                                               TestCheckTextSecondProductConst.REPEATED_TEXT_SONY)
        main_page.check_button_is_active(TestCheckCountProductsConst.BUTTON_MONITORS_TEXT)
        main_page.click_monitors_category()
        main_page.card_block_count_text_repeat(TestCheckTextSecondProductConst.PRODUCT_NAME_ASUS,
                                               TestCheckTextSecondProductConst.REPEATED_TEXT_ASUS)

    @allure.title("Проверка добавления и удаления товаров из корзины")
    def test_add_and_remove_products_from_cart(self, main_page):
        main_page.open()
        main_page.click_on_card_block_by_index(TestAddAndRemoveProductsFromCartConst.PRODUCT_CARD_INDEX)
        main_page.check_product_expected_url(TestAddAndRemoveProductsFromCartConst.PRODUCT_INDEX)
        main_page.click_button_add_to_cart()
        main_page.click_button_cart()
        main_page.check_expected_url(CART_URL)
        main_page.check_have_product_in_cart(TestAddAndRemoveProductsFromCartConst.PRODUCT_NAME)
        main_page.click_button_delete_from_cart()
        main_page.check_not_have_product_in_cart(TestAddAndRemoveProductsFromCartConst.PRODUCT_NAME)
