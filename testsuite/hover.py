import pytest
from pages.hover_page import HoverPage

@pytest.fixture
def hover_page(page):
    hp = HoverPage(page)
    hp.visit()
    return hp

def test_hover_over_each_image_and_check_text(hover_page):
    expected_names = ['user1', 'user2', 'user3']
    for index, name in enumerate(expected_names):
        hover_page.hover_and_check_text(index, name)

def test_should_have_exactly_3_image_captions(hover_page):
    assert hover_page.get_image_captions().count() == 3

def test_all_captions_hidden_initially(hover_page):
    captions = hover_page.get_image_captions()
    for i in range(captions.count()):
        assert not captions.nth(i).is_visible()
