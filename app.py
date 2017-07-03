import falcon
import logging

logging.basicConfig(level=logging.DEBUG)

from controllers import versions, applications

RESOURCES = {
    '/applications': applications.CollectionResource(logging)
}

RESOURCES['/'] = versions.ItemResource(logging, RESOURCES)

app = application = falcon.API()

for route, resource in RESOURCES.items():
    app.add_route(route, resource)