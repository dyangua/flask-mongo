from schemas.people import PEOPLE_SCHEMA
from schemas.work import WORK_SCHEMA

X_DOMAINS = ['http://127.0.0.1:3000']

# methods allowed at the resource (collection) endpoint
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# method allowed at the item (document) endpoint
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# uri
MONGO_URI = 'mongodb://root:abc123@ds161529.mlab.com:61529/flask-mongo?retryWrites=false'

# domain def (collection)
DOMAIN = {'people': {'schema': PEOPLE_SCHEMA},
          'works': {'resource_methods': ['GET'], 'item_methods': ['GET'], 'schema': WORK_SCHEMA}}
