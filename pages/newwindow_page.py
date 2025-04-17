from playwright.sync_api import Page

class WindowsPage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self):
        self.page.goto('/windows')

    def click_link_and_assert_url(self):
        link = self.page.locator('a').nth(1)
        href = link.get_attribute('href')
        target = link.get_attribute('target')
        
        assert href == '/windows/new', f"Expected href '/windows/new' but got {href}"
        assert target == '_blank', f"Expected target '_blank' but got {target}"

        link.evaluate('a => a.setAttribute("target", "_self")')
        link.click()

    def assert_new_window(self):
        assert '/windows/new' in self.page.url, f"URL should include '/windows/new', but got {self.page.url}"
        header = self.page.locator('h3')
        assert header.inner_text() == 'New Window', f"Expected header 'New Window' but got {header.inner_text()}"

    def assert_link_does_not_open_new_window(self):
        link = self.page.locator('a').nth(1)
        target = link.get_attribute('target')
        
        assert target != '_self', f"Expected target not to be '_self', but got {target}"
        
        link.click()
        assert '/windows/new' not in self.page.url, f"URL should not include '/windows/new', but got {self.page.url}"

    def assert_incorrect_header(self):
        assert '/windows/new' not in self.page.url, f"URL should not include '/windows/new', but got {self.page.url}"
        header = self.page.locator('h3')
        assert header.inner_text() != 'New Window', f"Expected header not to be 'New Window', but got {header.inner_text()}"

