import os
from werkzeug.security import check_password_hash

class LoginCheck:
    def __init__(self, root):
        self._root = root

    def _check_username_and_password(self, username, password):
        try:
            file_path = os.path.join("data", "users.csv")
            with open(file_path, "r", encoding="utf-8") as f:
                for row in f:
                    row = row.replace("\n", "")
                    info = row.split(";")
                    username_from_file = info[0]
                    if username_from_file == username:
                        if check_password_hash(info[1], password):
                            return True
        except FileNotFoundError:
            return "Väärä käyttäjätunnus tai salasana"
        return "Väärä käyttäjätunnus tai salasana"
    