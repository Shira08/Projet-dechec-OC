from models.Tournament import Tournament, TournamentModel
from views.TournamentView import TournamentView
from models.Round import RoundModel
from views.UserView import UserView


class TournamentController:
    def __init__(self, tournament_file):
        self.model = TournamentModel(tournament_file)
        self.view = TournamentView()
        self.user_view = UserView()

    def list_tournaments(self):
        tournaments = self.model.get_all_tournaments()
        self.view.display_tournaments(tournaments)

    def add_tournament(self):
        name, location, description = self.view.input_tournament_details()
        tournament = Tournament(name, location, description)
        print(self.model.create_tournament(tournament))

    def get_specific_tournament(self):
        specified_name = self.view.input_tournament_name()
        tournament_info = self.model.get_tournament_info(specified_name)
        self.view.display_tournament(tournament_info)

    def create_round(self):
        specified_name = self.view.input_tournament_name()
        get_tournament = self.model.get_tournament_for_round(specified_name)

        if get_tournament and not isinstance(get_tournament, str):
            round_model = RoundModel()
            updated_tournament = self.model.update_tournament(round_model.create_round(get_tournament))
            print(f'{updated_tournament}')
            self.view.display_round_info(updated_tournament)
        else:
            return print(get_tournament)

    def update_round(self):
        specified_name = self.view.input_tournament_name()
        get_players, tournament, actual_round = self.model.get_last_round_of_tournament(specified_name)
        scores = self.view.display_round_player(get_players)
        self.model.update_scores(tournament, scores, actual_round)

    def get_all_players_alphabetic_order(self):
        specified_name = self.view.input_tournament_name()
        players = self.model.get_tournament_players(specified_name)
        self.user_view.display_users(players)

    def get_all_round_tournament(self):
        specified_name = self.view.input_tournament_name()
        all_round = self.model.get_tournament_for_round(specified_name)
        self.view.display_all_round(all_round)
