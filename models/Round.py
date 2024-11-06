import json
from datetime import datetime
import random


def to_dict_player(player):
    return {
        "last_name": player["last_name"],
        "first_name": player["first_name"],
        "birth_date": player["birth_date"],
        "chess_id": player["chess_id"],
        "score_total": player["score_total"],
    }


class Round:
    def __init__(self, name=""):
        self.name = name
        self.start_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.end_date = None
        self.players = []

    def to_dict(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "players": self.players,
            "terminate": False,
        }


class RoundModel:

    def create_round(self, tournament):
        """
        Create a round using tournament
        Make sure last round has been terminated
        """
        round_name = f'Round{tournament["current_round"] + 1}'
        round_ = Round(round_name)
        round_to_dict = round_.to_dict()
        round_to_search = f'Round{tournament["current_round"]}'
        print(f"ok{tournament}")

        if tournament["current_round"] == 4:
            tournament["end_date"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            return "The tournament is finished. You can no longer create new rounds."
        elif (
            not tournament["round_list"]
            or any(
                round_to_search == round["name"] and round["terminate"]
                for round in tournament["round_list"]
            )
            or tournament["current_round"] == 0
        ):
            round_to_dict["players"], tournament["past_matches"] = self.generate_pair(
                tournament["players_list"],
                tournament["current_round"],
                tournament["past_matches"],
            )
            tournament["current_round"] += 1
            if tournament["current_round"] == 4:
                tournament["end_date"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            tournament["round_list"].append(round_to_dict)

            print(f"Final tournament: {json.dumps(tournament)}")
            return tournament

        # Checking if any round has the same name but is not yet terminated
        for round in tournament["round_list"]:
            if round_to_search == round["name"] and not round["terminate"]:
                text_result = f"Make sure the {round['name']} has been terminated"
                return text_result
        return []

    def generate_pair(self, players_list, current_round, past_matches):
        """
        Generate a pair of users for each match
        -Get ramdom users for first time
        -For other time follow the scores
        """
        selected_players_list = []
        selected_pair = []
        if current_round == 0:
            selected_pair = random.sample(players_list, 2)

            for player in selected_pair:
                selected_players_list.append(
                    {"player": to_dict_player(player), "score": 0}
                )

            past_matches.append(
                (selected_pair[0]["chess_id"], selected_pair[1]["chess_id"])
            )

        elif current_round < 4:
            sorted_players = sorted(
                players_list, key=lambda x: x["score_total"], reverse=True
            )

            while True:
                top_player = sorted_players.pop(0)

                opponent = None
                for player in sorted_players[:]:
                    if (
                        top_player["chess_id"],
                        player["chess_id"],
                    ) not in past_matches and (
                        player["chess_id"],
                        top_player["chess_id"],
                    ) not in past_matches:
                        opponent = player
                        sorted_players.remove(player)
                        break

                if opponent:
                    selected_pair.append((top_player, opponent))
                    past_matches.append((top_player["chess_id"], opponent["chess_id"]))

                    selected_players_list.append(
                        {"player": to_dict_player(top_player), "score": 0}
                    )
                    selected_players_list.append(
                        {"player": to_dict_player(opponent), "score": 0}
                    )

                    print(selected_players_list)
                    break
                else:
                    sorted_players = sorted(
                        players_list, key=lambda x: x["score_total"], reverse=True
                    )

            return selected_players_list, past_matches

        return selected_players_list, past_matches
