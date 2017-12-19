from bs4 import BeautifulSoup
import re


def html_parser(html):
    soup = BeautifulSoup(html, 'html.parser')

    requirements = soup.body.findAll(text=re.compile('Skills'))

    print(requirements)
    print(requirements[0])
    # if len(requirements) > 0:
    #     for elem in requirements:
    #         ul = elem.parent.parent.find_next_sibling('ul')
    #         print(ul, flush=True)

    items = []

    for item in soup.findAll('li'):
        items.append(item.getText())

    return items
