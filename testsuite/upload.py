import pytest
from pages.upload_page import FileUploadPage


@pytest.fixture
def file_upload_page(page):
    up = FileUploadPage(page)
    up.visit()  
    return up


def test_upload_valid_file(file_upload_page):
    file_upload_page.upload_file(
        './utilities/playwright.txt'
    )
    file_upload_page.submit()
    file_upload_page.assert_upload_success('playwright.txt')

def test_upload_without_file(file_upload_page): 
    file_upload_page.submit()  
    file_upload_page.assert_upload_failure()
