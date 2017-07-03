''' Applications CRUD
'''

import falcon
import json


class CollectionResource(object):

    def __init__(self, logger):
        self.logger = logger


class ItemResource(object):

    def __init__(self, logger):
        self.logger = logger

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({
            'result': 'true'
        })