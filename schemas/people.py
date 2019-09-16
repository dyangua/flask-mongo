PEOPLE_SCHEMA = {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
        'unique': True
    },
    'born': {'type': 'datetime'},
    'age': {'readonly': True, 'coerce': int},
    'role': {
        'type': 'list',
        'allowed': ['author', 'contributor', 'copy'],
        'default': ['author']
    },
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string', 'required': True}
        }
    },
    'email': {
        'type': 'string',
        'regex': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    },
    'middle_name': {
        'dependencies': ['firstname', 'lastname']
    },
    'salary': {
        'anyof_type': ['integer', 'float'],
    }
}
