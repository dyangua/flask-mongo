import json

import requests

KEY_ITEMS = '_items'
KEY_FIRSTNAME = 'firstname'
KEY_LASTNAME = 'lastname'


def url_for(endpoint):
    return 'http://localhost:5000/{}/'.format(endpoint)


def get_all_people():
    resp = requests.get(url_for('people'))

    if resp.status_code == 200:
        people = resp.json()[KEY_ITEMS]
        for person in people:
            print('{}, {}'.format(person[KEY_FIRSTNAME], person[KEY_LASTNAME]))

    print("server responde", resp.status_code)


def post_data():
    data = [{'firstname': 'Angelo', 'lastname': 'Funky'},
            {'firstname': 'James', 'lastname': 'Brown'}]

    resp = requests.post(url_for('people'), json.dumps(data), headers={'Content-Type': 'application/json'})
    print("server responde", resp.status_code)


def main():
    get_all_people()
    # post_data()


if __name__ == '__main__':
    main()
