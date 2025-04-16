import allure

from src.tests.constants import TestCheckCountProductsConst, TestCheckTextSecondProductConst


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
