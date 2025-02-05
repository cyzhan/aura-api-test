import decimal
import json
import random
import time
from typing import List


class BetVo:
    def __init__(self):
        self.bet_type: str = ""
        self.bet_option: str = ""
        self.bet_content: str = ""
        self.stake_amount: str = ""
        self.discount_percent: str = ""
        self.kei_percent: str = ""
        self.bet_amount: str = ""
        self.prize_multiplier = ""

    def to_dict(self):
        """
        Converts the object to a dictionary for serialization.
        """
        data = {
            "bet_type": self.bet_type,
            "bet_option": self.bet_option,
            "bet_content": self.bet_content,
            "stake_amount": self.stake_amount,
            "bet_amount": self.bet_amount,
            "prize_multiplier": self.prize_multiplier,
        }
        if self.discount_percent != "":
            data["discount_percent"] = self.discount_percent
        if self.kei_percent != "":
            data["kei_percent"] = self.kei_percent
        return data

def non_repeat_numbers(n :int) -> list[str]:
    if n == 0:
        return []

    m = {}
    while True:
        m[str(random.randint(0, 9))] = True
        if len(m) == n:
            return list(m.keys())


class ContentHelper:
    def __init__(self):
        self.__colok_jitu_options = ["AS", "KOP", "KEPALA", "EKOR"]
        self.__fifty_fifty_general_options = ["BIG", "SMALL", "ODD", "EVEN", "MID", "EDGE"]
        self.__fifty_fifty_special_options_1 = ["AS", "KOP", "KEPALA", "EKOR"]
        self.__fifty_fifty_special_options_2 = ["BIG", "SMALL", "ODD", "EVEN"]
        self.__fifty_fifty_combi_mono = ["MONO,FRONT", "MONO,MID", "MONO,END"]
        self.__fifty_fifty_combi_stereo = ["STEREO,FRONT", "STEREO,MID", "STEREO,END"]
        self.__fifty_fifty_combi_inflate = ["INFLATE,FRONT", "INFLATE,MID", "INFLATE,END"]
        self.__fifty_fifty_combi_deflate = ["DEFLATE,FRONT", "DEFLATE,MID", "DEFLATE,END"]
        self.__fifty_fifty_combi_twin = ["TWIN,FRONT", "TWIN,MID", "TWIN,END"]
        self.__others_macau_combi_options_1 = ["FRONT", "MID", "END"]
        self.__others_macau_combi_options_2 = ["BIG", "SMALL"]
        self.__others_macau_combi_options_3 = ["ODD", "EVEN"]
        self.__others_zodiac_zh_a = ["DRAGON","RABBIT","TIGER","OX"]
        self.__others_zodiac_zh_b = ["RAT","PIG","ROOSTER","MONKEY","GOAT","HORSE","SNAKE"]

    def four_three_two_d(self, bet_option: str):
        if bet_option == "4D":
            return f"{random.randint(0, 9)},{random.randint(0, 9)},{random.randint(0, 9)},{random.randint(0, 9)}"
        elif bet_option == "3D":
            return f"{random.randint(0, 9)},{random.randint(0, 9)},{random.randint(0, 9)}"
        else:
            return f"{random.randint(0, 9)},{random.randint(0, 9)}"

    def colok(self, bet_option: str) -> str:
        if bet_option == "COLOK_BEBAS":
            return str(random.randint(0, 9))
        elif bet_option == "COLOK_MACAU":
            ls = non_repeat_numbers(2)
            return f"{ls[0]},{ls[1]}"
        elif bet_option == "COLOK_NAGA":
            ls = non_repeat_numbers(3)
            return f"{ls[0]},{ls[1]},{ls[2]}"
        elif bet_option == "COLOK_JITU":
            d = random.randint(0, 9)
            return f"{d},{self.__colok_jitu_options[random.randint(0, 3)]}"

    def fifty_fifty(self, bet_option: str) -> str:
        if bet_option == "50_50_GENERAL":
            return self.__fifty_fifty_general_options[random.randint(0, 5)]
        elif bet_option == "50_50_SPECIAL":
            opt1 = self.__fifty_fifty_special_options_1[random.randint(0, 3)]
            opt2 = self.__fifty_fifty_special_options_2[random.randint(0, 3)]
            return f"{opt1},{opt2}"
        elif bet_option == "50_50_COMBI_MONO":
            return self.__fifty_fifty_combi_mono[random.randint(0, 2)]
        elif bet_option == "50_50_COMBI_STEREO":
            return self.__fifty_fifty_combi_stereo[random.randint(0, 2)]
        elif bet_option == "50_50_COMBI_INFLATE":
            return self.__fifty_fifty_combi_inflate[random.randint(0, 2)]
        elif bet_option == "50_50_COMBI_DEFLATE":
            return self.__fifty_fifty_combi_deflate[random.randint(0, 2)]
        elif bet_option == "50_50_COMBI_TWIN":
            return self.__fifty_fifty_combi_twin[random.randint(0, 2)]

    def others(self, bet_option: str) -> str:
        if bet_option == "MACAU_COMBI":
            opt1 = self.__others_macau_combi_options_1[random.randint(0, 2)]
            opt2 = self.__others_macau_combi_options_2[random.randint(0, 1)]
            opt3 = self.__others_macau_combi_options_3[random.randint(0, 1)]
            return f"{opt1},{opt2},{opt3}"
        elif bet_option == "SUM_2D_ODD":
            return "ODD"
        elif bet_option == "SUM_2D_EVEN":
            return "EVEN"
        elif bet_option == "SUM_2D_SMALL":
            return "SMALL"
        elif bet_option == "SUM_2D_BIG":
            return "BIG"
        elif bet_option == "ZODIAC_ZH_A":
            return self.__others_zodiac_zh_a[random.randint(0,3)]
        elif bet_option == "ZODIAC_ZH_B":
            return self.__others_zodiac_zh_b[random.randint(0,7)]

class BetSetting:
    def __init__(self, kei: str, discount: str, prize_multiplier: str):
        self.kei = kei
        self.discount = discount
        self.prize_multiplier = prize_multiplier


content_helper = ContentHelper()


class Togel:
    def __init__(self):
        self.__bet_type_list = ["4D_3D_2D", "COLOK", "50_50", "OTHERS"]
        self.__bet_option_dict = {
            "4D_3D_2D": [],
            "COLOK": [],
            "50_50": [],
            "OTHERS": []
        }
        self.__bet_setting_dict = {}

    def load_data(self):
        with open("data/tgl_95.json", "r") as file:
            # Read the entire content of the file
            json_str = file.read()
            json_ary = json.loads(json_str)
            for item in json_ary:
                bet_type = item['bet_type']
                bet_option = item['bet_option']
                key = f"{bet_type}:{bet_option}"
                self.__bet_setting_dict[key] = BetSetting(discount=item['discount'],
                                                   kei=item['kei'],
                                                   prize_multiplier=item['prize_multiplier'])
                self.__bet_option_dict[bet_type].append(bet_option)

    def generate_randon_bets(self, game_code: str, bets_count: int) -> List[dict]:
        now_timestamp = int(time.time())
        bet_type_count = len(self.__bet_type_list)
        bets: list[dict[str, str]] = []
        for i in range(bets_count):
            j = (i + now_timestamp) % bet_type_count
            bet_type = self.__bet_type_list[j]
            item = BetVo()
            item.game_code = game_code
            item.bet_type = bet_type

            bet_option_idx = random.randint(0, len(self.__bet_option_dict[bet_type]) - 1)
            bet_option = self.__bet_option_dict[bet_type][bet_option_idx]
            item.bet_option = bet_option
            bet_setting_key = f"{bet_type}:{bet_option}"
            bet_setting = self.__bet_setting_dict[bet_setting_key]
            item.prize_multiplier = bet_setting.prize_multiplier

            if bet_type == "4D_3D_2D":
                item.stake_amount = "1000.000"
                item.bet_amount = "1000.000"
                item.discount_percent = bet_setting.discount
                item.bet_content = content_helper.four_three_two_d(bet_option)
            elif bet_type == "COLOK":
                item.stake_amount = "5000.000"
                item.bet_amount = "5000.000"
                item.discount_percent = bet_setting.discount
                item.bet_content = content_helper.colok(bet_option)
            elif bet_type == "50_50":
                item.stake_amount = "5000.000"
                item.kei_percent = bet_setting.kei
                kei_amount = decimal.Decimal(item.kei_percent).__mul__(decimal.Decimal(item.stake_amount))
                bet_amount = decimal.Decimal(item.stake_amount).__add__(kei_amount)
                item.bet_amount = format(bet_amount, ".3f")
                item.bet_content = content_helper.fifty_fifty(bet_option)
            elif bet_type =="OTHERS":
                item.stake_amount = "5000.000"
                item.bet_content = content_helper.others(bet_option)
                if bet_setting.discount is not None:
                    item.discount_percent = bet_setting.discount
                    discount_amount = decimal.Decimal(item.discount_percent).__mul__(decimal.Decimal(item.stake_amount))
                    bet_amount = decimal.Decimal(item.stake_amount).__sub__(discount_amount)
                    item.bet_amount = format(bet_amount, ".3f")
                if bet_setting.kei is not None:
                    item.kei_percent = bet_setting.kei
                    kei_amount = decimal.Decimal(item.kei_percent).__mul__(decimal.Decimal(item.stake_amount))
                    bet_amount = decimal.Decimal(item.stake_amount).__add__(kei_amount)
                    item.bet_amount = format(bet_amount, ".3f")

            print(json.dumps(item.to_dict(), indent=4))
            bets.append(item.to_dict())
        return bets


togel = Togel()
togel.load_data()

