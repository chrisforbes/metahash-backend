import logging

import os
import simplejson as json

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from metahash.lib.base import BaseController, render

log = logging.getLogger(__name__)

class FileController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/file.mako')
        # or, return a response
        return 'Hello World'

    def get(self, hash, format='json'):
        d = os.curdir + '/file/'
        files = os.listdir(d)
        if hash in files:
            f = open(d + hash, 'r')
            if format == 'json':
                response.headers['content-type'] = 'text/javascript'
                return f.read()
            else:
                c.data = json.load(f)
                return render('file.mako')
            f.close()
        else:
            abort(404, '404 File Not Found')

    def update(self, hash):
        pass

