class TournamentView:
    @staticmethod
    def display_tournaments(tournaments):
        if not any(tournaments):
           print( "There is no tournament, Add one.")
        else:
            for tournament in tournaments:
                print(f"Tournament Name: {tournament['name']}, "
                      f"Lieu: {tournament['location']},"
                      f"Number of round {tournament['current_round']}, "
                      f"Start date: {tournament['start_date']}")

    @staticmethod
    def display_round_info(tournament):
        # Check if there are any rounds created
        if 'round_list' in tournament and tournament['round_list']:
            current_round_index = tournament['current_round']  # Get the current round index
            # Ensure that the current round index does not exceed the number of rounds in roundlist
            if 0 < current_round_index <= len(tournament['round_list']):
                current_round = tournament['round_list'][current_round_index - 1]  # Access the current round
                players = current_round.get('players', [])

                print(f"{current_round['name']} Information for Tournament: {tournament['name']}")
                for player_info in players:
                    player = player_info.get('player', {})
                    # Extracting details, assuming the player dict has 'nom', 'prenom', and 'chess_id'
                    nom = player.get('last_name', 'N/A')
                    prenom = player.get('first_name', 'N/A')
                    chess_id = player.get('chess_id', 'N/A')
                    print(f"Name: {prenom} {nom}, Chess ID: {chess_id}")
            else:
                print("No valid current round available for this tournament.")
        else:
            print("No rounds available for this tournament.")

    @staticmethod
    def display_tournament(tournament):
        if not any(tournament):
           print( "Name has not been found")
        else:
            print(f"Tournament Name: {tournament['name']}, "
                  f"Start Date: {tournament['start_date']}, "
                  f"End Date: {tournament['end_date'] if tournament['end_date'] is not None else 'Not closed'}")


    @staticmethod
    def input_tournament_details():
        name = input("Enter tournament name (ex: Tournament1): ")
        location = input("Enter tournament location: ")
        description = input("Enter the description: ")
        return name, location, description

    @staticmethod
    def input_tournament_name():
        name = input("Please specify the tournament you want to get: ")
        return name
