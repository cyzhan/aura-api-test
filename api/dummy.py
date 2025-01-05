import json

import requests


_POST = 'POST'
_GET = 'GET'
_PUT = 'PUT'
_GET_GAME_LINK_PATH = '/platform/game-link'
_base_url = ''


def set_env(env_data: dict):
    global _base_url
    _base_url = env_data['DUMMY_BASE_URL']


def get_game_link(body: dict) -> dict:
    response = requests.post(_base_url + _GET_GAME_LINK_PATH, json=body)
    print('{} - {}  {}'.format(response.status_code, _POST, _GET_GAME_LINK_PATH))
    json_dict = response.json()
    print(json.dumps(json_dict, indent=4))
    return json_dict['data']
