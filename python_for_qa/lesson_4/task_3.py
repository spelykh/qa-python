# -*- coding: utf-8 -*-


import xml.etree.ElementTree as etree

def main():
    habr = etree.parse('habraharb_all.xml')
    root = habr.getroot()

    for item in root.iter('item'):
        title = item.find('title').text.strip()
        author = item.find('author').text.strip()

        category = item.findall('category')

        data = []
        for item in category:
            data.append(item.text)

        print "-Author \"{}\",\nArticle \"{}\",\nCategories - {}".format(author, title.encode('utf-8'), ', '.join(data).encode('utf-8'))

if __name__ == '__main__':
    main()