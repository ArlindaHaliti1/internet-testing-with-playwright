import pytest
from pages.draganddrop_page import DragAndDropPage

@pytest.fixture
def dnd_page(page):
    dnd = DragAndDropPage(page)
    dnd.visit()
    return dnd

def test_initial_order_and_drag_b_to_a(dnd_page):
    dnd_page.assert_column_texts("A", "B")
    dnd_page.drag_b_to_a()
    dnd_page.assert_column_texts("B", "A")

def test_multiple_drag_operations(dnd_page):
    dnd_page.drag_b_to_a()
    dnd_page.assert_column_texts("B", "A")
    
    dnd_page.drag_a_to_b()
    dnd_page.assert_column_texts("A", "B")

def test_elements_are_visible_and_exist(dnd_page):
    assert dnd_page.get_column_a().is_visible()
    assert dnd_page.get_column_b().is_visible()
