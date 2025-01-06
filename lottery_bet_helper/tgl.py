import time
from typing import List


bet_type_list = ["2D", "2D_FRONT", "2D_MIDDLE", "3D", "4D", "COLOK_BEBAS", "COLOK_MACAU", "COLOK_NAGA", "COLOK_JITU"]

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


def generate_randon_bets(bets_count: int) -> List[BetVo]:
    now_timestamp = int(time.time())
    for i in range(bets_count):
        j = (i + now_timestamp) % len(bet_type_list)
        bet_type = bet_type_list[j]

    return []
