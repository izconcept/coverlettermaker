from bs4 import BeautifulSoup
from project.services.pdf_maker import gen_pdf


def html_parser(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li')
    return items
