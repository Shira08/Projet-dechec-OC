class UserView:
    @staticmethod
    def display_users(users):
        if not any(users):
            print("There is no users in the database")
        else:
            for user in users:
                print(
                    f"Chess ID: {user['chess_id']}, "
                    f"Name: {user['first_name']} "
                    f"{user['last_name']}, "
                    f"Birthdate: {user['birth_date']}"
                )

    @staticmethod
    def input_user_details():
        last_name = input("Enter last name: ")
        first_name = input("Enter first name: ")
        birth_date = input("Enter birth date (DD/MM/YYYY): ")
        chess_id = input("Enter chess ID: ")
        return last_name, first_name, birth_date, chess_id
