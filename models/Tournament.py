import json
from datetime import datetime
import random
from models.User import UserModel


class Tournament:

    def __init__(
        self,
        name,
        location,
        description="",
        tours=4,
        start_date=None,
        end_date=None,
        current_round=0,
        round_list=None,
        players_list=None,
        past_matches=None,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date or datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.end_date = end_date
        self.tours = tours
        self.current_round = current_round
        self.round_list = round_list if round_list is not None else []
        self.players_list = players_list if players_list is not None else []
        self.past_matches = past_matches if past_matches is not None else set()
        self.description = description

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            location=data.get("location"),
            description=data.get("description", ""),
            tours=data.get("tours", 4),
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
            current_round=data.get("current_round", 0),
            round_list=data.get("round_list", []),
            players_list=data.get("players_list", []),
            past_matches=set(data.get("past_matches", [])),
        )

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "tours": self.tours,
            "current_round": self.current_round,
            "round_list": self.round_list,
            "players_list": self.players_list,
            "description": self.description,
            "past_matches": list(self.past_matches),
        }


class TournamentModel:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tournaments = self.load_tournament()

    def load_tournament(self):
        try:
            with open(self.file_path, "r") as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
                else:
                    return []
        except FileNotFoundError:
            return []

    def save_tournaments(self):
        with open(self.file_path, "w") as f:
            json.dump(self.tournaments, f, indent=4)

    def validate_tournament(self, tournament_check):
        tournaments = self.load_tournament()
        for tournament in tournaments:
            if tournament["name"] == tournament_check["name"]:
                return False
        return True

    def create_tournament(self, tournament: Tournament):
        tournament_dict = tournament.to_dict()
        if self.validate_tournament(tournament_dict):
            print(f'Old Value{tournament_dict["players_list"]}')
            user_model = UserModel()
            users_list = random.sample(user_model.get_all_users(), 8)
            tournament_dict["players_list"] = users_list
            print(f'New value{tournament_dict["players_list"]}')
            self.tournaments.append(tournament_dict)
            self.save_tournaments()
            return "Tournament created successfully!"
        else:
            return "Sorry, this name has already been assigned to a tournament."

    def get_all_tournaments(self):
        return self.tournaments

    def get_tournament_info(self, specified_name):
        for tournament in self.tournaments:
            if tournament["name"] == specified_name:
                return {
                    "name": tournament["name"],
                    "start_date": tournament["start_date"],
                    "end_date": tournament["end_date"],
                }
        return []

    def get_tournament(self, specified_name):
        for tournament in self.tournaments:
            if tournament["name"] == specified_name:
                return tournament["round_list"]
        return []

    def get_tournament_players(self, specified_name):
        for tournament in self.tournaments:
            if tournament["name"] == specified_name:
                sorted_players_list = sorted(
                    tournament["players_list"], key=lambda x: x["last_name"]
                )
                return sorted_players_list
        return []

    def get_tournament_for_round(self, specified_name):
        for tournament in self.tournaments:
            if tournament["name"] == specified_name:
                return tournament
        return "This tournament does not exist"

    def get_last_round_of_tournament(self, specified_name):
        for tournament in self.tournaments:
            if tournament["name"] == specified_name:
                round_to_check = f'Round{tournament["current_round"]}'
                print(f"Checking round: {round_to_check}")

                for round_in_tournament in tournament["round_list"]:
                    if round_in_tournament[
                        "name"
                    ] == round_to_check and not round_in_tournament.get(
                        "terminate", False
                    ):
                        return (
                            round_in_tournament.get("players", []),
                            tournament,
                            round_to_check,
                        )
        return []

    def update_tournament_in_file(self, tournaments_data):
        try:
            # Debug print to verify tournament data before saving
            print(f"Tournament data to save: {tournaments_data}")

            # Open the file and write data in JSON format
            with open(self.file_path, "w") as file:
                json.dump(tournaments_data, file, indent=4)
            print("Tournament data successfully updated.")

        except (IOError, TypeError) as e:
            # Handle exceptions for file I/O errors or data serialization issues
            print(f"Error saving tournament data to file: {e}")

    def update_tournament(self, tournament):
        # Ensure the tournament is valid before updating
        if isinstance(tournament, str):
            return tournament
        if tournament:
            tournaments_data = self.load_tournament()
            for i, existing_tournament in enumerate(tournaments_data):
                if existing_tournament["name"] == tournament["name"]:
                    tournaments_data[i] = tournament
                    print("Updated tournament data:", tournaments_data)
                    self.update_tournament_in_file(
                        tournaments_data
                    )  # Ensure data is saved to file
                    return tournament
            print("Tournament not found.")
        else:
            print("No tournament data found or you have reached  .")
        return None

    def update_scores(self, tournament, scores, round_):
        for round_item in tournament["round_list"]:
            if round_item["name"] == round_:
                for player in round_item["players"]:
                    if scores == 0:
                        player["score"] = 0
                    else:
                        if player["player"]["chess_id"] == scores:
                            for tournament_player in tournament["players_list"]:
                                if (
                                    tournament_player["chess_id"]
                                    == player["player"]["chess_id"]
                                ):
                                    tournament_player["score_total"] += 1
                            player["score"] = 1
                        else:
                            player["score"] = 0
                round_item["terminate"] = True
                round_item["end_date"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.update_tournament(tournament)
        print(f"{round_} has been successfully updated and mark as terminate")
