import pytest
from pages.checboxes_page import CheckboxesPage

@pytest.fixture
def checkboxes_page(page):
    cp = CheckboxesPage(page)
    cp.visit()
    return cp

def test_check_first_checkbox(checkboxes_page):
    checkboxes_page.check_first_checkbox()
    checkboxes_page.assert_first_checkbox_checked()

def test_uncheck_second_checkbox(checkboxes_page):
    checkboxes_page.uncheck_last_checkbox()
    checkboxes_page.assert_last_checkbox_not_checked()
