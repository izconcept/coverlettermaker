from bs4 import BeautifulSoup


def html_parser(html):
    soup = BeautifulSoup(html, 'html.parser')

    items = []

    for item in soup.findAll('li'):
        items.append(item.getText())

    return items
