from auth import Auth
from quiz import Quiz
from leaderboard import Leaderboard


def main():
    auth = Auth()
    quiz = Quiz()
    lb = Leaderboard()

    print("===== ONLINE QUIZ SYSTEM =====")

    print("1. Login")
    print("2. Signup")

    choice = input("Choose: ")

    if choice == "2":
        username = auth.signup()
        if not username:
            return
    else:
        username = auth.login()

    while True:
        print("\n===== MENU =====")
        print("1. Quiz 1")
        print("2. Quiz 2")
        print("3. Leaderboard")
        print("4. Exit")

        c = input("Choose: ")

        if c == "1":
            score = quiz.quiz1()
            print("Score:", score)
            lb.add_score(username, score)

        elif c == "2":
            score = quiz.quiz2()
            print("Score:", score)
            lb.add_score(username, score)

        elif c == "3":
            lb.display()

        elif c == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


main()