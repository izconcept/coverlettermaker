import PyPDF2


def parse_cv(pdf):

    pdf_reader = PyPDF2.PdfFileReader(pdf)

    page = pdf_reader.getPage(0)
    print(page.extractText())
