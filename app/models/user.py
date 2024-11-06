class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = []

def add_user(username, password):
    user = User(username, password)
    users.append(user)
    return user

def get_users():
    return users

def authenticate(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False

add_user("user1", "pword1")
add_user("user2", "pword2")
add_user("user3", "pword3")
add_user("admin","1234")

