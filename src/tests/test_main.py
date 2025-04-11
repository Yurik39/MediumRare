import allure

from src.tests.constants import TestCheckCountProductsConst


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
