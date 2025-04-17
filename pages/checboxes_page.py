from playwright.sync_api import Page

class CheckboxesPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkbox_selector = '#checkboxes input[type="checkbox"]'

    def visit(self):
        self.page.goto("/checkboxes")

    def get_checkboxes(self):
        return self.page.locator(self.checkbox_selector)

    def check_first_checkbox(self):
        self.get_checkboxes().nth(0).check()

    def uncheck_last_checkbox(self):
        self.get_checkboxes().nth(1).uncheck()

    def assert_first_checkbox_checked(self):
        assert self.get_checkboxes().nth(0).is_checked()

    def assert_last_checkbox_not_checked(self):
        assert not self.get_checkboxes().nth(1).is_checked()
