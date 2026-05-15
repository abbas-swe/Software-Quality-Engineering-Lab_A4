from database import load_users, save_users

class Auth:

    def signup(self):
        users = load_users()

        username = input("Create username: ")
        password = input("Create password: ")

        for u in users:
            if u["username"] == username:
                print("User already exists!")
                return None

        users.append({"username": username, "password": password})
        save_users(users)

        print("Signup successful!")
        return username

    def login(self):
        users = load_users()

        while True:
            username = input("Username: ")
            password = input("Password: ")

            for u in users:
                if u["username"] == username and u["password"] == password:
                    print("Login successful!")
                    return username

            print("Invalid credentials, try again.\n")