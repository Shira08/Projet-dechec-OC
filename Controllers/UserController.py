from models.User import User, UserModel
from views.UserView import UserView

class UserController:
    def __init__(self, user_file):
        self.model = UserModel(user_file)
        self.view = UserView()

    def list_users(self):
        users = self.model.get_all_users()
        sorted_users = sorted(users, key=lambda user: user["last_name"])
        self.view.display_users(sorted_users)

    def add_user(self):
        last_name, first_name, birth_date, chess_id = self.view.input_user_details()
        user = User(last_name, first_name, birth_date, chess_id)
        self.model.add_user(user)
