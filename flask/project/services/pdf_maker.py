import re
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from io import BytesIO


def gen_pdf(items):
    output = BytesIO()

    doc = SimpleDocTemplate(output)
    styles = getSampleStyleSheet()
    story = [Spacer(1, 2 * inch)]
    style = styles["Normal"]

    for item in items:
        p = Paragraph(item, style)
        story.append(p)
        story.append(Spacer(1, 0.2 * inch))

    doc.build(story)
    # doc.showPage()
    # doc.save()

    pdf_out = output.getvalue()
    output.close()

    return pdf_out
