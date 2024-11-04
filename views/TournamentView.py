class TournamentView:
    @staticmethod
    def display_tournaments(tournaments):
        if not any(tournaments):
            print("There is no tournament, Add one.")
        else:
            for tournament in tournaments:
                print(
                    f"Tournament Name: {tournament['name']}, "
                    f"Lieu: {tournament['location']},"
                    f"Number of round {tournament['current_round']}, "
                    f"Start date: {tournament['start_date']}"
                )

    @staticmethod
    def display_round_info(tournament):
        if "round_list" in tournament and tournament["round_list"]:
            current_round_index = tournament["current_round"]
            if 0 < current_round_index <= len(tournament["round_list"]):
                current_round = tournament["round_list"][current_round_index - 1]
                players = current_round.get("players", [])

                print(
                    f"{current_round['name']} Information for Tournament: {tournament['name']}"
                )
                for player_info in players:
                    player = player_info.get("player", {})
                    nom = player.get("last_name", "N/A")
                    prenom = player.get("first_name", "N/A")
                    chess_id = player.get("chess_id", "N/A")
                    print(f"Name: {prenom} {nom}, Chess ID: {chess_id}")
            else:
                print("No valid current round available for this tournament.")

    @staticmethod
    def display_tournament(tournament):
        if not any(tournament):
            print("Name has not been found")
        else:
            print(
                f"Tournament Name: {tournament['name']}, "
                f"Start Date: {tournament['start_date']}, "
                f"End Date: {tournament['end_date'] if tournament['end_date'] is not None else 'Not closed'}"
            )

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

    @staticmethod
    def update_scores():
        name = input("Please specify the tournament you want to get: ")
        return name

    @staticmethod
    def display_all_round(round_list):
        for round in round_list:
            print(f"\nRound Name: {round['name']}")
            print(f"Start Date: {round['start_date']}")
            print(f"End Date: {round['end_date'] if round['end_date'] else 'In progress'}")
            print(f"Round Terminated: {'Yes' if round['terminate'] else 'No'}")
            print("Matches:")

            for match in round["players"]:
                player = match["player"]
                print(
                    f"  - {player['first_name']} {player['last_name']} (ID: {player['chess_id']})"
                )
                print(f"    Birth Date: {player['birth_date']}")
                print(f"    Score in Match: {match['score']}")
                print(f"    Total Score: {player['score_total']}\n")

    @staticmethod
    def display_round_player(players_list):
        print("Find below the player associated to the last round")
        for player_info in players_list:
            player = player_info.get("player", {})
            name = player.get("last_name", "N/A")
            surname = player.get("first_name", "N/A")
            chess_id = player.get("chess_id", "N/A")
            print(f"Name: {surname} {name}, Chess ID: {chess_id}")
        result = input(
            f"Please choose one of these result: \n"
            f"1. Winner: {players_list[0]['player']['chess_id']} \n"
            f"2. Winner: {players_list[1]['player']['chess_id']} \n"
            f"3. Match Null \n"
        )

        match result:
            case "1":
                return players_list[0]["player"]["chess_id"]
            case "2":
                return players_list[1]["player"]["chess_id"]
            case "3":
                return 0
            case _:
                result = input(
                    f"Please choose one of these result: \n"
                    f"1. Winner: {players_list[0]['player']['chess_id']} \n"
                    f"2. Winner: {players_list[1]['player']['chess_id']} \n"
                    f"3. Match Null \n"
                )
