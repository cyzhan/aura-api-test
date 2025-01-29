import time
from datetime import datetime
from functools import wraps
from urllib.parse import urlparse, parse_qs

from api import dummy, game
from const.lottery_code import LotteryCode
from lottery_bet_helper import tgl

_DIVIDER = '---------------------------------------------------------------------------------'

def timer(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start_milliseconds = round(time.time() * 1000)
        res = func(*args, **kwargs)
        end_milliseconds = round(time.time() * 1000)
        spend_milliseconds = end_milliseconds - start_milliseconds
        print(f"time spend : {spend_milliseconds} milliseconds")
        return res
    return wrap

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

    with open("auth.txt", "w") as file:
        file.write(jwt_token)
    return jwt_token


@timer
def placing_bets(token: str, game_code: str, bets_count: int):
    data_dict = game.get_lottery_game_current_info(token, game_code)
    next_period = data_dict["next_period"]
    next_draw_time = data_dict["next_draw_time"]
    now_timestamp = int(time.time())
    if next_draw_time - now_timestamp < 30:
        date_time = datetime.fromtimestamp(next_draw_time).strftime("%Y-%m-%d %H:%M:%S")
        print(f"invalid bet time. Next draw_time = {date_time}")
        return
    # check game_code to see if periodic or instant
    payload = {
        "game_code": game_code,
        "period": next_period
    }

    # bets = tgl.generate_randon_bets(game_code=game_code, bets_count=bets_count)
    from lottery_bet_helper.tgl import togel
    bets = togel.generate_randon_bets(game_code=game_code, bets_count=bets_count)
    payload["bets"] = bets
    game.placing_bets(token=token, body=payload)


def run_all_once(token: str):
    game.get_balance(token=token)
    print(_DIVIDER)
    game.get_lottery_game_setting(token=token, game_code=LotteryCode.TGL_MIN_5.value)
    print(_DIVIDER)
    game.get_lottery_bet_limit(token=token, game_code=LotteryCode.TGL_MIN_5.value)
    print(_DIVIDER)
    game.get_lottery_get_properties(token=token)
    print(_DIVIDER)
    game.get_lottery_game_current_info(token=token, game_code=LotteryCode.TGL_MIN_5.value)
    print(_DIVIDER)
    game.lottery_get_game_history(token=token, game_code=LotteryCode.TGL_MIN_5.value)
    print(_DIVIDER)
    game.lottery_get_bet_history(token=token)

