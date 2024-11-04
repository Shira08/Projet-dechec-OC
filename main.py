from Controllers.TournamentController import TournamentController
from Controllers.UserController import UserController


def main():
    user_controller = UserController('data/users/users.json')
    tournament_controller = TournamentController('data/tournament/tournaments.json')
    while True:
        print("1. list of users by alphabetic order"
              "\n2. Add user"
              "\n3. List all tournaments"
              "\n4. Get a tournament"
              "\n5. List players per tournament in alphabetic order "
              "\n6. Get all rounds of a tournament and matches of each "
              "\n7. Create tournament"
              "\n8. Create round"
              "\n9. Update round scores and mark as terminate"
              "\n98.Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            user_controller.list_users()
        elif choice == '2':
            user_controller.add_user()
        elif choice == '3':
            tournament_controller.list_tournaments()
        elif choice == '4':
            tournament_controller.get_specific_tournament()
        elif choice == '5':
            tournament_controller.get_all_players_alphabetic_order()
        elif choice == '6':
            tournament_controller.get_all_round_tournament()
        elif choice == '7':
            tournament_controller.add_tournament()
        elif choice == '8':
            tournament_controller.create_round()
        elif choice == '9':
            tournament_controller.update_round()
        elif choice == '98':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
