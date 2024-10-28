import json
from datetime import datetime
import random

class Round:
    def __init__(self,name=""):
        self.name = name
        self.start_date = datetime.now().strftime('%d-%m-%Y')
        self.end_date = None
        self.players = []
#        self.past_matches = set()

    def to_dict(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "players": self.players
        }

    def to_dict_player(self, player):
        return {
            "player": {
                "last_name": player['last_name'],
                "first_name": player['first_name'],
                "birth_date": player['birth_date'],
                "chess_id": player['chess_id'],
                "score_total": player['score_total']
            },
            "score": 0  # Initialize score; you can set it based on your logic
        }
class RoundModel:
    def mytourn(self,tournament):
        print(tournament.to_dict()["name"])

    def create_round(self,tournament):
        round_name = f'Round{tournament["current_round"]+ 1}'
        round_ = Round(round_name)
        round_to_dict = round_.to_dict()
        past_matches = set(tournament["past_matches"])
        round_to_dict['players'] = self.generate_pair(
                                                      tournament["players_list"],
                                                      tournament["current_round"],
                                                      past_matches)
        tournament["current_round"] +=1
        tournament["round_list"].append(round_to_dict)
        print(f' Final tournament'
              f'{tournament}')
        return tournament

    def generate_pair(self, players_list,current_round,past_matches):
        round_ = Round()
        if current_round == 0:
            print("iam first coming")
            selected_pair = random.sample(players_list, 2)
            print(f'selcted ones {selected_pair}')
            selected_players_list = []

            selected_players_list.append({
                "player1": round_.to_dict_player(selected_pair[0])["player"],
                "player2": round_.to_dict_player(selected_pair[1])["player"],
                "score": 0
            })

            past_matches.add((selected_pair[0]['chess_id'], selected_pair[1]['chess_id']))

        else:
            sorted_players = sorted(players_list, key=lambda x: x['score_total'], reverse=True)
            selected_pair = []
            selected_players_list = []
            print("not first time coming")
            # Affichage de la liste triée
            for i in range(0, len(sorted_players) - 1, 2):
                player1 = sorted_players[i]
                player2 = sorted_players[i + 1]

                if ((player1['chess_id'], player2['chess_id']) not in past_matches and
                        (player2['chess_id'], player1['chess_id']) not in past_matches):
                    selected_pair.append((player1, player2))
                    past_matches.add((player1['chess_id'], player2['chess_id']))
            selected_players_list.append({
                "player1": round_.to_dict_player(selected_pair[0])["player"],
                "player2": round_.to_dict_player(selected_pair[1])["player"],
                "score": 0
            })
        return selected_players_list , past_matches



"""
ajouter ça sous la forme

players: [
{
joueur1: {
        "last_name": "Ronaldo",
        "first_name": "BestJ",
        "birth_date": "03/07/1900",
        "chess_id": "AB01345",
        "score_total": 0
    },
score: 1
},
{
joueur2: {
        "last_name": "Ronaldo",
        "first_name": "BestJ",
        "birth_date": "03/07/1900",
        "chess_id": "AB01345",
        "score_total": 0
    },
score: 1
}]

Ma préoccupation est comment je peux voir

"""
