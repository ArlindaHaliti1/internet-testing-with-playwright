from playwright.sync_api import Page

class FileUploadPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_input_selector = '#file-upload'
        self.submit_button_selector = '#file-submit'
        self.success_message_selector = 'h3'
        self.failure_message_selector = 'h1'
        self.uploaded_file_name_selector = '#uploaded-files'

    def visit(self):
        self.page.goto("/upload")  # Use the full URL

    def upload_file(self, file_name: str):
        self.page.locator(self.file_input_selector).set_input_files(file_name)

    def submit(self):
        self.page.locator(self.submit_button_selector).click()

    def get_success_message(self):
        return self.page.locator(self.success_message_selector).text_content()

    def get_failure_message(self):
        return self.page.locator(self.failure_message_selector).text_content()

    def get_uploaded_file_name(self):
        return self.page.locator(self.uploaded_file_name_selector).text_content()

    def assert_upload_success(self, expected_file_name: str):
        assert 'File Uploaded!' in self.get_success_message()
        assert expected_file_name in self.get_uploaded_file_name()

    def assert_upload_failure(self):
        assert 'Internal Server Error' in self.get_failure_message()
