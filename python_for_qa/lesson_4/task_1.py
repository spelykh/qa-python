# -*- coding: utf-8 -*-

from lxml import html

AVAILABLE_PRODUCT = 'http://deshevshe.ua/desktop-lenovo/lenovo_y900_34isz_90dd0038rk'
NOT_AVAILABLE_PRODUCT = 'http://deshevshe.ua/planshetpc-samsung/samsung_galaxy_note_101_2014_edit_308827'

def product_price(url):
    dom = html.parse(url)
    try:
        price = dom.find('//span[@itemprop="price"]')
        print(price.text)
    except:
        price = 'Відсутній у продажу'
        print price.decode('utf-8')


if __name__ == '__main__':
    product_price(AVAILABLE_PRODUCT)
    product_price(NOT_AVAILABLE_PRODUCT)