from bs4 import BeautifulSoup
import re


def html_parser(html):
    soup = BeautifulSoup(html, 'html.parser')

    requirements = soup.body.findAll(text=re.compile('Skills'))

    requirements_found = True

    items = []

    while requirements_found:
        print(requirements)
        for i in range(0, len(requirements)):
            requirements[i] = requirements[i].parent
            req = requirements[i]
            ul = req.find_next_sibling('ul')
            if ul is not None:
                list_items = ul.findAll('li')
                for li in list_items:
                    if li.text != '':
                        items.append(li.text)
                requirements_found = False

    return items
