import urllib.request
from flask import redirect, request, Blueprint, make_response, flash
from project.services.parser import *
from project.services.pdf_maker import *


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/createcover', methods=['GET'])
def create_cover():
    if request.args.get('url'):

        req = urllib.request.urlopen(request.args.get('url'))
        res_bytes = req.read()
        resp_string = res_bytes.decode("utf8")

        items = html_parser(resp_string)
        pdf_out = gen_pdf(items)

        response = make_response(pdf_out)
        response.headers['Content-Disposition'] = "attachment; filename='test.pdf"
        response.mimetype = 'application/pdf'

        return response
    else:
        return redirect("/")
