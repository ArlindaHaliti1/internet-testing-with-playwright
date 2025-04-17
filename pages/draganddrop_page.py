from playwright.sync_api import Page

class DragAndDropPage:
    def __init__(self, page: Page):
        self.page = page
        self.column_a = page.locator("#column-a")
        self.column_b = page.locator("#column-b")

    def visit(self):
        self.page.goto("/drag_and_drop")

    def get_column_a(self):
        return self.column_a

    def get_column_b(self):
        return self.column_b

    def drag_a_to_b(self):
        self.column_a.drag_to(self.column_b)

    def drag_b_to_a(self):
        self.column_b.drag_to(self.column_a)

    def assert_column_texts(self, expected_text_a: str, expected_text_b: str):
        assert self.column_a.inner_text().strip() == expected_text_a
        assert self.column_b.inner_text().strip() == expected_text_b
