import json
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
    def __init__(self):
        self.game_code = ""
        self.bet_type = ""
        self.bet_option = ""
        self.bet_content = ""
        self.period = ""
        self.stake_amount = ""
        self.discount_percent = ""
        self.bet_amount = ""
        self.prize_multiplier = ""
    # self.game_code: str
    # bet_type: str
    # bet_option: str
    # bet_content: str
    # period: str
    # stake_amount: str
    # discount_percent: str
    # bet_amount: str
    # prize_multiplier: str

    def to_dict(self):
        """
        Converts the object to a dictionary for serialization.
        """
        return {
            "game_code": self.game_code,
            "bet_type": self.bet_type,
            "bet_option": self.bet_option,
            "bet_content": self.bet_content,
            "period": self.period,
            "stake_amount": self.stake_amount,
            "discount_percent": self.discount_percent,
            "bet_amount": self.bet_amount,
            "prize_multiplier": self.prize_multiplier,
        }


def generate_randon_bets(bets_count: int, period = None) -> List[dict]:
    now_timestamp = int(time.time())
    bet_type_count = len(bet_type_list)
    payload = []
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
        bet_option_idx = random.randint(0, bet_option_count-1)
        bet_option = bet_type_bet_option_dict[bet_type][bet_option_idx]
        item.bet_option = bet_option
        if bet_type == "4D_3D_2D":
            item.stake_amount = "1000.000"
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
            item.stake_amount = "5000.000"
            item.bet_amount = "5000.000"
            item.discount_percent = "0.00"
            item.bet_content = content.colok(bet_option)
            if bet_option == "COLOK_BEBAS":
                item.prize_multiplier = "1.5"
            elif bet_option == "COLOK_MACAU":
                item.prize_multiplier = "7,14,35"
            elif bet_option == "COLOK_NAGA":
                item.prize_multiplier = "35,95"
            elif bet_option == "COLOK_JITU":
                item.prize_multiplier = "8.5"

        print(json.dumps(item.to_dict(), indent=4))
        payload.append(item.to_dict())
    return payload
