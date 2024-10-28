from models.Tournament import Tournament, TournamentModel
from views.TournamentView import TournamentView
from models.Round import RoundModel,Round

class TournamentController:
    def __init__(self, tournament_file):
        self.model = TournamentModel(tournament_file)
        self.view = TournamentView()

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
        get_tournament = self.model.get_tournament_for_round(specified_name).to_dict()
        if get_tournament:
            round_model = RoundModel()
            updated_tournament = self.model.update_tournaments(round_model.create_round(get_tournament))
            self.view.display_round_info(updated_tournament)