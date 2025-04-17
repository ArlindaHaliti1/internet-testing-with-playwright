import pytest
from pages.newwindow_page import WindowsPage  

@pytest.fixture
def windows_page(page):
    return WindowsPage(page)

def test_clicks_in_a_new_window_and_asserts_url(windows_page):
    windows_page.visit()
    windows_page.click_link_and_assert_url()
    windows_page.assert_new_window()

def test_should_not_open_a_new_window_with_target_self(windows_page):
    windows_page.visit()
    windows_page.assert_link_does_not_open_new_window()

def test_should_not_have_header_text_new_window(windows_page):
    windows_page.visit()
    windows_page.assert_incorrect_header()
