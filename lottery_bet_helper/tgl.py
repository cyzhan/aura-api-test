import random
import time
from typing import List

from const import lottery_code
from lottery_bet_helper import content

bet_type_list = ["4D_3D_2D","COLOK"]

bet_type_bet_option_dict = {
    "4D_3D_2D": ["2D", "2D_FRONT", "2D_MIDDLE", "3D", "4D"],
    "COLOK": ["COLOK_BEBAS", "COLOK_MACAU", "COLOK_NAGA", "COLOK_JITU"]
}

class BetVo:
    game_code: str
    bet_type: str
    bet_option: str
    bet_content: str
    period: str
    stake_amount: str
    discount_percent: str
    bet_amount: str
    prize_multiplier: str


def generate_randon_bets(bets_count: int, period = None) -> List[BetVo]:
    now_timestamp = int(time.time())
    bet_type_count = len(bet_type_list)
    for i in range(bets_count):
        j = (i + now_timestamp) % bet_type_count
        bet_type = bet_type_list[j]
        item = BetVo()
        if period is not None:
            item.period = period
        item.game_code = lottery_code.TGL_MIN_5
        item.bet_type = bet_type
        item.stake_amount = "1000.000"

        bet_option_count = len(bet_type_bet_option_dict[bet_type])
        bet_option_idx = random.randint(0, bet_option_count)
        bet_option = bet_type_bet_option_dict[bet_type][bet_option_idx]
        item.bet_option = bet_option
        if bet_type == "4D/3D/2D":
            item.bet_amount = "1000.000"
            item.discount_percent = "0.00"
            if bet_option == "2D" or bet_option == "2D_FRONT" or bet_option == "2D_MIDDLE":
                item.bet_content = content.four_three_two_d(2)
                item.prize_multiplier = "95"
            elif bet_option == "3D":
                item.bet_content = content.four_three_two_d(3)
                item.prize_multiplier = "950"
            elif bet_option == "4D":
                item.bet_content = content.four_three_two_d(4)
                item.prize_multiplier = "9500"
        elif bet_type == "COLOK":
            if bet_option == "COLOK_BEBAS":
                item.bet_content = content.






    return []
