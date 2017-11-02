from reportlab.pdfgen import canvas
from io import BytesIO
from flask import make_response, redirect, request, Blueprint, Response

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/createcover', methods=['POST'])
def create_cover():
    print('test')
    if request.method == 'POST':

        with BytesIO() as bytes_io:
            c = canvas.Canvas(bytes_io)
            c.drawString(0, 0, "Some sweet PDF.")
            c.showPage()
            c.save()

            response = Response(c)
            response.headers['Content-Disposition'] = "attachment; filename='test.pdf"
            response.mimetype = 'application/pdf'
            return response
    else:
        return redirect('/')
