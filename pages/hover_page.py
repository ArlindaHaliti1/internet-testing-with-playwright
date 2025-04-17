class HoverPage:
    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/hovers")

    def get_image_captions(self):
        return self.page.locator(".figcaption")

    def hover_and_check_text(self, index, expected_text):
        figure = self.page.locator(".figure").nth(index)
        caption = figure.locator(".figcaption")
        figure.hover()
        caption.wait_for(state="visible")
        assert expected_text in caption.inner_text().strip()
