from rest_client.rest_errors import ApiError
import requests


resp = requests.get('http://127.0.0.1:8000/tracker/rest_index/')
if resp.status_code != 200:
    raise ApiError(resp.status_code, 'Error: GET /rest_index {}'.format(resp.status_code))

print(resp.json()['results'])
