import time
from datetime import datetime
from urllib.parse import urlparse, parse_qs

from api import dummy, game
from const import game_code
from utils import content

_DIVIDER = '---------------------------------------------------------------------------------'


def get_link_and_login() -> str:
    payload = {
        'account': 'jeff007',
        'currency_code': 'IDR',
        'target': 'target',
        'timezone': 'Asia/Taipei'
    }

    data_dict = dummy.get_game_link(payload)
    parsed_url = urlparse(data_dict['link'])
    query_params = parse_qs(parsed_url.query)
    token = query_params.get('token', [None])[0]
    if token is None:
        print('link is not present')
        raise Exception('link is not present')
    else:
        print('token = {}'.format(token))

    print(_DIVIDER)
    payload = {
        'token': token,
        'device': 'PC'
    }
    data_dict = game.uuid_login(payload)
    jwt_token = data_dict['token']
    print('jwt = {}'.format(jwt_token))
    print('ws_link = {}'.format(data_dict['websocket_link']))

    with open("temp.txt", "w") as file:
        file.write(jwt_token)
    return jwt_token


def placing_bets(token: str, game_code: str, bets_count: int):
    data_dict = game.get_lottery_game_current_info(token, game_code)
    next_period = data_dict["next_period"]
    next_draw_time = data_dict["next_draw_time"]
    now_timestamp = int(time.time())
    if next_draw_time - now_timestamp < 30:
        date_time = datetime.fromtimestamp(next_draw_time).strftime("%Y-%m-%d %H:%M:%S")
        print('invalid bet time. Next draw_time = {}', date_time)
        return

    bet_types = ["2D", "2D_FRONT", "2D_MIDDLE", "3D", "4D"]
    payload = []
    for i in range(bets_count):
        j = (i + now_timestamp) % 5
        bet_type = bet_types[j]
        bet_content = ""
        prize_multiplier = ""
        if bet_type == "2D" or bet_type == "2D_FRONT" or bet_type == "2D_MIDDLE":
            bet_content = content.generator_1(2)
            prize_multiplier = "95"
        elif bet_type == "3D":
            bet_content = content.generator_1(3)
            prize_multiplier = "950"
        elif bet_type == "4D":
            bet_content = content.generator_1(4)
            prize_multiplier = "9500"

        item = {
            "game_type": "LOTTERY",
            "game_code": game_code,
            "bet_type": "4D_3D_2D",
            "bet_option": bet_type,
            "bet_content": bet_content,
            "period": str(next_period),
            "stake_amount": "1000.000",
            "discount_percent": "0.00",
            "bet_amount": "1000.000",
            "prize_multiplier": prize_multiplier
        }
        print('bet_option:{}, bet_content:{}'.format(bet_type, bet_content))
        payload.append(item)

    game.placing_bets(token=token, body=payload)


def run_all_once(token: str):
    game.get_balance(token=token)
    print(_DIVIDER)
    game.get_lottery_game_setting(token=token, game_code=game_code.TGL_MIN_5)
    print(_DIVIDER)
    game.get_lottery_bet_limit(token=token, game_code=game_code.TGL_MIN_5)
    print(_DIVIDER)
    game.get_lottery_get_properties(token=token)
    print(_DIVIDER)
    game.get_lottery_game_current_info(token=token, game_code=game_code.TGL_MIN_5)
    print(_DIVIDER)
    game.lottery_get_game_history(token=token, game_code=game_code.TGL_MIN_5)
    print(_DIVIDER)
    game.lottery_get_bet_history(token=token)

