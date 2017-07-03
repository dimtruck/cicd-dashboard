''' Version resource
'''
import falcon
import json

class ItemResource(object):

    def __init__(self, logger, resources):
        self.logger = logger
        self.resources = resources

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(sorted(list(self.resources.keys())))