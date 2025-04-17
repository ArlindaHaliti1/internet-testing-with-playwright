import pytest
from pages.upload_page import FileUploadPage

# Pytest fixture for creating the FileUploadPage object
@pytest.fixture
def file_upload_page(page):
    up = FileUploadPage(page)
    up.visit()  # Visit the page as part of the fixture setup
    return up

# Test case to upload a valid file and verify the upload success
def test_upload_valid_file(file_upload_page):
    file_upload_page.upload_file(
        'C:/Users/ArlindaHaliti/OneDrive - Telos-Labs/Desktop/internet-testing-with-playwright/utilities/playwright.txt'
    )
    file_upload_page.submit()
    file_upload_page.assert_upload_success('playwright.txt')

# Test case for submitting without selecting a file
def test_upload_without_file(file_upload_page):
    file_upload_page.submit()  # Submitting without uploading a file
    file_upload_page.assert_upload_failure()
