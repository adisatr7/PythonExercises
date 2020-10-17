from Experiments.MathQuiz.DataBank import Questions

# IN GAME SETTINGS

# Enter how many questions the quiz should have
# Input -1 for endless questions
rounds = 2

# How many times user are given chance to re-answer a wrongly answered questions
chance = 3

# -------------------- IGNORE PAST THIS LINE ---------------------------------------

game = Questions(rounds, chance)
game.start_quiz()
