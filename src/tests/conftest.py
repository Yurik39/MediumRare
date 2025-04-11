from pathlib import Path

import pytest
from gpn_qa_utils.ui.browser_launcher import BrowserLauncher

from src.pages.main_page import MainPage

config_browser = Path(__file__).parent / "config_browser.yaml"

@pytest.fixture(scope="function")
def browser():
    browser = BrowserLauncher(local_browser_config_path=config_browser)
    new_page = browser.create_page()
    yield new_page
    browser.close()

@pytest.fixture(scope="function")
def main_page(browser):
    """Методы главной страницы"""
    return MainPage(browser)