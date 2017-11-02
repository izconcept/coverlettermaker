from reportlab.pdfgen import canvas
from io import BytesIO
from flask import redirect, request, Blueprint, Response, make_response

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/createcover', methods=['GET'])
def create_cover():
    if request.args.get('url'):
        output = BytesIO()

        p = canvas.Canvas(output)
        p.drawString(100, 100, 'Hello')
        p.showPage()
        p.save()

        pdf_out = output.getvalue()
        output.close()

        response = make_response(pdf_out)
        response.headers['Content-Disposition'] = "attachment; filename='test.pdf"
        response.mimetype = 'application/pdf'
        return response
    else:
        return redirect("/")
