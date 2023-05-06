from .pages.product_page import ProductPage
import pytest

link_start = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
link = [f'{link_start}{i}' for i in range(10)]

@pytest.mark.parametrize('link', link)
def test_guest_can_add_product_to_basket(browser, link):
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()


