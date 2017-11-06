import urllib.request
from flask import redirect, request, Blueprint, make_response, flash

from project import logger
from project.services.parser import *
from project.services.pdf_maker import *


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/v0.0/createcover', methods=['POST'])
def create_cover():
    if request.args.get('url'):
        try:

            req = urllib.request.urlopen(request.args.get('url'))
            res_bytes = req.read()
            resp_string = res_bytes.decode("utf8")

            items = html_parser(resp_string)
            pdf_out = gen_pdf(items)

            response = make_response(pdf_out)
            response.headers['Content-Disposition'] = "attachment; filename='test.pdf"
            response.mimetype = 'application/pdf'

            return response

        except ValueError:
            print("bad URL")
            flash("incorrect URL")

        except Exception:
            print(Exception)
            flash("Server error occured")
    else:
        if not request.args.get('url'):
            return "Missing URL argument"
        else:
            return "Bad Request"
