import pytest
from pages.javascriptalert_page import JavascriptAlertsPage

@pytest.fixture
def javascript_alerts_page(page):
   
    jap = JavascriptAlertsPage(page)
    jap.visit() 
    return jap

def test_click_js_alert_and_assert(javascript_alerts_page):
    javascript_alerts_page.click_js_alert_and_assert()

def test_click_js_confirm_and_assert(javascript_alerts_page):
    javascript_alerts_page.click_js_confirm_and_assert()

def test_click_js_prompt_and_assert(javascript_alerts_page):
    javascript_alerts_page.click_js_prompt_and_assert()
