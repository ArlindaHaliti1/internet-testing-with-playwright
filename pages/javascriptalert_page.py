from playwright.sync_api import Page

class JavascriptAlertsPage:
    def __init__(self, page: Page):
        self.page = page
    
    def visit(self):
        self.page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    def click_js_alert_and_assert(self):
        self.page.click('button[onclick="jsAlert()"]')
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.locator('#result').wait_for(state="visible")
        result_text = self.page.locator('#result').inner_text()
        assert result_text == "You successfully clicked an alert"
        print(result_text)
    def click_js_confirm_and_assert(self):
        def handle_dialog(dialog):
            dialog.accept()

        self.page.on("dialog", handle_dialog)
        self.page.click('button[onclick="jsConfirm()"]')
        result_text = self.page.locator("#result").inner_text().strip()
        assert result_text == "You clicked: Ok", f"Expected 'You clicked: Ok', but got: {result_text}"



    def click_js_prompt_and_assert(self):
        text_input = "Hello World"
        self.page.on("dialog", lambda dialog: dialog.accept(text_input))
        self.page.click('button[onclick="jsPrompt()"]')
        self.page.locator('#result').wait_for(state="visible")
        result_text = self.page.locator('#result').inner_text()
        assert text_input in result_text
