from bs4 import BeautifulSoup


def html_parser(html):
    soup = BeautifulSoup(html, 'html.parser')

    print(soup.prettify())

    items = soup.find_all('li')
    print(items)
    return items
