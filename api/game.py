import json
import time

import requests


_POST = 'POST'
_GET = 'GET'
_PUT = 'PUT'
_UUID_LOGIN_PATH = '/v1/player/login'
_GET_BALANCE = '/v1/player/balance'
_LOTTERY_GAME_CURRENT_INFO = '/v1/lottery/:game_code/current-info'
_LOTTERY_GAME_SETTING = '/v1/lottery/:game_code/setting'
_LOTTERY_PROPERTIES = '/v1/lottery/properties'
_LOTTERY_BET_LIMIT = '/v1/lottery/:game_code/bet-limit'
_DRAWING_NUMBERS = '/v1/lottery/:game_code/numbers'
_PLACING_BETS = '/v1/lottery/bets'
_LOTTERY_BET_HISTORY = '/v1/lottery/bets'
_base_url = ''


def set_env(env_data: dict):
    global _base_url
    _base_url = env_data['GAME_API_BASE_URL']


def uuid_login(body: dict) -> dict:
    response = requests.post(_base_url + _UUID_LOGIN_PATH, json=body)
    print('{} - {}  {}'.format(response.status_code, _POST, _UUID_LOGIN_PATH))
    json_dict = response.json()
    print(json.dumps(json_dict, indent=4))
    return json_dict['data']


def get_balance(token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url=_base_url + _GET_BALANCE, headers=headers)
    print(f"{response.status_code} - {_GET}  {_GET_BALANCE}")
    json_dict = response.json()
    print(json.dumps(json_dict, indent=4))
    return json_dict['data']


def get_lottery_game_current_info(token: str, game_code: str) -> dict:
    request_path = _LOTTERY_GAME_CURRENT_INFO.replace(':game_code', game_code)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url=_base_url + request_path, headers=headers)
    print(f"{response.status_code} - {_GET}  {request_path}")
    json_dict = response.json()
    print(json.dumps(json_dict, indent=4))
    return json_dict['data']


def get_lottery_game_setting(token: str, game_code: str) -> dict:
    request_path = _LOTTERY_GAME_SETTING.replace(':game_code', game_code)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url=_base_url + request_path, headers=headers)
    print(f"{response.status_code} - {_GET}  {request_path}")
    json_dict = response.json()
    print(json.dumps(json_dict, indent=4))
    return json_dict['data']


def get_lottery_bet_limit(token: str, game_code: str) -> dict:
    request_path = _LOTTERY_BET_LIMIT.replace(':game_code', game_code)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url=_base_url + request_path, headers=headers)
    print(f"{response.status_code} - {_GET}  {request_path}")
    json_dict = response.json()
    print(json.dumps(json_dict, indent=4))
    return json_dict['data']


def get_lottery_get_properties(token: str, params=None) -> dict:
    from const import lottery_code
    if params is None:
        params = {
            "game_code": lottery_code.TGL_MIN_5,
        }

    path = _LOTTERY_PROPERTIES + "?"
    for k, v in params.items():
        path += k + "=" + v

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url=_base_url + path, headers=headers)
    print(f"{response.status_code} - {_GET}  {path}")
    json_dict = response.json()
    print(json.dumps(json_dict, indent=4))
    return json_dict['data']


def lottery_get_game_history(token: str, game_code: str, params=None):
    now_timestamp = int(time.time())
    if params is None:
        params = {
            "page": "1",
            "page_size": "10",
            "start_time": str(now_timestamp - 3600),
            "end_time": str(now_timestamp)
        }

    path = _DRAWING_NUMBERS.replace(":game_code", game_code) + "?"
    for k, v in params.items():
        path += k + "=" + v + "&"
    path = path[:-1]

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url=_base_url + path, headers=headers)
    print(f"{response.status_code} - {_GET}  {path}")
    json_dict = response.json()
    print(json.dumps(json_dict, indent=4))
    return json_dict['data']


def placing_bets(token: str, body: any) -> dict:
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url=_base_url + _PLACING_BETS, headers=headers, json=body)
    print(f"{response.status_code} - {_POST}  {_PLACING_BETS}")
    json_dict = response.json()
    print(json.dumps(json_dict, indent=4))
    return json_dict['data']


def lottery_get_bet_history(token: str, params=None) -> dict:
    now_timestamp = int(time.time())
    if params is None:
        params = {
            "page": "1",
            "page_size": "10",
            "start_time": str(now_timestamp - 604800),
            "end_time": str(now_timestamp)
        }

    path = _LOTTERY_BET_HISTORY + "?"
    for k, v in params.items():
        path += k + "=" + v + "&"
    path = path[:-1]
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url=_base_url + path, headers=headers)
    print(f"{response.status_code} - {_GET}  {path}")
    json_dict = response.json()
    print(json.dumps(json_dict, indent=4))
    return json_dict['data']