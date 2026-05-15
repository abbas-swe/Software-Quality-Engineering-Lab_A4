from database import load_leaderboard, save_leaderboard

class Leaderboard:

    def add_score(self, username, score):
        data = load_leaderboard()

        found = False

        for d in data:
            if d["username"] == username:
                d["score"] += score
                found = True
                break

        if not found:
            data.append({"username": username, "score": score})

        save_leaderboard(data)

    def display(self):
        data = load_leaderboard()
        data = sorted(data, key=lambda x: x["score"], reverse=True)

        print("\n===== LEADERBOARD =====")
        for d in data:
            print(d["username"], "->", d["score"])