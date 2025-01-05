import time

from dotenv import dotenv_values
from api import dummy, game
from const import game_code
from process import process

if __name__ == '__main__':
    env_data = dotenv_values(".env.dev")
    dummy.set_env(env_data)
    game.set_env(env_data)

    with open("auth.txt", "r") as file:
        # Read the entire content of the file
        token = file.read()
    if token == '':
        token = process.get_link_and_login()

    # run process
    process.run_all_once(token)

    # params = {
    #     "page": 1,
    #     "page_size": 10,
    #     "start_time": int(time.time()) - 3700,
    #     "end_time": int(time.time()) - 100
    # }
    # game.get_drawing_numbers(token=token, game_code=game_code.TGL_MIN_5, params=params)

    process.placing_bets(token=token, game_code=game_code.TGL_MIN_5, bets_count=20)


