import json
from datetime import datetime
import random


def to_dict_player(player):
    return {
            "last_name": player["last_name"],
            "first_name": player["first_name"],
            "birth_date": player['birth_date'],
            "chess_id": player['chess_id'],
            "score_total": player['score_total']
    }


class Round:
    def __init__(self,name=""):
        self.name = name
        self.start_date = datetime.now().strftime('%d-%m-%Y')
        self.end_date = None
        self.players = []

    def to_dict(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "players": self.players
        }


class RoundModel:
    def mytourn(self,tournament):
        print(tournament.to_dict()["name"])

    def create_round(self, tournament):
        round_name = f'Round{tournament["current_round"] + 1}'
        round_ = Round(round_name)
        round_to_dict = round_.to_dict()

        round_to_dict['players'], tournament['past_matches'] = self.generate_pair(
            tournament["players_list"],
            tournament["current_round"],
            tournament["past_matches"])

        tournament["current_round"] += 1
        tournament["round_list"].append(round_to_dict)
        print(f'Final tournament: {json.dumps(tournament)}')
        return tournament

    def generate_pair(self, players_list,current_round,past_matches):
        round_ = Round()
        if current_round == 0:
            print("iam first coming")
            selected_pair = random.sample(players_list, 2)
            print(f'selcted ones {selected_pair}')
            selected_players_list = []
            for player in selected_pair:
                selected_players_list.append({
                    "player": to_dict_player(player),
                    "score": 0
                })

            past_matches.append((selected_pair[0]['chess_id'], selected_pair[1]['chess_id']))

        else:
            sorted_players = sorted(players_list, key=lambda x: x['score_total'], reverse=True)
            selected_pair = []
            selected_players_list = []

            while True:
                sorted_players_pair = random.sample(sorted_players, 2)

                # Vérifie si la paire aléatoire existe déjà dans past_matches
                if ((sorted_players_pair[0]['chess_id'], sorted_players_pair[1]['chess_id']) not in past_matches and
                        (sorted_players_pair[1]['chess_id'], sorted_players_pair[0]['chess_id']) not in past_matches):
                    break

            print("not first time coming")
            selected_pair.append((sorted_players_pair[0], sorted_players_pair[1]))
            past_matches.append((sorted_players_pair[0]['chess_id'], sorted_players_pair[1]['chess_id']))

            print(f"Users pair {selected_pair}")

            # Création de la liste finale avec les informations des joueurs sélectionnés
            selected_players_list.append({
                "player": to_dict_player(sorted_players_pair[0]),
                "score": 0
            })
            selected_players_list.append({
                "player": to_dict_player(sorted_players_pair[1]),
                "score": 0
            })

            print(selected_players_list)

        return selected_players_list, past_matches



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
