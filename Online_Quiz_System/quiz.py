import time

class Quiz:

    def run_quiz(self, questions):
        score = 0
        print("\nQuiz Started! (Each question = 1 mark)")

        for q in questions:
            print("\n", q["question"])

            for opt in q["options"]:
                print("-", opt)

            start = time.time()
            ans = input("Answer: ")
            end = time.time()

            if end - start > 10:
                print("Time up!")
                continue

            if ans.lower() == q["answer"].lower():
                print("Correct! +1")
                score += 1
            else:
                print("Wrong!")

        return score

    def quiz1(self):
        return self.run_quiz([
            {
                "question": "What is the capital of Pakistan?",
                "options": ["Karachi", "Islamabad", "Lahore", "Peshawar"],
                "answer": "Islamabad"
            },
            {
                "question": "2 + 2 = ?",
                "options": ["3", "4", "5", "6"],
                "answer": "4"
            }
        ])

    def quiz2(self):
        return self.run_quiz([
            {
                "question": "HTML is used for?",
                "options": ["Web structure", "AI", "Database", "OS"],
                "answer": "Web structure"
            },
            {
                "question": "CPU stands for?",
                "options": ["Central Processing Unit", "Control Power Unit", "Central Print Unit", "None"],
                "answer": "Central Processing Unit"
            }
        ])