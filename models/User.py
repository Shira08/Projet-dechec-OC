import json

FILEPATH= 'data/users/users.json'
class User:
    def __init__(self, last_name, first_name, birth_date, chess_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score_total = 0

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score_total": self.score_total
        }

class UserModel:
    def __init__(self, file_path= FILEPATH):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_users(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.users, f, indent=4)

    def add_user(self, user: User):
        self.users.append(user.to_dict())
        self.save_users()

    def get_all_users(self):
        return self.users
