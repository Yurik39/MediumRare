from dataclasses import dataclass


@dataclass
class TestCheckCountProductsConst:
    TITLE_CATEGORIES = "CATEGORIES"
    MAX_COUNT_CARD_BLOCK_ON_PAGE = 9
    COUNT_LAPTOPS_CARD_BLOCK = 6
    COUNT_MONITORS_CARD_BLOCK = 2
    BUTTON_PHONES_TEXT = "Phones"
    BUTTON_LAPTOPS_TEXT = "Laptops"
    BUTTON_MONITORS_TEXT = "Monitors"


class TestCheckTextSecondProductConst:
    PRODUCT_NAME_NOKIA = "Nokia"
    REPEATED_TEXT_NOKIA = "Nokia"
    PRODUCT_NAME_SONY_VAIO_I5 = "Sony vaio i5"
    REPEATED_TEXT_SONY = "Sony"
    PRODUCT_NAME_ASUS = "Asus"
    REPEATED_TEXT_ASUS = "ASUS"
    COUNT_REPEATED_TEXT = 2
