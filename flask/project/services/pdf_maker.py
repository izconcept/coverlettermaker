from reportlab.pdfgen import canvas
from io import BytesIO


def gen_pdf(items):
    output = BytesIO()
    p = canvas.Canvas(output)
    p.drawString(100, 100, 'Hello')
    p.showPage()
    p.save()

    pdf_out = output.getvalue()
    output.close()

    return pdf_out
