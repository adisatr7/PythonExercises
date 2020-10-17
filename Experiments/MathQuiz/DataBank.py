import random


class Questions:

    def __init__(self, rounds, chance):
        self.rounds = int(rounds)
        self.chance = int(chance)
        self.score = 0

    @staticmethod
    def randomize_operator(seed):
        if seed == 1:
            return "+"
        elif seed == 2:
            return "-"
        elif seed == 3:
            return "*"
        elif seed == 4:
            return "/"

    @staticmethod
    def get_answer(num1, op, num2):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return num1 / num2

    def show_question(self):

        level_chance = self.chance

        # Generate a new math problem
        op = self.randomize_operator(random.randrange(1, 5, 1))
        is_division = op == "/"
        num1 = random.randrange(2, 1000, 2) if is_division else random.randrange(1, 1000, 1)
        num2 = 2 if is_division else random.randrange(1, num1 - 1, 1)

        while level_chance > 0:

            # Prints the math problem to user
            answer = int(input("\n" + str(num1) + " " + op + " " + str(num2) + " = "))

            # Check if the answer is correct
            if answer == self.get_answer(num1, op, num2):
                self.score += 20
                print("Well done! You have earned +10 pts")
                print("Current score: " + str(self.score) + "\n")
                break

            # If the answer is wrong
            else:
                level_chance -= 1
                if level_chance > 0:
                    print("Try again! (Chance: " + str(level_chance) + "x)")
                else:
                    print("You have lost -10 pts!")
                    break

        self.score -= 10

    def start_quiz(self):
        if self.rounds == -1:
            given_questions = 1
            while True:
                self.show_question()
                given_questions += 1
                print("\nCurrent score:", str(self.score), "\nQuestions faced:", str(given_questions))

        else:
            for q in range(self.rounds):
                self.show_question()
                print("\nCurrent score:", str(self.score), "\nQuestions: " + str(q+1) + "/" + str(self.rounds))

        print("\nGame over!")
        print("Final score:", self.score)