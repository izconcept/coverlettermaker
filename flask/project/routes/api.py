import urllib.request
from flask import redirect, request, Blueprint, make_response, flash

from project import logger
from project.services.parser import *
from project.services.pdf_maker import *


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/v0.0/createcover', methods=['GET'])
def create_cover():
    if request.args.get('url'):
        try:

            req = urllib.request.urlopen(request.args.get('url'))
            res_bytes = req.read()
            resp_string = res_bytes.decode("utf8")

            items = html_parser(resp_string)
            pdf_out = gen_pdf(items)

            # print(items, flush=True)

            resp = make_response(pdf_out)
            resp.headers['Content-Disposition'] = "attachment; filename='test.pdf"
            resp.mimetype = 'application/pdf'

            return redirect('/')
            # return resp

        except ValueError:
            print("bad URL", flush=True)
            flash("incorrect URL")

        except Exception:
            print(Exception, flush=True)
            flash("Server error occured")
    else:
        print('Missing URL', flush=True)
        if not request.args.get('url'):
            return "Missing URL argument"
        else:
            return "Bad Request"
